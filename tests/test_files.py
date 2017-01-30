import unittest

from files import make_new_base_name, is_valid_file_type, make_srt_new
from lib.line_adjuster import adjust


class TestFiles(unittest.TestCase):
    def test_make_new_base_name(self):
        new_base_name = make_new_base_name('/path/to/my/file.srt')
        self.assertEqual('file.new.srt', new_base_name)

    def test_is_valid_file_type(self):
        self.assertEqual(True, is_valid_file_type('file.srt'))
        self.assertEqual(False, is_valid_file_type('file.txt'))

    def test_make_srt_new(self):
        srt_new = make_srt_new('/new/path', '/old/path/file.srt')
        self.assertEqual('/new/path/file.new.srt', srt_new)


if __name__ == '__main__':
    unittest.main()
