def game_horizontally(nums):
    for i in range(3):
        if nums[i][0] == nums[i][1] == nums[i][2] != "0":
            if nums[i][0] == "1":
                return "First player won"
            else:
                return "Second player won"


def game_vertically(nums):
    for i in range(3):
        if nums[0][i] == nums[1][i] == nums[2][i] != "0":
            if nums[i][0] == "1":
                return "First player won"
            else:
                return "Second player won"


def game_crosswise(nums):
    if nums[2][0] == nums[1][1] == nums[0][2] != "0":
        if nums[2][0] == "1":
            return "First player won"
        else:
            return "Second player won"
    elif nums[0][0] == nums[1][1] == nums[2][2] != "0":
        if nums[0][0] == "1":
            return "First player won"
        else:
            return "Second player won"


list_of_nums = []

for c in range(3):
    numbers = input().split()
    list_of_nums.append(numbers)

if game_horizontally(list_of_nums):
    print(game_horizontally(list_of_nums))
elif game_vertically(list_of_nums):
    print(game_vertically(list_of_nums))
elif game_crosswise(list_of_nums):
    print(game_crosswise(list_of_nums))
else:
    print("Draw!")
