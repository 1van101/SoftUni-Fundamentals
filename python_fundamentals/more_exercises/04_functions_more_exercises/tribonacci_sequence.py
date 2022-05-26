def get_tribonacci_sequence(num):
    counter = 0
    list_of_nums = []

    while True:
        counter += 1
        if counter > num:
            break

        if counter > 2:
            list_of_sum = list_of_nums[-3:]
            list_of_nums.append(sum(list_of_sum))
        else:
            list_of_nums.append(1)

    list_of_nums = [str(x) for x in list_of_nums]
    return " ".join(list_of_nums)


number = int(input())
print(get_tribonacci_sequence(number))