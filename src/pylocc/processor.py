from dataclasses import dataclass
from typing import Dict, List, Tuple, Iterable


class Report:
    __slots__ = ['file_type', 'code', 'comments', 'blanks']

    def __init__(self,file_type, code: int = 0, comments: int = 0, blanks: int = 0):
        self.file_type=file_type
        self.code = code
        self.comments = comments
        self.blanks = blanks

    def increment_code(self, count: int = 1):
        """Increments the code count by the specified amount."""
        self.code += count

    def increment_comments(self, count: int = 1):
        """Increments the comments count by the specified amount."""
        self.comments += count

    def increment_blanks(self, count: int = 1):
        """Increments the blanks count by the specified amount."""
        self.blanks += count

    @property
    def total(self) -> int:
        """Returns the total count of code and comments."""
        return self.code + self.comments + self.blanks


@dataclass
class ProcessorConfiguration:
    """Language Configuration for the loc counter processor.
    Defines the characteristics of the code that will be used to process the code files,
    such as what makes a line comment or a multi line comment"""
    file_type: str
    file_extensions: List[str]
    line_comment: List[str]
    multiline_comment: List[Tuple[str, str]]

    @staticmethod
    def load_from_dict(configs) -> List['ProcessorConfiguration']:
        assert configs is not None, "configs can't be None"
        return [ProcessorConfiguration(file_type=lang,
                                       file_extensions=lang_config['extensions'],
                                    line_comment=lang_config['line_comment'] if 'line_comment' in lang_config else [],
                                    multiline_comment=lang_config['multi_line'] if 'multi_line' in lang_config else []
                                       ) for lang, lang_config in configs.items()]


class Processor:
    def __init__(self, config: List[ProcessorConfiguration] = []):
        configurations = config or [ProcessorConfiguration(file_type='txt',
                                                           file_extensions=[
                                                               'txt'],
                                                           line_comment=["//",],
                                                           multiline_comment=[])]
        self.config:Dict[str, ProcessorConfiguration] = {}
        for c in configurations:
            for ft in c.file_extensions:
                self.config[ft] = c
        # self.config = {ft: c [for ft in c.file_extensions] for c in configurations}

    def process(self, text: Iterable[str], file_extension='txt') -> Report:
        """Counts the number of words in the given text."""
        file_configuration = self.config.get(
            file_extension, self.config['txt'])

        report = Report(file_configuration.file_type)
        in_multi_line_comment = False
        for line in text:
            stripped_line = line.strip()
            if not stripped_line:
                # If the line is blank it's easy
                report.increment_blanks()
            elif file_configuration.line_comment and stripped_line.startswith(file_configuration.line_comment[0]):
                # If the line is not blank, it can contains code, comments or both, if the comment is after a valid code block,
                # therefore we only check for the comment line pattern at the beginning of the line.
                # Even if the line may contains the line comment pattern after the code block, we still want to count this line as a code one.
                report.increment_comments()
            elif file_configuration.multiline_comment and \
                    (in_multi_line_comment or
                     stripped_line.startswith(file_configuration.multiline_comment[0][0])):
                # If the line begins with the multiline comment start pattern, we are entering a commented block and until the termination
                # pattern, we will continue incrementing the commented line counter
                in_multi_line_comment = not stripped_line.endswith(
                    file_configuration.multiline_comment[0][1])
                report.increment_comments()
            else:
                report.increment_code()
        return report
