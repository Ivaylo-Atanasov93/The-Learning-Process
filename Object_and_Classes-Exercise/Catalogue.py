class Catalogue:
    def __init__(self, name):
        self.name = name
        self.catalogue = []

    def add_product(self, product):
        self.catalogue.append(product)

    def get_by_letter(self, letter):
        return [item for item in self.catalogue if letter == item[0]]

    def __repr__(self):
        string = f'Items in the {self.name} catalogue:\n'
        string += '\n'.join(sorted(self.catalogue))
        return string


# class Catalogue:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_by_letter(self, first_letter):
#         return [p for p in self.products if first_letter == p[0]]
#
#     def __repr__(self):
#         res = f'Items in the {self.name} catalogue:\n'
#         res += '\n'.join(sorted(self.products))
#         return res

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("M"))
print(catalogue)
