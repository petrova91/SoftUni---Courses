class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        list_with_given_letter = [product for product in self.products if product.startswith(first_letter)]
        return list_with_given_letter

    def __repr__(self):
        text_to_print = f"Items in the {self.name} catalogue:\n"
        text_to_print += f'\n'.join(sorted(self.products))
        return text_to_print

# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
