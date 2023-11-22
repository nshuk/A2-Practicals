stackData = [" " for i in range (10)] # declare array [0:1] of integer
stackPointer = 0 # declare stackPointer integer
# our stackPointer is quite unconventional. this one points to the next available space instead
# of top of stack

#output initial stack and pointer
print("The stack initially: ")
print(stackData)
print("The current stackpointer is at index:", stackPointer)

def Push(newItem):
    global stackPointer
    if stackPointer < 10: # must less than 10 cuz 9 is the final index. if sP points to 10, means end of stack
        stackPointer = stackPointer + 1
        stackData[stackPointer-1] = newItem # sp -1 cuz of the same reason
        return True
    else:
        return False

# since they said "allow user to enter" thus must use input()

for i in range(11):
    newItem = int(input("Please enter an integer: "))
    if Push(newItem) == True:
        print("Push successful")
    else:
        print("Push failed. Stack is full")

print("Here's the stack after attempting to add all 11 numbers:")
print(stackData)
print("The current stackpointer is at index:", stackPointer)

# test data with numbers 11 until 20. screenshot

def Pop():
    global stackPointer
    if stackPointer > 0: # sP = 0 means empty stack. it therefore points to the very first index which is 0
        removedItem = stackData[stackPointer-1]
        stackData[stackPointer-1] = " "
        stackPointer = stackPointer - 1
        return removedItem
    else:
        return -1

# finally pop twice then output the content after the inputting the test datas

Pop()
Pop()
print("Here's the stack after popping twice:")
print(stackData)
print("The current stackpointer is at index:", stackPointer)
