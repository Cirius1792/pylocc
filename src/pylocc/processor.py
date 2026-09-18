from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Iterable
from pylocc.language import Language


class Report:
    __slots__ = ['file_type', 'code', 'comments', 'blanks']

    def __init__(self, file_type: Language, code: int = 0, comments: int = 0, blanks: int = 0):
        self.file_type = file_type
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
    file_type: Language
    file_extensions: List[str]
    line_comment: List[str]
    multiline_comment: List[Tuple[str, str]]

    @staticmethod
    def load_from_dict(configs) -> List['ProcessorConfiguration']:
        """Loads the processor configurations from a dictionary."""
        assert configs is not None, "configs can't be None"
        return [ProcessorConfiguration(file_type=Language(lang),
                                       file_extensions=lang_config['extensions'],
                                       line_comment=lang_config['line_comment'] if 'line_comment' in lang_config else [
        ],
            multiline_comment=lang_config['multi_line'] if 'multi_line' in lang_config else [
        ]
        ) for lang, lang_config in configs.items()]


def load_default_language_config() -> List[ProcessorConfiguration]:
    """Load language configurations from the packaged JSON file."""
    import json
    from importlib import resources

    with resources.files('pylocc').joinpath('language.json').open('r', encoding='utf-8') as f:
        config_data = json.load(f)
    return ProcessorConfiguration.load_from_dict(config_data)


class ProcessorConfigurationFactory:

    def __init__(self, configs: List[ProcessorConfiguration]):
        self.configs_per_extension: Dict[str, ProcessorConfiguration] = {}
        if configs:
            for c in configs:
                if c:
                    for ft in c.file_extensions:
                        self.configs_per_extension[ft] = c
        self.configs_per_language: Dict[Language, ProcessorConfiguration] = {}
        if configs:
            for c in configs:
                if c:
                    self.configs_per_language[Language(c.file_type)] = c

    def get_configuration(self, file_type: Optional[Language] = None, file_extension: Optional[str] = None, or_default: Optional[str] = None) -> Optional[ProcessorConfiguration]:
        """Returns the configuration for the given language or file extension if it exists.
        Fallback to the default configuration provided or None otherwise.

        Only one of the parameters must be provided, if both are provided, an assertion error will be raised.

        Args:
            language: Language to look for in the configurations.
            file_extension (str): The file extension to look for.
            or_default (Optional[str]): The default configuration to return if the file extension is not found.
        Returns:
            Optional[ProcessorConfiguration]: The configuration for the file extension or the default configuration if provided. None otherwise.

        """
        assert (file_type is not None) ^ (
            file_extension is not None), "Either language or file_extension must be provided, but not both"
        config = None
        if file_type in self.configs_per_language:
            config = self.configs_per_language[file_type]
        elif file_extension in self.configs_per_extension:
            config = self.configs_per_extension[file_extension]
        elif or_default is not None:
            config = self.configs_per_extension.get(or_default, None)
        return config

    @staticmethod
    def get_default_factory() -> 'ProcessorConfigurationFactory':
        """Returns a default configuration factory with the built-in language configurations."""
        return ProcessorConfigurationFactory(load_default_language_config())


def count_locs(text: Iterable[str], file_configuration: ProcessorConfiguration) -> Report:
    """Counts the number of lines in the given text according to the provide configuration."""
    assert file_configuration is not None, "File Configuration can't be null"
    # Cache the comment patterns in local variables to avoid repeated attribute lookups on every line.
    line_comment = file_configuration.line_comment[0] if file_configuration.line_comment else None
    multi_line_comment = file_configuration.multiline_comment[0] if file_configuration.multiline_comment else None
    multi_line_start = multi_line_comment[0] if multi_line_comment is not None else None
    multi_line_end = multi_line_comment[1] if multi_line_comment is not None else None

    in_multi_line_comment = False
    blanks = 0
    comments = 0
    total = 0
    for line in text:
        total += 1
        stripped_line = line.lstrip()
        if not stripped_line:
            # If the line is blank it's easy
            blanks += 1
        elif line_comment is not None and stripped_line.startswith(line_comment):
            # If the line is not blank, it can contains code, comments or both, if the comment is after a valid code block,
            # therefore we only check for the comment line pattern at the beginning of the line.
            # Even if the line may contains the line comment pattern after the code block, we still want to count this line as a code one.
            comments += 1
        elif multi_line_start is not None and \
                (in_multi_line_comment or
                 stripped_line.startswith(multi_line_start)):
            # If the line begins with the multiline comment start pattern, we are entering a commented block and until the termination
            # pattern, we will continue incrementing the commented line counter
            in_multi_line_comment = not stripped_line.endswith(multi_line_end)
            comments += 1
    # Since we incremented the counters only for blanks and comments, the difference between the total number of lines and comments+blanks will be the code.
    # Doing so we avoid to increment every time the code lines and we can do it only once.
    # Note: an empty file has total == 0, so it correctly yields 0 code lines (previously it reported 1).
    return Report(file_configuration.file_type, total - blanks - comments, comments, blanks)
