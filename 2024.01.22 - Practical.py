class Image:
    def __init__(self, desc, wid, hei, fc):
        self.__Description = desc
        # __Description : STRING
        self.__Width = wid
        # __Width : INTEGER
        self.__Height = hei
        # __Height : INTEGER
        self.__FrameColour = fc
        # __FrameColour : STRING

    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, desc):
        self.__Description = desc

# declare array of type Image with 50 elements
myImage = [Image(None, None, None, None) for i in range(50)]
numOfImage = 0

def NewImage(myImage, numOfImage): # parameter array and index, return incremented index
    print("Enter the following")
    desc = input("Enter the description: ")
    wid = int(input("Enter the width: "))
    hei = int(input("Enter the height: "))
    fc = input("Enter the frame colour: ")
    myImage.append(Image(desc, wid, hei, fc))
    print("The description, width, height and frame color are as follows")
    print(desc, wid, hei, fc)
    return (numOfImage + 1) # incremented index

numOfImage = NewImage(myImage, numOfImage)

class Picture:
    def __init__(self, desc, wid, hei, fc, pt, pl):
        Image.__init__(self, desc, wid ,hei, fc)
        self.__PictureText = pt  # STRING
        self.__PictureLabel = pl  # STRING
