import unittest
import day08.treetopscanner as day8

input_file = "day08/input.txt"
test_input_file = "day08/test_input.txt"


class TestTreeTopScanner(unittest.TestCase):
    def testPart1(self):
        mapdata = open(input_file).read().strip().splitlines()
        self.assertEqual(day8.scan_tress(mapdata)[0], 1803)

    def testPart2(self):
        mapdata = open(input_file).read().strip().splitlines()
        self.assertEqual(max(day8.scan_tress(mapdata)[1]), 268912)
