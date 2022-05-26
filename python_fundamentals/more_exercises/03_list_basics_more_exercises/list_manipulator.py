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