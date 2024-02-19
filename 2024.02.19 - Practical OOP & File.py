# 9618 paper 4 mj 2021 variant 1 question 3

class TreasureChest:
    # __question : STRING
    # __answer : INTEGER
    # __points : INTEGER
    def __init__(self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, answerAttempt):
        if answerAttempt == self.__answer:
            return True
        else:
            return False
    def getPoints(self, numOfAttempt):
        if numOfAttempt == 1:
            return self.__points
        elif numOfAttempt == 2:
            return int(self.__points / 2)
        elif (numOfAttempt == 3) or (numOfAttempts == 4):
            return int(self.__points / 4)
        else:
            return 0

# now they want us to read the file where for every three lines there are question, answer, and points on each
# therefore file.readline() three times in the correct order
# and there are also 5 datas in the file
# therefore in range (5)
# and they want us to append each object to the array
# and they want us to use exception handling method with appropriate message ouput

arrayTreasure = []

def readData():
    global arrayTreasure
    try:
        file = open("C:/9618/Feb19/TreasureChestData.txt", "r")
        for i in range(5):
            q = file.readline()
            a = int(file.readline())
            p = int(file.readline())
            arrayTreasure.append(TreasureChest(q,a,p))
        file.close()
    except IOError:
        print("File doesn't exist")

# stuck for a moment cuz i didnt int a and p since a and p when read is string
# on further coding, we want to compare and int with the a and p so a and p must be integer
# remember that from the very beginning we have declared a and p as integer while q string

# main program
readData()
print("There are 5 questions. Please enter number between 1 and 5 inclusive")
questionNum = int(input("Question Number: "))
i = questionNum - 1  # because index arrays starts at 0 and ends at 4
trueFlag = False
numOfAttempts = 0

while trueFlag == False:
    print("The question is", arrayTreasure[i].getQuestion())
    answerAttempt = int(input("Enter your answer: "))
    trueFlag = arrayTreasure[i].checkAnswer(answerAttempt)
    print(trueFlag)
    numOfAttempts = numOfAttempts + 1

pointsReceived = arrayTreasure[i].getPoints(numOfAttempts)
print("The points you received are", pointsReceived)





