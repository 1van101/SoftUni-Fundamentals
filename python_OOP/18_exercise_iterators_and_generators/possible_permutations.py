from itertools import permutations


def possible_permutations(nums):
    res = permutations(nums)

    for perm in res:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]