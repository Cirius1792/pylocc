import os
import tempfile
import unittest

from pylocc.language import Language
from pylocc.parallel import (count_files_parallel, should_use_pool,
                             suggested_worker_count, POOL_MIN_FILES)
from pylocc.processor import ProcessorConfiguration, count_locs


def _text_config():
    return ProcessorConfiguration(
        file_type=Language.PLAIN_TEXT,
        file_extensions=['txt'],
        line_comment=['//'],
        multiline_comment=[['/*', '*/']]
    )


class TestShouldUsePool(unittest.TestCase):

    def test_auto_uses_pool_only_for_large_trees(self):
        self.assertFalse(should_use_pool(10, None))
        self.assertFalse(should_use_pool(POOL_MIN_FILES - 1, None))
        self.assertTrue(should_use_pool(POOL_MIN_FILES, None))
        self.assertTrue(should_use_pool(10000, None))

    def test_explicit_jobs_respected(self):
        self.assertTrue(should_use_pool(1, 2))
        self.assertTrue(should_use_pool(1000, 4))
        self.assertFalse(should_use_pool(1000, 1))


class TestSuggestedWorkerCount(unittest.TestCase):

    def test_suggested_worker_count_positive_and_capped(self):
        n = suggested_worker_count()
        self.assertGreaterEqual(n, 1)
        self.assertLessEqual(n, 8)


class TestCountFilesParallel(unittest.TestCase):

    def _make_files(self, directory, count):
        paths = []
        for i in range(count):
            path = os.path.join(directory, f'file_{i:03d}.txt')
            with open(path, 'w', encoding='utf-8') as f:
                f.write('// comment\nline of code\n\n')
            paths.append(path)
        return paths

    def test_matches_sequential_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = _text_config()
            paths = self._make_files(tmp, 12)
            expected = {}
            for p in paths:
                with open(p, 'r', encoding='utf-8') as f:
                    expected[p] = count_locs(f, file_configuration=config)

            ext_to_config = {'txt': config}
            actual, errors = count_files_parallel(paths, ext_to_config, 2)

            self.assertEqual(errors, [])
            self.assertEqual(list(actual), paths)
            # Report instances are not comparable by identity, compare values
            for p in paths:
                self.assertEqual(
                    (actual[p].code, actual[p].comments, actual[p].blanks),
                    (expected[p].code, expected[p].comments, expected[p].blanks))

    def test_collects_errors_and_keeps_good_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = _text_config()
            paths = self._make_files(tmp, 4)
            # a directory with a supported extension makes the worker raise (IsADirectoryError)
            bad = os.path.join(tmp, 'bad.txt')
            os.makedirs(bad)
            all_paths = paths[:2] + [bad] + paths[2:]

            ext_to_config = {'txt': config}
            actual, errors = count_files_parallel(all_paths, ext_to_config, 2)

            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], bad)
            self.assertEqual(set(actual), set(paths))

    def test_skips_files_without_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = _text_config()
            txt = os.path.join(tmp, 'a.txt')
            with open(txt, 'w', encoding='utf-8') as f:
                f.write('hello\n')
            unknown = os.path.join(tmp, 'b.zzz')
            with open(unknown, 'w', encoding='utf-8') as f:
                f.write('no config\n')

            ext_to_config = {'txt': config}
            actual, errors = count_files_parallel([txt, unknown], ext_to_config, 2)

            self.assertEqual(errors, [])
            self.assertEqual(list(actual), [txt])
            self.assertEqual(actual[txt].code, 1)


if __name__ == '__main__':
    unittest.main()
