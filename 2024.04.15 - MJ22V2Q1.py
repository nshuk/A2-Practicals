# StackData : ARRAY [0:9] OF INTEGER
# StackPointer : INTEGER

StackData = [0 for i in range(10)]
StackPointer = 0 #next available space

def OutputStack():
    global StackPointer
    x = StackPointer - 1
    print("The elements in the stack are:")
    for i in range(x):
        print(StackData[i])
    print("The StackPointer points at:", StackPointer)

def Push(newValue):
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = newValue
        StackPointer = StackPointer + 1
        return True

for i in range(11):
    newValue = int(input("Please enter an integer: "))
    successFlag = Push(newValue)
    if successFlag == True:
        print("The number", newValue, "is successfully added to stack")
    else:
        print("Stack full. The number", newValue, "is not added to stack")

OutputStack()

def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        PoppedValue = StackData[StackPointer]
        return PoppedValue

for i in range(2):
    PoppedValue = Pop()

OutputStack()