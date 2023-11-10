# declaration of array, headpointer, tailpointer, and number of item

emptyString = " "
queueArray =[emptyString for i in range (10)] # this will create empty array from index 0 to 9
headP = 0
tailP = 0
numofItems = 0

print("Here's the queue initially:")
print(queueArray)
print(emptyString)

# now write a enqueue and dequeue function. for both, return true is succesful
# else, for enqueue return false, dequeue return the false

def Enqueue(dataToAdd):
    global tailP, numofItems
    if numofItems == len(queueArray):
        return False
    queueArray[tailP] = dataToAdd
    if tailP >= 9: #because 9 is the last index
        tailP = 0
    else:
        tailP = tailP +1
    numofItems = numofItems + 1
    return True

def Dequeue():
    global headP, numofItems
    if numofItems == 0:
        return False
    queueArray[headP] = emptyString
    if headP >= 9:
        headP = 0
    else:
        headP = headP + 1
    numofItems = numofItems - 1
    return False

# here's the instruction. enqueue 11 string values, dequeue 2 values
# next is to initialize the queue back empty
# then queue the characters A B C D E F G H I J K

for i in range (11):
    testString = "test" + str(i)
    resultFlag = Enqueue(testString)
    if resultFlag == False:
        print("Failed, Queue is full")
        print(emptyString)
    else:
        print("Successful, Here's the queue after enqueue:")
        print(queueArray)
        print(emptyString)

for i in range (2):
    resultFlag = Dequeue()
    if resultFlag == False:
        print("Failed, Queue is empty")
        print(emptyString)
    else:
        print("Successful, Here's the queue after dequeue:")
        print(queueArray)
        print(emptyString)

for i in range (8):
    resultFlag = Dequeue()
    if resultFlag == False:
        print("Failed, Queue is empty")
        print(emptyString)
    else:
        print("Successful, Here's the queue after dequeue:")
        print(queueArray)
        print(emptyString)

for i in range (65, 76): # capital A ascii starts with 65.
    character = chr(i) # use of chr to turn ascii into char
    resultFlag = Enqueue(character)
    if resultFlag == False:
        print("Failed, Queue is full")
        print(emptyString)
    else:
        print("Successful, Here's the queue after enqueue:")
        print(queueArray)
        print(emptyString)
