from project import Product


class ProductRepository():
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        try:
            searched_product = [x for x in self.products if x.name == product_name][0]
            return searched_product
        except IndexError:
            return None

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = ""
        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"
        return result.rstrip("\n")