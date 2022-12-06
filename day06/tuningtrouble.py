
def isLastUnique(datastream) -> bool:
    val = datastream[-1]
    compare = datastream[0:-1]
    print("Looking for '{}' in '{}' from '{}'".format(val, compare, datastream))

    if val not in compare:
        if len(datastream) >= 2:
            print("Checking rest of string '{}'.".format(compare))
            return isLastUnique(compare)
        else:
            return True
    else:
        False


def part1(datastream: str) -> int:
    print("Datastream is '{}'.".format(datastream))
    result = 0
    for i in range(4, len(datastream)):
        print("{} is {}".format(i, datastream[i-1]))
        if isLastUnique(datastream[i-4:i]):
            return i
    return result


def part2(datastream: str) -> int:
    print("Datastream is '{}'.".format(datastream))
    result = 0
    for i in range(14, len(datastream)):
        print("{} is {}".format(i, datastream[i-1]))
        if isLastUnique(datastream[i-14:i]):
            return i
    return result


if __name__ == "__main__":
    # input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    input = open("day06/input.txt").read()
    result1 = part1(input)
    result2 = part2(input)
    print("Part 1 result: {}".format(result1))
    print("Part 2 result: {}".format(result2))  # 23?
