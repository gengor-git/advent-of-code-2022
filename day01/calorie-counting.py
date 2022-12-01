input_file = "day01/input.txt"

elves_backpack = [0]

with open(input_file, "r") as input:
    for entry in input:
        try:
            fruit = int(entry)
            elves_backpack[-1] = elves_backpack[-1] + fruit
        except ValueError:
            # This means the was not fruit but an empty line.
            # So we start a new elf's backpack with 0 fruit in it.
            elves_backpack.append(0)
    print("We've got {0} elves.".format(len(elves_backpack)))

    elves_backpack.sort(reverse=True)
    top1 = elves_backpack[0]
    top2 = elves_backpack[1]
    top3 = elves_backpack[2]
    print("Maximum calories with one elf are: {0}".format(top1))
    print("Calories with the top 3 are: {0}".format(top1 + top2 + top3))
