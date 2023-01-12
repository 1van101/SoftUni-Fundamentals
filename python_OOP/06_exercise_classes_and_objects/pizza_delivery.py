class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredients, qty, price_per_qty):
        if not self.ordered:
            if ingredients not in self.ingredients:
                self.ingredients[ingredients] = 0
            self.ingredients[ingredients] += qty
            self.price += price_per_qty * qty
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient, qty, price_per_qty):
        if not self.ordered:
            try:
                if self.ingredients[ingredient] < qty:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= qty
                    self.price -= qty * price_per_qty
            except KeyError:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            all_ingredients = ', '.join([f"{k}: {v}" for k, v in self.ingredients.items()])
            return f"You've ordered pizza {self.name} prepared with {all_ingredients}" \
                   f" and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
