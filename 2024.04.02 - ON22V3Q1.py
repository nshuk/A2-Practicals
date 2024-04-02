DataArray = [0 for i in range(100)]
# DataArray : ARRAY [0:99] OF INTEGER

print(DataArray)

def ReadFile():
    x = 0
    try:
        file = open("C:/9618/Apr02/IntegerData.txt", "r")
        item = file.readline().strip()
        while item != "":
            DataArray[x] = int(item)
            x = x + 1
            item = file.readline().strip()
    except EOFError:
        print("File is not found")

def FindValues():
    count = 0
    numInput = int(input("Please enter a number between 1 and 100 inclusive: "))
    if (numInput < 1) or (numInput > 100):
        print("Invalid number entered")
    else:
        for i in range(100):
            if DataArray[i] == numInput:
                count = count + 1
    return count

ReadFile()
print(DataArray)
count = FindValues()
if count == 0:
    print("The number you have entered is not found")
else:
    print("The number you have entered is found", count, "times")

def BubbleSort():
    lowerbound = 0
    upperbound = len(DataArray) - 1
    n = upperbound - 1
    flag = False
    while (flag == False) or (n >= lowerbound):
        for i in range(lowerbound, n + 1):
            if DataArray[i] > DataArray[i + 1]:
                temp = DataArray[i]
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = temp
                flag = True
        n = n - 1
    print(DataArray)

BubbleSort()


