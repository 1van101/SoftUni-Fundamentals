def grocery_store(**kwargs):
    products = ""
    kwargs_sorted = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for name, qty in kwargs_sorted:
        products += f"{name}: {qty}" + "\n"
    return products


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
