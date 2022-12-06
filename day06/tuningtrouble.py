
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


def find_marker(datastream: str, marker_length: int) -> int:
    print("Datastream is '{}'.".format(datastream))
    result = 0
    for i in range(marker_length, len(datastream)):
        print("{} is {}".format(i, datastream[i-1]))
        if isLastUnique(datastream[i-marker_length:i]):
            return i
    return result


if __name__ == "__main__":
    # input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    input = open("day06/input.txt").read()
    result_marker_4 = find_marker(input, 4)
    result_marker_14 = find_marker(input, 14)
    print("Part 1 result: {}".format(result_marker_4))
    print("Part 2 result: {}".format(result_marker_14))  # 23?
