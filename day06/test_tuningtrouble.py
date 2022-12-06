import unittest
import day06.tuningtrouble as day6


class TestTuningTrouble(unittest.TestCase):
    def testFindMarkerPart1(self):
        self.assertEqual(day6.find_marker(
            "bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(day6.find_marker(
            "nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(day6.find_marker(
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(day6.find_marker(
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)
        input = open("./day06/input.txt").read()
        self.assertEqual(day6.find_marker(input, 4), 1235)

    def testFindMarkerPart2(self):
        self.assertEqual(day6.find_marker(
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
        self.assertEqual(day6.find_marker(
            "bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(day6.find_marker(
            "nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(day6.find_marker(
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(day6.find_marker(
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)
        input = open("./day06/input.txt").read()
        self.assertEqual(day6.find_marker(input, 14), 3051)
