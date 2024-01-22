#__BoxName  String
#__Creator  String
#__DateHidden  Date
#__GameLocation  String
#__LastFinds  2D Array of String
#__Active Boolean


class HiddenBox:
    def __init__(self, bn, c, dh, gl):
        self.__BoxName = bn  # String
        self.__Creator = c  # String
        self.__DateHidden = dh  # Date
        self.__GameLocation = gl  # String
        self.__LastFinds = ["" for i in range(10)]  # 2D Array of String
        self.__Active = False  # Boolean

    def GetBoxName(self, bn):
        return self.__BoxName

    def GetGameLocation(self, gl):
        return self.__GameLocation

TheBoxes = [HiddenBox("", "", None, "") for i in range(10000)]  # 1D Array of HiddenBox [0:9999]
index = 0
import datetime
def NewBox(TheBoxes, index): # take array and index as parameter, return final index
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
    return (index+1) # increment index

index = NewBox(TheBoxes, index)

class PuzzleBox:
    def __init__(self, bn, c, dh, gl, pt, s):
        HiddenBox.__init__(self, bn, c, dh, gl)
        self.__PuzzleText = pt  # String
        self.__Solution = s  # String





