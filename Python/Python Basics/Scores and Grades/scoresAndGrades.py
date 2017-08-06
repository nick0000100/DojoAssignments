import random

def grades():
    print "Scores and Grades"
    for num in range(0, 10):
        random_num = random.randint(60,100)
        if (random_num >= 60 and random_num <= 69):
            print "Score: " + str(random_num) + "; Your grade is D"
        elif (random_num >= 70 and random_num <= 79):
            print "Score: " + str(random_num) + "; Your grade is C"
        elif (random_num >= 80 and random_num <= 89):
            print "Score: " + str(random_num) + "; Your grade is B"
        elif (random_num >= 90 and random_num <= 100):
            print "Score: " + str(random_num) + "; Your grade is A"


grades()