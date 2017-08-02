class Call(object):

    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID:", self.id
        print "Name:", self.name
        print "Number:", self.number
        print "Time:", self.time
        print "Reason:", self.reason
        return self

class CallCenter(object):

    def __init__(self, calls, queue):
        self.calls = calls
        self.queue = queue

    def add(self, call):
        self.queue += 1
        self.calls.append(call)
        return self

    def remove(self):
        self.queue -= 1
        self.calls[1:len(self.calls)]
        return self

    def displayInfo(self):
        for i in range(len(self.calls)):
            print "newcall"
            name = self.calls[i].name
            number = self.calls[i].number
            print "Name:", name
            print "Number", number
        print "Calls in queue", self.queue
        return self
    
    def removeNum(self, number):
        for i in range(len(self.calls) - 1):
            if self.calls[i].number == number:
                self.calls.remove(self.calls[i])
        self.queue -= 1
        return self

call1 = Call(1, "A", 12, 1, "hurt")
# call1.display()

call2 = Call(2, "B", 123, 2, "hi")
callCenter1 = CallCenter([], 0)
callCenter1.add(call1)
callCenter1.add(call2)

callCenter1.displayInfo()
callCenter1.removeNum(12)
callCenter1.displayInfo()