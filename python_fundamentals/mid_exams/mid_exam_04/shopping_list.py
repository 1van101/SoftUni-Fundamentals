def urgent(item, products):
    if item not in products:
        products.insert(0, item)
    return products


def unnecessary(item, products):
    if item in products:
        products.remove(item)
    return products


def correct(item, n_item, products):
    products_replaced = []
    if item in products:
        for product in products:
            if product != item:
                products_replaced.append(product)
            else:
                products_replaced.append(n_item)
        return products_replaced
    else:
        return products

def rearrange(item, products):
    if item in products:
        index = products.index(item)
        if index < len(products) - 1:
            popped_product = products.pop(index)
            products.append(popped_product)
    return products


def go_shopping(products):
    print(", ".join(products))


shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        shopping_list = urgent(item, shopping_list)
    elif action == "Unnecessary":
        shopping_list = unnecessary(item, shopping_list)
    elif action == "Correct":
        new_item = command[2]
        shopping_list = correct(item, new_item, shopping_list)
    elif action == "Rearrange":
        shopping_list = rearrange(item, shopping_list)

    command = input()

go_shopping(shopping_list)