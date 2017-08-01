class product(object):
    def __init__(self, price, name, weight, brand, cost, status = "for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self
    
    def addTax(self, tax):
        self.cost = self.cost + self.cost * tax
        return self

    def returnProduct(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        elif reason == "box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price *= .8
        return self

    def displayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self