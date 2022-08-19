annual_tax = int(input())
shoes = 0.6 * annual_tax
uniform = shoes * 0.8
ball = uniform * 0.25
accesories = ball * 0.2
total_price = annual_tax + shoes + uniform + ball + accesories
print(f"{total_price:.2f}")