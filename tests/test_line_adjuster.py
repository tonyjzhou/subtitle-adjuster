import unittest

from line_adjuster import adjust


class TestLineAdjuster(unittest.TestCase):
    def test_adjust_nonTimeLine_returnSameString(self):
        line = "non Time Line"
        self.assertEqual(line, adjust(line, 1))

    def test_adjust_timeLineByAddingOneSecond_returnTimeLineOneSecondLater(self):
        line = "00:01:47,559 --> 00:01:50,892"
        self.assertEqual("00:01:48,559 --> 00:01:51,892", adjust(line, 1))

    def test_adjust_timeLineBySubtractingOneSecond_returnTimeLineOneSecondLater(self):
        line = "00:01:47,559 --> 00:01:50,892"
        self.assertEqual("00:01:46,559 --> 00:01:49,892", adjust(line, -1))

    def test_adjust_timeLineByAddingOneSecond_returnTimeLineOneSecondLater2(self):
        line = "00:59:59,559 --> 09:59:59,892"
        self.assertEqual("01:00:00,559 --> 10:00:00,892", adjust(line, 1))

    def test_adjust_timeLineBySubtractingOneSecond_returnTimeLineOneSecondLater2(self):
        line = "00:01:00,559 --> 00:02:00,892"
        self.assertEqual("00:00:59,559 --> 00:01:59,892", adjust(line, -1))


if __name__ == '__main__':
    unittest.main()
