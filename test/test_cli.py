import unittest
import os
from click.testing import CliRunner
from pylocc.cli import pylocc

class TestCli(unittest.TestCase):

    def test_pylocc_single_file(self):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('test.py', 'w') as f:
                f.write('print("hello world")')

            # Act
            result = runner.invoke(pylocc, ['test.py'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    def test_pylocc_directory(self):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            os.makedirs('test_dir')
            with open('test_dir/test.py', 'w') as f:
                f.write('print("hello world")')

            # Act
            result = runner.invoke(pylocc, ['test_dir'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    def test_pylocc_by_file(self):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('test.py', 'w') as f:
                f.write('print("hello world")')

            # Act
            result = runner.invoke(pylocc, ['--by-file', 'test.py'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Provider', result.output)

if __name__ == '__main__':
    unittest.main()
