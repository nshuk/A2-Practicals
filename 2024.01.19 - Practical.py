class HiddenBox:
    def __init__(self, bn, c, dh, gl):
        self.__BoxName = bn  # String
        self.__Creator = c  # String
        self.__DateHidden = dh  # Date
        self.__GameLocation = gl  # String
        self.__LastFinds = ["" for i in range(10)]  # 2D Array of String
        self.__Active = False  # Boolean

    def GetBoxName(self, bn):
        self.__BoxName = bn

    def GetGameLocation(self, gl):
        self.__GameLocation = gl

TheBoxes = []  # 1D Array of HiddenBox [0:9999]
index = 0
import datetime
def NewBox(): # take bn,c,dh,gl as input, not parameter
    global index
    print("Please input the following")
    bn = input("Box Name: ")
    c = input("Creator: ")
    y = int(input("Date Hidden Year: "))
    m = int(input("Date Hidden Month: "))
    d = int(input("Date Hidden Day: "))
    dh = datetime.date(y, m, d)
    gl = input("Game Location: ")
    myBox = HiddenBox(bn, c, dh,  gl)
    TheBoxes.append(myBox)
    index = index + 1

NewBox()

class PuzzleBox:
    def __init__(self, bn, c, dh, gl, pt, s):
        HiddenBox.__init__(self, bn, c, dh, gl)
        self.__PuzzleText = pt  # String
        self.__Solution = s  # String





