## Other Examples

[FormalPlatypus1231](https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/iyurl2s/?utm_source=share&utm_medium=web2x&context=3)

```Bash
#!/bin/bash
# Advent of Code day 4
# https://adventofcode.com/2022/day/4

part1=0
part2=0

while read line; do
  rangeA=$(echo "$line" | cut -d "," -f 1)
  rangeB=$(echo "$line" | cut -d "," -f 2)
  minA=$(echo "$rangeA" | cut -d "-" -f 1)
  maxA=$(echo "$rangeA" | cut -d "-" -f 2)
  minB=$(echo "$rangeB" | cut -d "-" -f 1)
  maxB=$(echo "$rangeB" | cut -d "-" -f 2)

  if [[ (minA -le minB && maxA -ge maxB) || (minB -le minA && maxB -ge maxA) ]]; then
    part1=$((part1+1))
  fi

  if [[ (minA -le minB && maxA -ge minB) || (minB -le minA && maxB -ge minA) ]]; then
    part2=$((part2+1))
  fi
done < input.txt

echo "Answer for part 1: $part1"
echo "Answer for part 2: $part2"
```


(chillymosh)[https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/iyuvczi/?utm_source=share&utm_medium=web2x&context=3]

```Python
with open("AdventOfCode2022/Day4/input.txt", "r") as f:
data = [l.strip() for l in f.readlines()]

total = 0 total2 = 0

for a in data: g1 = a.split(",")[0].split("-") g2 = a.split(",")[1].split("-") set1 = {int(x) for x in range(int(g1[0]), int(g1[1])+1)} set2 = {int(x) for x in range(int(g2[0]), int(g2[1])+1)} if all(i in set1 for i in set2) or all(i in set2 for i in set1): total +=1

# Part 2
  if any(i in set1 for i in set2) or any(i in set2 for i in set1):
      total2 +=1

print(total) print(total2)
```