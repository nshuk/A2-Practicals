ArrayNodes=[[0 for i in range(3)] for j in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the new value: "))
    if FreeNode <= 19:  # if not empty
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData # assign to parent node
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1: # if the array is initially empty
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]: # left child node
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else: # right child node
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Trees is full")

def PrintAll():
    global ArrayNodes
    for i in range(20):
        print(ArrayNodes[i][0], " ", ArrayNodes[i][1], " ", ArrayNodes[i][2])

for i in range(10):
    AddNode()

PrintAll()

def InOrder(RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes[RootNode][0])
    print(ArrayNodes[RootNode][1])
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes[RootNode][2])

InOrder(0)