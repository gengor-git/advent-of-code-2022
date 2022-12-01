import os
from re import I

input_file = "day01/input.txt"


elves_backpack = [0]

with open(input_file, "r") as input:
    for entry in input:
        try:
            fruit = int(entry)
            # print("entry a number {0}".format(fruit))
            elves_backpack[-1] = elves_backpack[-1] + fruit
        except:
            # print("entry not a number")
            elves_backpack.append(0)
    print(len(elves_backpack))

    max_value = None

    for num in elves_backpack:
        if (max_value is None or num > max_value):
            max_value = num

    print('Maximum value:', max_value)
