import unittest
import os
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from pylocc.cli import pylocc

class TestCli(unittest.TestCase):

    @patch('pylocc.cli.load_language_config')
    @patch('pylocc.cli.Processor')
    def test_pylocc_single_file(self, mock_processor, mock_load_config):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('test.py', 'w') as f:
                f.write('print("hello world")')

            mock_config = MagicMock()
            mock_config.file_extensions = ['py']
            mock_load_config.return_value = [mock_config]

            mock_proc_instance = mock_processor.return_value
            mock_proc_instance.process.return_value = MagicMock(total=1, code=1, comments=0, blanks=0, file_type='python')

            # Act
            result = runner.invoke(pylocc, ['test.py'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    @patch('pylocc.cli.load_language_config')
    @patch('pylocc.cli.Processor')
    def test_pylocc_directory(self, mock_processor, mock_load_config):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            os.makedirs('test_dir')
            with open('test_dir/test.py', 'w') as f:
                f.write('print("hello world")')

            mock_config = MagicMock()
            mock_config.file_extensions = ['py']
            mock_load_config.return_value = [mock_config]

            mock_proc_instance = mock_processor.return_value
            mock_proc_instance.process.return_value = MagicMock(total=1, code=1, comments=0, blanks=0, file_type='python')

            # Act
            result = runner.invoke(pylocc, ['test_dir'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    @patch('pylocc.cli.load_language_config')
    @patch('pylocc.cli.Processor')
    def test_pylocc_by_file(self, mock_processor, mock_load_config):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('test.py', 'w') as f:
                f.write('print("hello world")')

            mock_config = MagicMock()
            mock_config.file_extensions = ['py']
            mock_load_config.return_value = [mock_config]

            mock_proc_instance = mock_processor.return_value
            mock_proc_instance.process.return_value = MagicMock(total=1, code=1, comments=0, blanks=0, file_type='python')

            # Act
            result = runner.invoke(pylocc, ['--by-file', 'test.py'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Provider', result.output)

if __name__ == '__main__':
    import os
    unittest.main()
