import unittest
import day05.supplystacks as day5


class TestSupplyStacks(unittest.TestCase):

    def testPart1(self):
        expected = "WHTLRMZRC"
        result = day5.part1()

        self.assertEqual(result, expected)

    def testPart2(self):
        expected = "GMPMLWNMG"
        result = day5.part2()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
