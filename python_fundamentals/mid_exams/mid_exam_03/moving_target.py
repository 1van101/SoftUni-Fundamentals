def index_is_valid(nums, i):
    if i in range(len(nums)):
        return True


def shoot(nums, i, power):
    if index_is_valid(nums, i):
        nums[i] -= power
        if nums[i] <= 0:
            nums.pop(i)
    return nums


def add(nums, i, value):
    if index_is_valid(nums, i):
        nums.insert(i, value)
    else:
        print("Invalid placement!")
    return nums


def strike(nums, i, radius):
    start = i - radius
    end = i + radius
    if start >= 0 and end < len(nums):
        nums = nums[:start] + nums[end + 1:]
    else:
        print("Strike missed!")
    return nums


targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)


    command = input()

print("|".join(str(x) for x in targets))