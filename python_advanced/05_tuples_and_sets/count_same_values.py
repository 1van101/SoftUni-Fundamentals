nums = [float(x) for x in input().split()]
dct = {x: nums.count(x) for x in nums}
[print(f"{x} - {y} times") for x, y in dct.items()]