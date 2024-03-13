Animal = [" " for i in range(20)] # ARRAY [0:19] OF STRING
Colour = [" " for j in range(10)] # ARRAY [0:9] OF STRING
AnimalTopPointer = 0 # INTEGER
ColourTopPointer = 0 # INTEGER

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return " "
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

def ReadData():
    try:
        file = open("C:/9618/Mar13/AnimalData.txt", "r")
        line = file.readline().strip()
        while line != "":
            PushAnimal(line)
            line = file.readline().strip()
        file.close()
    except IOError:
        print("File not found")

def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return " "
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

# now they want us to ammend ReadData() to also read file color.
# here, im just denoting it as ReadData2() to show the difference
# in the evidence file, you should actually ammend the already written ReadData() instead
def ReadData2():
    try:
        fileA = open("C:/9618/Mar13/AnimalData.txt", "r")
        fileC = open("C:/9618/Mar13/ColourData.txt", "r")
        lineA = fileA.readline().strip()
        lineC = fileC.readline().strip()
        while lineA != "":
            PushAnimal(lineA)
            lineA = fileA.readline().strip()
        while lineC != "":
            PushColour(lineC)
            lineC = fileC.readline().strip()
        fileA.close()
        fileC.close()
    except IOError:
        print("File not found")

def OutputItem():
    poppedA = PopAnimal()
    poppedC = PopColour()
    if (poppedA != " ") and (poppedC != " "):
        print(poppedC, poppedA)
    elif poppedC == " ":
        PushAnimal(poppedA)
        print("No colour")
    elif poppedA == " ":
        PushColour(poppedC)
        print("No animal")

ReadData2()
for i in range(4):
    OutputItem()