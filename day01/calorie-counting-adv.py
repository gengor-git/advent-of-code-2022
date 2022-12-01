input_file = "day01/input.txt"
elves = open(input_file).read().split("\n\n")
elves_backpacks = [sum(map(int, elf.split())) for elf in elves]
print(max(elves_backpacks))
print(sum(sorted(elves_backpacks)[-3:]))
