import unittest
import day09.ropebridge as day9


class TestRopeBridge(unittest.TestCase):
    def __init__(self):
        self.test_input_file = "day09/test_input.txt"
        self.input_file = "day09/input.txt"

    def testPart1withTestInput(self):
        self.assertEqual(day9.move_through_grid(
            day9.load_data(self.test_input_file)), 13)

    def testPart1withMyInput(self):
        self.assertEqual(day9.move_through_grid(
            day9.load_data(self.input_file)), 0)
