import unittest
import day07.filesystemchecks as day7


class TestFileSystemChecks(unittest.TestCase):
    def testMaxSize(self):
        data = open("day07/input.txt").read().strip().splitlines()
        root = day7.create_directory_dict(data)
        sizes = sorted(day7.calculate_sizes(root))
        self.assertEqual(sizes[-1], 42036703)
