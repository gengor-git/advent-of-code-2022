
import unittest
import day04.cleanupassignments as day4


class TestCleanupAssignments(unittest.TestCase):

    def testPart1(self):
        self.assertEqual(day4.find_fully_contained(), 560)

    def testPart2(self):
        self.assertEqual(day4.find_overlap(), 839)


if __name__ == '__main__':
    unittest.main()
