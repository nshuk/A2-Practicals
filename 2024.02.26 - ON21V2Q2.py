class Picture:
    # __desc : STRING
    # __width : INTEGER
    # __height : INTEGER
    # __frame =: STRING
    def __init__(self,d,w,h,c):
        self.__desc = d
        self.__width = w
        self.__height = h
        self.__color = c
    def getDescription(self):
        return self.__desc
    def getHeight(self):
        return self.__height
    def getWidth(self):
        return self.__width
    def getColor(self):
        return self.__color
    def setDescription(self,newDesc):
        self.__desc = newDesc

pictureArray = [Picture("",0,0,"") for i in range (100)]
# pictureArray : ARRAY[0:99] of Picture

def ReadData():
    global pictureArray
    count = 0
    try:
        file = open("C:/9618/Feb26/Pictures.txt", "r")
        d = file.readline().strip()
        while d != "":
            w = int(file.readline().strip())
            h = int(file.readline().strip())
            c = file.readline().strip()
            pictureArray[count] = Picture(d, w, h, c)
            count = count + 1
            d = file.readline().strip()
        file.close()
    except IOError:
        print("File not found")
    return count


numOfPic = ReadData()
print(numOfPic)

color = input("Enter frame color: ").lower().strip() # use of .lower() tu LCASE the entire string. .strip() to remove whitespace
maxWidth = int(input("Enter max width: "))
maxHeight = int(input("Enter max height: "))
print("Here are the ones found:")

for i in range(numOfPic):
    if pictureArray[i].getColor().lower() == color:
        if pictureArray[i].getWidth() <= maxWidth:
            if pictureArray[i].getHeight() <= maxHeight:
                print(pictureArray[i].getDescription())
                print(pictureArray[i].getWidth())
                print(pictureArray[i].getHeight())


# use of strip() to remove the /n and also whitespace
# use of lower() to LCASE the entire string
# may use upper() instead
# OOP assigned into array, cant be printed and displayed directly. instead, use get methods to print them out
# at the read data, you have to open file and read the first line (text1) first before try:
# the include condition where the successive text1 is not empty.
# if empty, the already reached EOF. otherwise, keep on reading
# hence why text1 appears for a second time down there

