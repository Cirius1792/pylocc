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

    def test_pylocc_directory_jobs_sequential(self):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            os.makedirs('test_dir')
            with open('test_dir/test.py', 'w') as f:
                f.write('print("hello world")')

            # Act
            result = runner.invoke(pylocc, ['--jobs', '1', 'test_dir'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    def test_pylocc_directory_jobs_parallel(self):
        # Arrange: an explicit --jobs > 1 forces the pool even for small trees.
        runner = CliRunner()
        with runner.isolated_filesystem():
            os.makedirs('test_dir')
            for i in range(3):
                with open(f'test_dir/test_{i}.py', 'w') as f:
                    f.write('print("hello world")\n')

            # Act
            result = runner.invoke(pylocc, ['--jobs', '2', 'test_dir'])

            # Assert
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Total', result.output)

    def test_pylocc_no_arguments_defaults_to_cwd(self):
        # Arrange
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('test.py', 'w') as f:
                f.write('print("hello world")')

            # Act
            result = runner.invoke(pylocc, [])

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
