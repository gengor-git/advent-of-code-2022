# Day 1: Calorie Counting

## Results

- We've got 254 elves.
- Maximum calories with one elf are: 75622
- Calories with the top 3 are: 213159

## Other Examples via Reddit

[Dryctas](https://www.reddit.com/r/adventofcode/comments/z9ezjb/comment/iyhb9y8/?utm_source=share&utm_medium=web2x&context=3)

```Bash
(sed 's?^$?x?g' input.txt | tr '\nx' '+\n' | sed -r 's?^\+|\+$??g'; echo '') | bc | sort -n | tail -n 3 | tr '\n' ' ' | awk '{print $3; print $1+$2+$3}'
```

[Zweedeend](https://www.reddit.com/r/adventofcode/comments/z9ezjb/comment/iyh9nu7/?utm_source=share&utm_medium=web2x&context=3)

```Python
elves = open("day1.txt").read().split("\n\n")
calories = [sum(map(int, elf.split())) for elf in elves]
print(max(calories), sum(sorted(calories)[-3:]))

```
