def shopping_list(budget, **kwargs):
    bought_products = []

    if budget < 100:
        return "You do not have enough budget."

    for product, data in kwargs.items():
        price = data[0] * data[1]

        if budget - price >= 0 and len(bought_products) < 5:
            budget -= price
            bought_products.append((f"You bought {product} for {price:.2f} leva."))

    result = '\n'.join(bought_products)
    return result



