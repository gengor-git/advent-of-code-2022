import unittest
import day02.rockpaperscissors as day2


class TestRockPaperScissors(unittest.TestCase):
    def testPart1(self):
        rules_part_1 = {
            'A X\n': 4,
            'A Y\n': 8,
            'A Z\n': 3,
            'B X\n': 1,
            'B Y\n': 5,
            'B Z\n': 9,
            'C X\n': 7,
            'C Y\n': 2,
            'C Z\n': 6
        }
        self.assertEqual(day2.play_by_rules(rules_part_1), 12586)

    def testPart2(self):
        rules_part_2 = {
            'A X\n': 3,
            'A Y\n': 4,
            'A Z\n': 8,
            'B X\n': 1,
            'B Y\n': 5,
            'B Z\n': 9,
            'C X\n': 2,
            'C Y\n': 6,
            'C Z\n': 7
        }
        self.assertEqual(day2.play_by_rules(rules_part_2), 13193)
