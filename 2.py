import numpy as np


with open('spreadsheet.txt', 'r') as f:
    numbers_str = f.readlines()

numbers = np.asarray([map(int, num.split()) for num in numbers_str])
max_values = np.amax(numbers, axis=1)
min_values = np.amin(numbers, axis=1)

print("Part 1: {}".format(np.sum(max_values - min_values)))

n_entries = numbers.shape[1]
sum_rows = 0
for row in numbers:
    x, y = np.meshgrid(row, row)
    even_division = np.mod(x, y) + np.eye(n_entries)
    inds = np.where(even_division == 0)
    sum_rows += row[inds[1][0]] / row[inds[0][0]]

print("Part 2: {}".format(sum_rows))
