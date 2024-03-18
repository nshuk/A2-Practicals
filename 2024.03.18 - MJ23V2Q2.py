class SaleData:
    def __init__(self, id, quan):
        # __ID : STRING
        # __Quantity : INTEGER
        self.__ID = id
        self.__Quantity = quan
    def GetDetails(self):
        print(self.__ID, self.__Quantity)

# CircularQueue : ARRAY [0:5] OF SaleData
# Head : INTEGER
# Tail : INTEGER
# NumberOfItems : INTEGER
CircularQueue = [SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(newRecord):
    global Tail, NumberOfItems
    if NumberOfItems < len(CircularQueue): # if not full
        NumberOfItems = NumberOfItems + 1 # update current amount
        CircularQueue[Tail] = newRecord # enqueue
        if Tail < len(CircularQueue) - 1: # if tail haven't reach end of queue
            Tail = Tail + 1 # increment normally
        else:
            Tail = 0 # loop back to front
        return 1
    else:
        return -1

def Dequeue():
    global Head, NumberOfItems
    if NumberOfItems == 0 : # if empty
        return SaleData("", -1) # return empty record
    else:
        NumberOfItems = NumberOfItems - 1 # update current amount
        DequeuedRecord = CircularQueue[Head] # dequeue
        if Head < len(CircularQueue) - 1:
            Head = Head + 1
        else:
            Head = 0
        return DequeuedRecord

def EnterRecord():
    inputID = input("Please enter item ID: ")
    inputQuantity = int(input("Please enter the quantity: "))
    inputRecord = SaleData(inputID, inputQuantity)
    resultFlag = Enqueue(inputRecord)
    if resultFlag == -1 :
        print("Full")
    else:
        print("Stored")

for i in range(6):
    EnterRecord()
result = Dequeue()
if result == SaleData("", -1):
    print("Error circular queue empty")
else:
    result.GetDetails()
EnterRecord()
for i in range (5):
    CircularQueue[i].GetDetails()


# we len(CircularQueue) - 1 cuz len counts the amount of items in there, yielding 10.
# what we need is the last index, 9. hence the minus one
# question asked for record structure. didnt mention what datatype specifically
# so i used OOP for convenience
