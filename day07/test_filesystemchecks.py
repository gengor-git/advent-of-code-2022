import unittest
import day07.filesystemchecks as day7


class TestFileSystemChecks(unittest.TestCase):

    def testReadRootTotalSum(self):
        test_input_data = open("day07/test_input.txt").read().splitlines()
        self.assertEqual(day7.read_drive(test_input_data).size, 48381165)
