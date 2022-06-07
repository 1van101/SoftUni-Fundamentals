def palindrome_nums(nums):
    for i in range(len(nums)):
        number = nums[i]
        if number == number[::-1]:
            print(True)
        else:
            print(False)


list_of_nums = input().split(", ")
palindrome_nums(list_of_nums)



