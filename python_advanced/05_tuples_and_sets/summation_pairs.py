nums = [int(x) for x in input().split()]
target = int(input())
iterations = 0
pairs = []
numbers = set()
for first_num_i in range(len(nums)):
    if first_num_i < len(nums) - 1:
        for second_num_i in range(first_num_i + 1, len(nums)):
            if nums[first_num_i] + nums[second_num_i] == target:
                pairs.append(f"{nums[first_num_i]} + {nums[second_num_i]} = {target}")
                numbers.add(f"({nums[first_num_i]}, {nums[second_num_i]})")
            iterations += 1
[print(x) for x in pairs]
print(f"Iterations done: {iterations}")
[print(f"{x}") for x in numbers]
