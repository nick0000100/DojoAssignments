class Classroom(object):

    def __init__(self, name, room ={}):
        self.name = name
        self.room = room

    def add(self, kid):
        self.room[kid] = "new kid"
        return self

    def allSpeak(self):
        for kid in self.room:
            kid.speak()
            return self


class Kid(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def speak(self):
        print self.first, self.last
        return self

# class Classroom(object):
#     def __init__(self, name = "Generic Classroom"):
#         self.name = name
#         self.room = []
    
#     def add(self, childObj):
#         self.room.append(childObj)
#         return self

#     def allSpeak(self):
#         print "\nRoll Call!\n-------"
#         for child in self.room:
#             child.speak();
#         return self

# class Kid(object):
#     def __init__ (self, first = "GenericFirst", last = "GenericLast"):
#         self.first = first.title()
#         self.last = last.title()

#     def speak(self):
#         print "My name is {} {}".format(self.first, self.last)

kid1 = Kid("nick", "sor")
kid2 = Kid("jon", "jon")
# kid1.speak()

class1 = Classroom("python")
class1.add(kid1)
class1.add(kid2)
class1.allSpeak()
