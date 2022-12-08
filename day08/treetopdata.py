#!/usr/bin/env python
# coding: utf-8

# # Day 8: Treetop Tree House
#
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.
#
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
input_file = "day08/input.txt"
data_raw = open(input_file).read().strip().splitlines()
ert = [list(map(int, line)) for line in data_raw]
data = pd.DataFrame(ert)
plt.figure(figsize=(12, 12))
heat_map = sns.heatmap(data, linewidth=0, annot=False)
heat_map.figure.savefig('./day08/heatmap.svg', transparent=True)
heat_map.figure.savefig('./day08/heatmap.png', transparent=True)
