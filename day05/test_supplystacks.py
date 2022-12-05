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

    def testClean(self):
        self.assertEqual(day5.clean(
            "[P]     [L]         [T]            "), "P # L # # T # # #")
        self.assertEqual(day5.clean(
            "[M]     [Q] [W]     [H] [R] [G]    "), "M # Q W # H R G #")
        self.assertEqual(day5.clean(
            "[B] [Q] [D] [T] [T] [B] [N] [L] [D]"), "B Q D T T B N L D")


if __name__ == '__main__':
    unittest.main()
