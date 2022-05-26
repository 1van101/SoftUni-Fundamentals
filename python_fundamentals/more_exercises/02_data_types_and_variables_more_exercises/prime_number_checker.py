def check_if_is_prime_num(number):

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            return True
    else:
        return False


num = int(input())
print(check_if_is_prime_num(num))

