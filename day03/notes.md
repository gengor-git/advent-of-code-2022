# Day 3: Rucksack Reorganization

## Other Solutions

- https://www.reddit.com/r/adventofcode/comments/zb865p/comment/iyqdx7e/?utm_source=share&utm_medium=web2x&context=3

```Python
lines = open("./day03/input.txt").read().splitlines()

print(sum(
    (ord(x) - ord("a")) % 58 + 1
    for l in lines
    for x in set(l[: len(l) // 2]) & set(l[len(l) // 2 :])
))

print(sum(
    (ord(x) - ord("a")) % 58 + 1
    for a, b, c in zip(*[iter(lines)] * 3)
    for x in set(a) & set(b) & set(c)
))
```