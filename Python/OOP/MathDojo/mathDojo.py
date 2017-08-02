class MathDojo(object):
    def __init__(self, value = 0):
        self.value = value

    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.value += k
            else:
                self.value += i
        return self

    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.value -= k
            else:
                self.value -= i
        return self

    def result(self):
        print self.value
        return self