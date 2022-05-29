def palindrome_nums():
    list_of_nums = input().split(", ")
    for i in range(len(list_of_nums)):
        number = list_of_nums[i]
        if number == number[::-1]:
            print(True)
        else:
            print(False)


palindrome_nums()



