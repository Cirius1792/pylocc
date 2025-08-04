from unittest import TestCase

from pylocc.processor import ProcessorConfiguration, ProcessorConfigurationFactory

class TestProcessorConfigurationFactory(TestCase):

    def setUp(self):
        self.text_config = ProcessorConfiguration(
            file_type='txt',
            file_extensions=['txt'],
            line_comment=["//"],
            multiline_comment=[("/*", "*/")]
        )
        self.sql_config = ProcessorConfiguration(
            file_type='sql',
            file_extensions=['sql'],
            line_comment=["--"],
            multiline_comment=[]
        )
        self.factory = ProcessorConfigurationFactory([self.sql_config, self.text_config])

    def test_should_return_configuration_for_text_file(self):
        config = self.factory.get_configuration('txt')
        assert config is not None
        self.assertEqual(config.file_type, 'txt')

        config = self.factory.get_configuration('sql')
        assert config is not None
        self.assertEqual(config.file_type, 'sql')

