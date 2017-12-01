import numpy as np


def find_sum(captcha, shift=1):
    numbers = np.asarray([int(ch) for ch in captcha])
    shifted = np.roll(numbers, shift)

    return np.dot(numbers == shifted, numbers)

with open('captcha.txt', 'r') as f:
    captcha = f.read()

print("Part 1: {}".format(find_sum(captcha)))
print("Part 2: {}".format(find_sum(captcha, len(captcha)/2)))
