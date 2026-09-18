from unittest import TestCase
from typing import Dict

from pylocc.language import Language
from pylocc.processor import ProcessorConfiguration, count_locs


class TestProcessor(TestCase):
    def setUp(self):
        self.text_config = ProcessorConfiguration(
            file_type=Language.PLAIN_TEXT,
            file_extensions=['txt'],
            line_comment=[],
            multiline_comment=[]
        )
        self.sql_config = ProcessorConfiguration(
            file_type=Language.SQL,
            file_extensions=['sql'],
            line_comment=["--"],
            multiline_comment=[]
        )

    def test_should_count_code_lines(self):
        text = ["line 1", "line 2", "line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.code, 3)

    def test_should_count_commented_lines(self):
        text = ["line 1", "line 2", "line 3", r"//Commented Line"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.comments, 0)

    def test_should_count_multi_lines_comments(self):
        text = ["line 1",
                "/* at line 2 the comment begins",
                "line 3",
                r"at line 4 the comment ends */"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.code, 4)
        self.assertEqual(report.comments, 0)
        self.assertEqual(report.total, 4)

    def test_should_count_blank_lines(self):
        text = ["line 1", "", "line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.code, 2)

        text = ["line 1", "    ", "line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.code, 2)

    def test_should_count_total_lines_in_file(self):
        text = ["line 1", "line 2", "line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.total, 3)

        text = ["line 1", "", "line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.total, 3)

        text = ["line 1", "", "//line 3"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.total, 3)

    def test_should_count_comments_lines_according_to_the_file_type(self):
        text = ["line 1", "line 2", "line 3", r"//Commented Line"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.comments, 0)

        text = ["line 1", "line 2", "line 3", r"-- Commented Line"]
        report = count_locs(text, file_configuration=self.sql_config)
        self.assertEqual(report.comments, 1)

    def test_should_count_as_code_lines_not_totally_commented(self):
        text = ["line 1", "line 2", "line 3",
                r"there is code here // Comment"]
        report = count_locs(text, file_configuration=self.text_config)
        self.assertEqual(report.code, 4)
        self.assertEqual(report.comments, 0)

    def test_should_count_zero_lines_for_empty_file(self):
        report = count_locs([], file_configuration=self.text_config)
        self.assertEqual(report.code, 0)
        self.assertEqual(report.comments, 0)
        self.assertEqual(report.blanks, 0)
        self.assertEqual(report.total, 0)

    def test_should_keep_multiline_state_when_line_comment_inside_block(self):
        # The line-comment branch takes precedence over the multiline branch, so a line
        # starting with the line-comment pattern inside an open multiline block is counted
        # as a comment and does not close the block (matches the original semantics).
        cfg = ProcessorConfiguration(
            file_type=Language.PLAIN_TEXT,
            file_extensions=['txt'],
            line_comment=['#'],
            multiline_comment=[['<#', '#>']]
        )
        text = ['<# block', '# inside', 'more', '#> end', 'code']
        report = count_locs(text, file_configuration=cfg)
        self.assertEqual(report.code, 0)
        self.assertEqual(report.comments, 5)
        self.assertEqual(report.total, 5)

    def test_should_close_multiline_block_on_termination_line(self):
        # When the terminating pattern does not start with the line-comment pattern,
        # the block is closed and subsequent lines are counted as code.
        cfg = ProcessorConfiguration(
            file_type=Language.PLAIN_TEXT,
            file_extensions=['txt'],
            line_comment=['//'],
            multiline_comment=[['/*', '*/']]
        )
        text = ['/* start', 'mid', 'end */', 'code']
        report = count_locs(text, file_configuration=cfg)
        self.assertEqual(report.code, 1)
        self.assertEqual(report.comments, 3)
        self.assertEqual(report.total, 4)


class TestProcessorConfiguration(TestCase):
    def setUp(self):
        import json
        with open(r"./tests/test_language.json", 'r') as f:
            self.config_data: Dict[str, Dict] = json.load(f)

    def test_should_load_config_from_json(self):
        configs = ProcessorConfiguration.load_from_dict(self.config_data)
        self.assertEqual(len(configs), 2)
        java_config = next((c for c in configs if c.file_type == Language.JAVA), None)
        self.assertIsNotNone(java_config)
        self.assertEqual(java_config.file_type, Language.JAVA)
        self.assertEqual(java_config.file_extensions, ['java'])
        self.assertEqual(java_config.line_comment, ['//'])
        self.assertEqual(java_config.multiline_comment, [[ "/*", "*/" ]])
        javascript_config = next((c for c in configs if c.file_type == Language.JAVASCRIPT), None)
        self.assertIsNotNone(javascript_config)
        self.assertEqual(javascript_config.file_type, Language.JAVASCRIPT)
        self.assertEqual(javascript_config.file_extensions, ["js", "cjs", "mjs"])
        self.assertEqual(javascript_config.line_comment, ['//'])
        self.assertEqual(javascript_config.multiline_comment, [[ "/*", "*/" ]])
