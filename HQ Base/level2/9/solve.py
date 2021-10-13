from itertools import permutations

nums = [2, 5, 4, 7]

for row in permutations(nums):
    print("".join(str(x) for x in list(row)))