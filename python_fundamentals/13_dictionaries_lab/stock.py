input_string = input().split()
store = {}
searched_products = input().split()

for i in range(0, len(input_string), 2):
    key = input_string[i]
    value = input_string[i + 1]
    store[key] = int(value)


for product in searched_products:
    if product in input_string:
        print(f"We have {store[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")