from product import product

class store(object):

    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        for i in range(0, len(self.products) - 1):
            if product.name == self.products[i].name:
                self.products.remove(self.products[i])
        return self

    def inventory(self):
        count = 0
        for product in self.products:
            count += 1
            print "Product:", count
            print product.price
            print product.name
            print product.weight
            print product.brand
            print product.cost
            print product.status
        return self
            

product1 = product(100, "thing", 20, "sdfsdfd", 232, "for sale")
product2 = product(11, "th", 10, "d", 2, "for sale")
# product1.displayInfo()

store = store([], "home", "me")
store.add_product(product1)
store.add_product(product2)
store.remove_product(product1)
store.inventory()