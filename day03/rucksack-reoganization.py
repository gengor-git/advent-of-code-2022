input_file = "day03/input.txt"

priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

def get_prio_by_letter(x):
    return priorities[x]

def find_double_items():
    with open('./day03/input.txt') as rucksacks:
        priority_values = 0
        counter = 0
        for rucksack in rucksacks:
            counter += 1
            print("\nRucksack {0}".format(counter))
            rucksack_size = len(rucksack)-1
            compartment1 = rucksack[0:int(rucksack_size/2)]
            compartment2 = rucksack[int(rucksack_size/2):rucksack_size]
            if len(compartment1) != len(compartment2):
                print("ERROR")
                break;

            already_found = ""
            for item in compartment1:
                if compartment2.count(item) > 0 and item != already_found:
                    already_found = item
                    priority_values += priorities[item]

        print(priority_values)

def find_badges():
    with open("./day03/input.txt") as input:
        data_raw = [x for x in input.read().splitlines()]
        data = list(zip(*(iter(data_raw),) * 3))
        result = sum(get_prio_by_letter((set(group[0]) & set(group[1]) & set(group[2])).pop()) for group in data)

        print(result)

if __name__ == "__main__":
    # find_double_items()
    find_badges()