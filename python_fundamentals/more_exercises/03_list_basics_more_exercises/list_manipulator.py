def even_or_odd(list, data):
    if data == "even":
        list = [x for x in list if x % 2 == 0]
    elif data == "odd":
        list = [x for x in list if x % 2 != 0]
    return list


def exchange(list, i):
    if 0 <= i < len(list):
        list = list[i + 1:] + list[:i + 1]
    else:
        print("Invalid index")
    return list


def max_even_odd(list, filtered_list):
    if len(filtered_list) > 0:
        max_num = max(filtered_list)
        for num in range(len(list) - 1, -1, -1):
            if list[num] == max_num:
                return num
    else:
        return "No matches"


def min_even_odd(list, filtered_list):
    if len(filtered_list) > 0:
        min_num = min(filtered_list)
        for num in range(len(list) - 1, -1, -1):
            if list[num] == min_num:
                return num
    else:
        return "No matches"


def first_even_odd(list, count, filtered_list):
    first_count_evens = []
    if count > len(list):
        return "Invalid count"
    else:
        if count >= len(filtered_list):
            return filtered_list
        else:
            for num in range(count):
                first_count_evens.append(filtered_list[num])
        return first_count_evens


def last_even_odd(list, count, filtered_list):
    last_count_evens = []
    if count > len(list):
        return "Invalid count"
    else:
        if count >= len(filtered_list):
            return filtered_list
        else:
            last_count_evens = filtered_list[:len(filtered_list) - count - 1:-1]
        return last_count_evens[::-1]


my_list_of_ints = [int(x) for x in input().split()]
command = input()

while command != "end":
    data = command.split()
    action = data[0]
    if action == "exchange":
        index = int(data[1])
        my_list_of_ints = exchange(my_list_of_ints, index)
    elif action == "max":
        type = data[1]
        filtered_list = even_or_odd(my_list_of_ints, type)
        print(max_even_odd(my_list_of_ints, filtered_list))
    elif action == "min":
        type = data[1]
        filtered_list = even_or_odd(my_list_of_ints, type)
        print(min_even_odd(my_list_of_ints, filtered_list))
    elif action == "first":
        count = int(data[1])
        type = data[2]
        filtered_list = even_or_odd(my_list_of_ints, type)
        print(first_even_odd(my_list_of_ints, count, filtered_list))
    elif action == "last":
        count = int(data[1])
        type = data[2]
        filtered_list = even_or_odd(my_list_of_ints, type)
        print(last_even_odd(my_list_of_ints, count, filtered_list))

    command = input()

print(my_list_of_ints)
