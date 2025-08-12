from unittest import TestCase

from pylocc.language import Language
from pylocc.processor import ProcessorConfiguration, ProcessorConfigurationFactory


class TestProcessorConfigurationFactory(TestCase):

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
        self.factory = ProcessorConfigurationFactory(
            [self.sql_config, self.text_config])

    def test_should_return_configuration_per_extension(self):
        config = self.factory.get_configuration(file_extension='txt')
        assert config is not None
        self.assertEqual(config.file_type, Language.PLAIN_TEXT)

        config = self.factory.get_configuration(file_extension='sql')
        assert config is not None
        self.assertEqual(config.file_type, Language.SQL)

    def test_should_return_configuration_per_file_type(self):
        config = self.factory.get_configuration(file_type=Language.PLAIN_TEXT)
        assert config is not None
        self.assertEqual(config.file_type, Language.PLAIN_TEXT)

        config = self.factory.get_configuration(file_type=Language.SQL)
        assert config is not None
        self.assertEqual(config.file_type, Language.SQL)
