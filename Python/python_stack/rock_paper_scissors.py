from random import randint

def compChoose():
    randType = randint(0,2)
    if randType == 0:
        handType = "rock"
    elif randType == 1:
        handType = "paper"
    else:
        handType = "scissors"
    print handType
    return handType

def checkWinner(computer, user):
    if computer == user:
        print "Tie"
    elif (computer == "rock" and user == "scissors") or (computer == "scissors" and user == "paper") or (computer == "paper" and user == "rock"):
        print "You lose"
    else:
        print "You Win"



def play():
    playing = True
    while playing:
        userChoice = raw_input("Type rock, paper, or scissors to play! Type exit to quit.").lower()
        userChoice = userChoice.split("\r")
        userChoice = userChoice[0]
        if userChoice not in ("rock", "paper", "scissors", "exit"):
            print "Not valid input. Try again."
            continue
        elif userChoice == "exit":
            playing = False
            print "Thank you for playing!"
        compChoice = compChoose()
        checkWinner(compChoice, userChoice)
play()