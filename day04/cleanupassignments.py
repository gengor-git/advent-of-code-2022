input_file = "day04/input.txt"

def find_fully_contained():
    data = open(input_file).read().split("\n")
    counter = 0
    for entry in data:
        if entry != "":
            pair = list(entry.split(","))

            val1 = list(map(int, pair[0].split("-")))
            val2 = list(map(int, pair[1].split("-")))

            # range1 = list(range(int(val1[0]), int(val1[1])))
            # range2 = list(range(int(val2[0]), int(val2[1])))

            if is_full_overlap(val1, val2):
                counter += 1

    return counter

def find_overlap():
    data = open(input_file).read().split("\n")
    counter = 0
    for entry in data:
        if entry != "":
            pair = list(entry.split(","))
            val1 = list(map(int, pair[0].split("-")))
            val2 = list(map(int, pair[1].split("-")))

            if is_general_overlap(val1, val2):
                counter += 1

    return counter

def is_general_overlap(val1, val2):
    start1 = val1[0]
    end1 = val1[1]
    start2 = val2[0]
    end2 = val2[1]

    return start1 <= start2 and end1 >= start2 or start2 <= start1 and end2 >= start1

def is_full_overlap(val1, val2):
    start1 = val1[0]
    end1 = val1[1]
    start2 = val2[0]
    end2 = val2[1]

    return start1 <= start2 and end1 >= end2 or start2 <= start1 and end2 >= end1


# function to compare lists
def compare_sets(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    if set1 == set2:
        return True
    elif set1.issubset(set2):
        return True
    elif set2.issubset(set1):
        return True
    else:
        return False

if __name__ == "__main__":
    print(find_fully_contained())
    print(find_overlap())