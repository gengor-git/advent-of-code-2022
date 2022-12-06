import unittest
import day06.tuningtrouble as day6


class TestTuningTrouble(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(day6.part1("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(day6.part1("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(day6.part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(day6.part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
        input = open("./day06/input.txt").read()
        self.assertEqual(day6.part1(input), 1235)
