class Card:
    def __init__(self, n, c):
        # __Number : INTEGER
        # __Colour : STRING
        self.__Number = n
        self.__Colour = c

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

Card1R = Card(1, "red")
Card2R = Card(2, "red")
Card3R = Card(3, "red")
Card4R = Card(4, "red")
Card5R = Card(5, "red")
Card1B = Card(1, "blue")
Card2B = Card(2, "blue")
Card3B = Card(3, "blue")
Card4B = Card(4, "blue")
Card5B = Card(5, "blue")
Card1Y = Card(1, "yellow")
Card2Y = Card(2, "yellow")
Card3Y = Card(3, "yellow")
Card4Y = Card(4, "yellow")
Card5Y = Card(5, "yellow")

class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        # __Cards : ARRAY[0:9] OF Card
        # __FirstCard : INTEGER
        #__NumberCards : INTEGER
        self.__Cards = [c1, c2, c3, c4, c5]
        self.__FirstCard = 0
        self.__NumberCards = 5
    def GetCard(self, index):
        return self.__Cards[index]

Player1 = Hand(Card1R, Card2R, Card3R, Card4R, Card1Y)
Player2 = Hand(Card2Y, Card3Y, Card4Y, Card5Y, Card1B)

def CalculateValue(player):
    score = 0
    for i in range(5):
        myCard = player.GetCard(i)
        if myCard.GetColour() == "red":
            score = score + 5
        elif myCard.GetColour() == "blue":
            score = score + 10
        elif myCard.GetColour() == "yellow":
            score = score + 15
        score = score + myCard.GetNumber()
    return score

scorePlayer1 = CalculateValue(Player1)
scorePlayer2 = CalculateValue(Player2)
if scorePlayer1 > scorePlayer2:
    print("Player 1 with the score", scorePlayer1, "wins against Player 2 with the score", scorePlayer2)
elif scorePlayer2 > scorePlayer1:
    print("Player 2 with the score", scorePlayer2, "wins against Player 1 with the score", scorePlayer1)
else:
    print("Game is draw with both scoring", scorePlayer1)

