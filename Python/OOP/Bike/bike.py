class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Price:", self.price
        print "Max Speed:", self.max_speed
        print "Miles:", self.miles

    def ride(self):
        self.miles += 10
        return self

    def reverse(self):
        if(self.miles >= 5):
            print "Reversing"
            self.miles -= 5
        return self

bike1 = Bike(200, "35 mph")
bike1 = Bike(300, "25 mph")
bike1 = Bike(400, "15 mph")

bike1.displayInfo()
bike1.ride().ride().ride().reverse().displayInfo()
# bike1.displayInfo()