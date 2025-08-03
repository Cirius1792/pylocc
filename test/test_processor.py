from unittest import TestCase
from typing import Dict

from pylocc.processor import Processor, ProcessorConfiguration


class TestProcessor(TestCase):
    def setUp(self):
        text_config = ProcessorConfiguration(
            file_type='txt',
            file_extensions=['txt'],
            line_comment=["//"],
            multiline_comment=[("/*", "*/")]
        )
        sql_config = ProcessorConfiguration(
            file_type='sql',
            file_extensions=['sql'],
            line_comment=["--"],
            multiline_comment=[]
        )
        self.processor = Processor([text_config, sql_config])

    def test_should_count_code_lines(self):
        text = ["line 1", "line 2", "line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.code, 3)

    def test_should_count_commented_lines(self):
        text = ["line 1", "line 2", "line 3", r"//Commented Line"]
        report = self.processor.process(text)
        self.assertEqual(report.comments, 1)

    def test_should_count_multi_lines_comments(self):
        text = ["line 1",
                "/* at line 2 the comment begins",
                "line 3",
                r"at line 4 the comment ends */"]
        report = self.processor.process(text)
        self.assertEqual(report.code, 1)
        self.assertEqual(report.comments, 3)
        self.assertEqual(report.total, 4)

    def test_should_count_blank_lines(self):
        text = ["line 1", "", "line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.code, 2)

        text = ["line 1", "    ", "line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.code, 2)

    def test_should_count_total_lines_in_file(self):
        text = ["line 1", "line 2", "line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.total, 3)

        text = ["line 1", "", "line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.total, 3)

        text = ["line 1", "", "//line 3"]
        report = self.processor.process(text)
        self.assertEqual(report.total, 3)

    def test_should_count_comments_lines_according_to_the_file_type(self):
        text = ["line 1", "line 2", "line 3", r"//Commented Line"]
        text_type = "txt"
        report = self.processor.process(text, file_extension=text_type)
        self.assertEqual(report.comments, 1)

        text = ["line 1", "line 2", "line 3", r"-- Commented Line"]
        text_type = "sql"
        report = self.processor.process(text, file_extension=text_type)
        self.assertEqual(report.comments, 1)

    def test_should_count_as_code_lines_not_totally_commented(self):
        text = ["line 1", "line 2", "line 3",
                r"there is code here // Comment"]
        text_type = "txt"
        report = self.processor.process(text, file_extension=text_type)
        self.assertEqual(report.code, 4)
        self.assertEqual(report.comments, 0)


class TestProcessorConfiguration(TestCase):
    def setUp(self):
        import json
        with open(r"./test/test_language.json", 'r') as f:
            self.config_data: Dict[str, Dict] = json.load(f)

    def test_should_load_config_from_json(self):
        configs = ProcessorConfiguration.load_from_dict(self.config_data)
        self.assertEqual(len(configs), 2)
        java_config = configs[0]
        self.assertEqual(java_config.file_type, 'Java')
        self.assertEqual(java_config.file_extensions, ['java'])
        self.assertEqual(java_config.line_comment, ['//'])
        self.assertEqual(java_config.multiline_comment, [[ "/*", "*/" ]])
        javascript_config = configs[1]
        self.assertEqual(javascript_config.file_type, 'JavaScript')
        self.assertEqual(javascript_config.file_extensions, ["js", "cjs", "mjs"])
        self.assertEqual(javascript_config.line_comment, ['//'])
        self.assertEqual(javascript_config.multiline_comment, [[ "/*", "*/" ]])



