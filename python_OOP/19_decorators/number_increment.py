def number_increment(numbers):

    def increase():

        increased_numbers = [x + 1 for x in numbers]
        return increased_numbers

    return increase()


print(number_increment([1, 2, 3])) 