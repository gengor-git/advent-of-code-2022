import unittest
import day09.ropebridge as day9

test_input_file = "day09/test_input.txt"
input_file = "day09/input.txt"

class TestRopeBridge(unittest.TestCase):
    def testPart1withTestInput(self):
        self.assertEqual(day9.move_through_grid(
            day9.load_data(test_input_file)), 13)

    def testPart1withMyInput(self):
        self.assertEqual(day9.move_through_grid(
            day9.load_data(input_file)), 6209)
