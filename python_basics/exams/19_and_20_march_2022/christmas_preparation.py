rolls_num = int(input())
fabrics_num = int(input())
glue = float(input())
discount = int(input())
total_sum = rolls_num * 5.8 + fabrics_num * 7.2 + glue * 1.2
total_sum_with_discount = total_sum - (total_sum * discount / 100)
print(f"{total_sum_with_discount:.3f}")