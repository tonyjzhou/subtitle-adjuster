import unittest

from line_adjuster import adjust
from srt_adjuster import make_new_filename


class TestSrtAdjuster(unittest.TestCase):
    def test_adjust_make_new_filename_normalFile_addNewInBase(self):
        filename = "normal.srt"
        self.assertEqual("normal_new.srt", make_new_filename(filename))

    def test_adjust_make_new_filename_fileWithoutExtension_addNewInBase(self):
        filename = "normal"
        self.assertEqual("normal_new", make_new_filename(filename))


if __name__ == '__main__':
    unittest.main()
