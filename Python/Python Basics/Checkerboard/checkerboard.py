
def checkerboard(height):
    for count in range(0, height):
        if (count % 2 == 0):
            print ("* * * *")
        else:
            print (" * * * *")

checkerboard(10)