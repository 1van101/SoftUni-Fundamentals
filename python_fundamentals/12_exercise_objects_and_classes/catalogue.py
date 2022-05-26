class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []


    def add_product(self, product_name):
        self.products.append(product_name)


    def get_by_letter(self, first_letter):
        return [s for s in self.products if s.startswith(first_letter)]

    def __repr__(self):
        self.products.sort()
        items_of_list = "\n".join(self.products)
        return f"Items in the {self.name} catalogue:\n{items_of_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)