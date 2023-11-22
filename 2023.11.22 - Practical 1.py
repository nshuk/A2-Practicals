animalList = [" " for i in range (10)] # array[0:1] of string

animalList = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]
print("The array initially: ")
print(animalList)

def SortDescending():
    arrayLength = len(animalList)
    for x in range(0, arrayLength - 1):
        for y in range(0, (arrayLength - x - 1)):
            if ord((animalList[y])[0:1]) < ord((animalList[y+1])[0:1]):
                temp = animalList[y]
                animalList[y] = animalList[y+1]
                animalList[y+1] = temp

SortDescending()
print("The array after sorting descendingly: ")
for i in range (10):
    print(animalList[i])

# instructions
# 1. declare array of string for 10 items to be stored
# 2. put in those animals in order (they never said anything about getting input from user).
# ensure they are all lower case
# therese a reason why they want you to make sure it's lowercase. you'll see
# 3. write a sorting algo where it will sort alphabetically descending
# must use mid to slice a char from string, turn it into ascii using ord the compare with item in the next slot
# if smaller, swap
# 4. screenshot output. print the names of each animal on a new line each