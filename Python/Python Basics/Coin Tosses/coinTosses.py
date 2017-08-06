import random

def coinToss():
    head = 0
    tails = 0
    for toss in range(0, 5001):
        side = round(random.random())
        print "Attempt #" + str(toss) + ": Throwing a coin... It's a",
        if (side == 1):
            head += 1
            print "head!",
        else:
            tails += 1
            print "tail!",
        print "... Got " + str(head) + " head(s) so far and " + str(tails) + " tails(s) so far"
    print "Ending the program, thank you!"
coinToss()