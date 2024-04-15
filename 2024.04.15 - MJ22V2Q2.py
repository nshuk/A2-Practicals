# use of random library. we learned this back in AS

# ArrayData : ARRAY [0:9, 0:9] OF INTEGER
import random
ArrayData = [[random.randint(1,100) for i in range(10)] for j in range(10)]


def OutputArray():
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], end=" ")
        print(" ")



# skip to line 23, as this part is only to be used for (c)(ii)
# i want to input my own values in teh first row, since i need to know what values are and arent in there for (c)(ii)
# input any number including 1. also, any number except 11. see (c)(ii)
for i in range(10):
    ArrayData[0][i] = int(input("Enter integer: "))


print("The array before sorting:")
OutputArray()
print("")

ArrayLength = 10
for x in range(0, ArrayLength):
    for y in range (0, ArrayLength-1):
        for z in range(0, ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue

print("The array after sorting:")
OutputArray()



# Use these values
# SearchArray = ArrayData
# Lower = 0
# Upper = 9

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = int((Lower+Upper) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        elif SearchArray[0][Mid] < SearchValue:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1

# (c)(ii)
print(BinarySearch(ArrayData, 0, 9, 1)) # 1 is present in the first row
print(BinarySearch(ArrayData, 0, 9, 11)) # 11 is not present in the first row

