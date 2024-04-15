class Card:
    # __Number : INTEGER
    # __Colour : STRING
    def __init__(self, n, c):
        self.__Number = n
        self.__Colour = c
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour


CardArray = [Card(0, "") for i in range(30)]

x = 0
try:
    file = open("C:/9618/Apr15/CardValues.txt", "r")
    lineNumber = file.readline().strip()
    while lineNumber != "":
        lineColour = file.readline().strip()
        CardArray[x] = Card(int(lineNumber), lineColour)
        x = x + 1
        lineNumber = file.readline().strip()
except EOFError:
    print("File is not found")


flagArray = [True for i in range(30)] # all cards are initialised as available
def Choosecard():
    global flagArray
    index = int(input("Please enter an integer between 1 and 30 inclusive: "))
    index = index - 1 # python's off by one. index starts at 0, ends at 29.
    if (index<0) or (index>29):
        print("Invalid input. Only enter between 0 and 29")
        return Choosecard() # forgot to put return. MUST PUT otherwise it will return None
    else:
        if flagArray[index] == False : # if card unavailable
            print("Card is unavailable. Choose another one.")
            return Choosecard() # make sure put return
        else:
            print("Card successfully selected.")
            flagArray[index] = False # make the card unavailable
            return index

Player1 = [Card(0, "") for i in range(4)]
for i in range(4):
    index = Choosecard()
    Player1[i] = CardArray[index]
    print("Card selected is:")
    print(Player1[i].GetNumber())
    print(Player1[i].GetColour())

