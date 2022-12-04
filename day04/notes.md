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