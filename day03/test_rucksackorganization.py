import unittest
import day03.rucksackreorganization as day3


class TestRucksackReorganization(unittest.TestCase):
    def testDoublePriorites(self):
        self.assertEqual(day3.find_double_items(), 7553)

    def testBadges(self):
        self.assertEqual(day3.find_badges(), 2758)
