class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = Car(2000, "5mph", "full", "12mpg")

car2 = Car(3000, "15mph", "full", "12mpg")

car3 = Car(4000, "25mph", "full", "12mpg")

car4 = Car(5000, "35mph", "full", "12mpg")

car5 = Car(6000, "45mph", "full", "12mpg")

car6 = Car(7000, "55mph", "full", "12mpg")
