def get_perfect_num(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    return False


number = int(input())
is_perfect_num = get_perfect_num(number)

if is_perfect_num:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
