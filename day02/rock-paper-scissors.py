input_file = "day02/input.txt"


def part1():
    rules = {
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

    score = 0
    with open(input_file, "r") as strategy_guide:
        for round in strategy_guide:
            this_score = rules[round]
            score += this_score
        print(score)


def part2():
    rules = {
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

    score = 0
    with open(input_file, "r") as strategy_guide:
        for round in strategy_guide:
            this_score = rules[round]
            score += this_score
        print(score)


if __name__ == "__main__":
    part1()
    part2()
