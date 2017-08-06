import math
from random import randint

class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck(object):

    def __init__(self, cards = []):
        self.cards = cards

    def createDeck(self):
        for suit in suits:
            for number in range(1, 14):
                card = Card(suit, number)
                self.cards.append(card)

        return self

    def printDeck(self):
        for i in range(len(self.cards)):
            print self.cards[i].suit, self.cards[i].number
        return self

    def hit(self):
        card = self.cards.pop()
        return card

    def deal(self):
        cards = []
        cards.append(self.cards.pop())
        cards.append(self.cards.pop())
        return cards

    def shuffle(self):
        n = len(self.cards) - 1
        for count in range(0, len(self.cards)):
            i = randint(0, n)
            temp = self.cards[i]
            self.cards[i] = self.cards[n]
            self.cards[n] = temp
            n -= 1

class Hand(object):

    def __init__(self, cards = []):
        self.cards = cards

    def checkSum(self):
        handSum = 0
        for card in self.cards:
            if card.number >= 11:
                handSum += 10
            elif handSum <= 10 and card.number == 1:
                handSum += 11
            else:
                handSum += card.number
        return str(handSum)

    def add(self, card):
        self.cards.append(card)
        return self


suits = ["heart", "spade", "clover", "diamond"]

def numberHands(deck, number):
    playerList = []
    for count in range(0, number + 1):
        playerList.append(Hand(deck.deal()))
    return playerList

def checkWinner(playerList):
    if int(playerList[0].checkSum()) > 21:
        print "Everyone wins!"
        return None
    for i in range(1,len(playerList)):
        if int(playerList[i].checkSum()) == 21 and len(playerList[i].cards) == 2:
            print "Player", i, "got BLACKJACK!"
        if int(playerList[i].checkSum()) > int(playerList[0].checkSum()) and int(playerList[i].checkSum()) <= 21:
            print "Player", i, "is a winner!"
        else:
            print "Player", i, "is a loser!"

def play():
    # Creates deck
    deck = Deck()
    deck.createDeck()
    deck.shuffle()

    players = int(raw_input("How many people will play?"))

    playerList = numberHands(deck, players)

    # Prompts user for action
    count = 0
    for player in playerList:
        if count == 0:
            print "Dealer your total is", player.checkSum()
        else:
            print "Player", count, "your total is", player.checkSum()
        count += 1
        choice = ""
        for i in range(0, len(player.cards)):
            print "Your cards are", player.cards[i].suit, player.cards[i].number
        while choice != "pass":
            choice = raw_input("Type hit or pass ")
            choice = choice.split("\r")
            choice = choice[0]
            if (choice == "hit" and int(player.checkSum()) < 21):
                player.add(deck.hit())
                print "New total:", player.checkSum()
                for i in range(0, len(player.cards)):
                    print "Your cards are", player.cards[i].suit, player.cards[i].number
            if int(player.checkSum()) > 21:
                print "You busted!"
                choice = "pass"
    checkWinner(playerList)
play()

# deck = Deck()
# deck.createDeck()
# deck.shuffle()
# print deck.printDeck()