def get_max_even_or_odd(command, list):
    if "even" in command:
        even = [x for x in list if x % 2 == 0]
        if len(even) == 0:
            return f"No matches"
        even_max = max(even)
        for i in range(len(list) - 1, -1, -1):
            if list[i] == even_max:
                return f"{i}"

    else:
        odd = [x for x in list if x % 2 != 0]
        if len(odd) == 0:
            return f"No matches"
        odd_max = max(odd)
        for i in range(len(list) - 1, -1, -1):
            if list[i] == odd_max:
                return f"{i}"



def get_min_even_or_odd(command, list):
    if "even" in command:
        even = [x for x in list if x % 2 == 0]
        if len(even) == 0:
            return f"No matches"
        even_min = min(even)
        for i in range(len(list) - 1, -1, -1):
            if list[i] == even_min:
                return f"{i}"

    else:
        odd = [x for x in list if x % 2 != 0]
        if len(odd) == 0:
            return f"No matches"
        odd_min = min(odd)
        for i in range(len(list) - 1, -1, -1):
            if list[i] == odd_min:
                return f"{i}"



def get_first_even_odd(command, list, i):
    if "even" in command:
        if i > len(list):
            return "Invalid count"
        else:
            list = [x for x in list if x % 2 == 0]
            new_list = []
            if len(list) == len(new_list):
                return new_list
            j = 0
            while i > 0:
                i -= 1
                new_list.append(list[j])
                j += 1
                if len(list) == len(new_list):
                    return new_list
            return new_list
    else:
        if i > len(list):
            return "Invalid count"
        else:
            list = [x for x in list if x % 2 != 0]
            new_list = []
            if len(list) == len(new_list):
                return new_list
            j = 0
            while i > 0:
                i -= 1
                new_list.append(list[j])
                j += 1
                if len(list) == len(new_list):
                    return new_list
            return new_list


def get_last_even_or_odd(command, list, i):
    if "even" in command:
        if i > len(list):
            return "Invalid count"
        else:
            list = [x for x in list if x % 2 == 0]
            new_list = []
            if len(list) == len(new_list):
                return new_list
            j = len(list) - 1
            while i > 0:
                i -= 1
                new_list.append(list[j])
                j -= 1
                if len(list) == len(new_list):
                    return new_list[::-1]
            return new_list[::-1]
    else:
        if i > len(list):
            return "Invalid count"
        else:
            list = [x for x in list if x % 2 != 0]
            new_list = []
            if len(list) == len(new_list):
                return new_list
            j = len(list) - 1
            while i > 0:
                i -= 1
                new_list.append(list[j])
                j -= 1
                if len(list) == len(new_list):
                    return new_list[::-1]
            return new_list[::-1]


numbers = [int(x) for x in input().split()]

while True:
    command = input().split()

    if "end" in command:
        break

    if "exchange" in command:
        i = int(command[1])
        if i >= len(numbers) or i < 0:
            print("Invalid index")
            continue
        numbers = numbers[i + 1:] + numbers[:i + 1]
    elif "max" in command:
        print(get_max_even_or_odd(command, numbers))
    elif "min" in command:
        print(get_min_even_or_odd(command, numbers))
    elif "first" in command:
        index = int(command[1])
        print(get_first_even_odd(command, numbers, index))
    elif "last" in command:
        index = int(command[1])
        print(get_last_even_or_odd(command, numbers, index))

print(numbers)

#========================
# def exchange(list, i):
#     if 0 <= i < len(list):
#         list = list[i + 1:] + list[:i + 1]
#     else:
#         print("Invalid index")
#     return list
#
#
# def max_even_odd(list, data):
#     if data == "even":
#         max_evens = [x for x in list if x % 2 == 0]
#         if len(max_evens) > 0:
#             max_even_num = max(max_evens)
#             for num in range(len(list) - 1, -1, -1):
#                 if list[num] == max_even_num:
#                     return num
#         else:
#             return "No matches"
#     elif data == "odd":
#         max_odd = [x for x in list if x % 2 != 0]
#         if len(max_odd) > 0:
#             max_odd_num = max(max_odd)
#             for num in range(len(list) - 1, -1, -1):
#                 if list[num] == max_odd_num:
#                     return num
#         else:
#             return "No matches"
#
#
# def min_even_odd(list, data):
#     if data == "even":
#         min_evens = [x for x in list if x % 2 == 0]
#         if len(min_evens) > 0:
#             min_even_num = min(min_evens)
#             for num in range(len(list) - 1, -1, -1):
#                 if list[num] == min_even_num:
#                     return num
#         else:
#             return "No matches"
#     elif data == "odd":
#         min_odd = [x for x in list if x % 2 != 0]
#         if len(min_odd) > 0:
#             min_odd_num = min(min_odd)
#             for num in range(len(list) - 1, -1, -1):
#                 if list[num] == min_odd_num:
#                     return num
#         else:
#             return "No matches"
#
#
# def first_even_odd(list, count, data):
#     if data == "even":
#         even_nums = [x for x in list if x % 2 == 0]
#         first_count_evens = []
#         if count > len(list):
#             return "Invalid count"
#         else:
#             if count >= len(even_nums):
#                 return even_nums
#             else:
#                 for num in range(count):
#                     first_count_evens.append(even_nums[num])
#             return first_count_evens
#     elif data == "odd":
#         odd_nums = [x for x in list if x % 2 != 0]
#         first_count_odds = []
#         if count > len(list):
#             return "Invalid count"
#         else:
#             if count >= len(odd_nums):
#                 return odd_nums
#             else:
#                 for num in range(count):
#                     first_count_odds.append(odd_nums[num])
#             return first_count_odds
#
#
# def last_even_odd(list, count, data):
#     if data == "even":
#         even_nums = [x for x in list if x % 2 == 0]
#         last_count_evens = []
#         if count > len(list):
#             return "Invalid count"
#         else:
#             if count >= len(even_nums):
#                 return even_nums
#             else:
#                 last_count_evens = even_nums[:len(even_nums) - count - 1:-1]
#             return last_count_evens[::-1]
#     elif data == "odd":
#         odd_nums = [x for x in list if x % 2 != 0]
#         last_count_odds = []
#         if count > len(list):
#             return "Invalid count"
#         else:
#             if count >= len(odd_nums):
#                 return odd_nums
#             else:
#                 last_count_odds = odd_nums[:len(odd_nums) - count - 1:-1]
#             return last_count_odds[::-1]
#
#
# my_list_of_ints = [int(x) for x in input().split()]
# command = input()
#
# while command != "end":
#     data = command.split()
#     action = data[0]
#     if action == "exchange":
#         index = int(data[1])
#         my_list_of_ints = exchange(my_list_of_ints, index)
#     elif action == "max":
#         type = data[1]
#         print(max_even_odd(my_list_of_ints, type))
#     elif action == "min":
#         type = data[1]
#         print(min_even_odd(my_list_of_ints, type))
#     elif action == "first":
#         count = int(data[1])
#         type = data[2]
#         print(first_even_odd(my_list_of_ints, count, type))
#     elif action == "last":
#         count = int(data[1])
#         type = data[2]
#         print(last_even_odd(my_list_of_ints, count, type))
#
#     command = input()
# 
# print(my_list_of_ints)