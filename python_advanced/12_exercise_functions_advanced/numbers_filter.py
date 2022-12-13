def even_odd_filter(**kwargs):
    numbers_dct = {}

    for type, nums in kwargs.items():
        if type == "even":
            numbers_dct[type] = [x for x in nums if x % 2 == 0]
        else:
            numbers_dct[type] = [x for x in nums if x % 2 != 0]

    return dict(sorted(numbers_dct.items(), key= lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

