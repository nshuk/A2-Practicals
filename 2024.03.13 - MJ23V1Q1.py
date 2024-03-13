DataArray = [0 for i in range(25)]
# DataArray : ARRAY [0:24] OF INTEGER

count = 0
try:
    file = open("C:/9618/Mar13/Data.txt", "r")
    line = file.readline()
    while line != "":
        DataArray[count] = int(line)
        count = count + 1
        line = file.readline()
    file.close()
except IOError:
    print("File not found")

def PrintArray(array):
    for i in range(25):
        print(array[i], " ", end="")

PrintArray(DataArray)

def LinearSearch(array, searchValue):
    numbersFound = 0
    for i in range(25):
        if array[i] == searchValue:
            numbersFound = numbersFound + 1
    return numbersFound

print(" ")
num = int(input("Enter a whole number between 0 and 100 inclusive: "))
if (num<0) or (num>100):
    print("Invalid input. Between 0 and 100 inclusive only.")
else:
    numbersFound = LinearSearch(DataArray, num)
    print("The number", num, "is found",numbersFound, "times." )


