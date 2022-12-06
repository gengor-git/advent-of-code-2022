
def part1(datastream: str) -> int:
    print("Datastream is '{}'.".format(datastream))
    result = 0
    for i in range(3, len(datastream)):
        print("{} is {}".format(i+1, datastream[i]))
        pre3 = datastream[i-3:i]
        pre2 = datastream[i-3:i-1]
        print("Checking against '{}'.".format(pre3))
        if datastream[i] not in pre3 and datastream[i-1] not in pre2 and datastream[i-2] != datastream[i-3]:
            return i+1

    return result


def part2(datastream: str) -> int:
    result = 0
    return result


if __name__ == "__main__":
    # input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    input = open("day06/input.txt").read()
    result = part1(input)
    print("Part 1 result: {}".format(result))
