# this is very crucial. we rarely ever work with 2D arrays. here's how you play around with them
# look at the question's pseudocode 2d array and python's 2d list. best to not get confused

ArrayNode = [[-1, -1, -1] for i in range(20)]
# ArrayNode : ARRAY[0:19, 0:2] OF INTEGER

# rows, cols = (20,3)
# 2DArray = [[item]*cols]*rows

print(ArrayNode)

#[0][1] means index 0's data. [0][0] means index 0's left pointer. [0][2] means index 0's right pointer

FreeNode = 6
RootPointer = 0

ArrayNode[0][0] = 1
ArrayNode[0][1] = 20
ArrayNode[0][2] = 5
# this is how you input in different lines
ArrayNode[1][0], ArrayNode[1][1], ArrayNode[1][2] = (2, 15, -1)
ArrayNode[2][0], ArrayNode[2][1], ArrayNode[2][2] = (-1, 3, 3)
ArrayNode[3][0], ArrayNode[3][1], ArrayNode[3][2] = (-1, 9, 4)
ArrayNode[4][0], ArrayNode[4][1], ArrayNode[4][2] = (-1, 10, -1)
ArrayNode[5][0], ArrayNode[5][1], ArrayNode[5][2] = (-1, 58, -1)
ArrayNode[6][0], ArrayNode[6][1], ArrayNode[6][2] = (-1, -1, -1)
# this is how you input in the same line

print(ArrayNode)

def SearchValue(Root, ValueToFind): # based on given pseudocode in the question
    if Root == -1:
        return -1
    else:
        if ArrayNode[Root][1] == ValueToFind:
            return Root
        elif ArrayNode[Root][1] == -1:
            return -1
    if ArrayNode[Root][1] > ValueToFind: # if the searchvalue is greater than the current node data
        return SearchValue(ArrayNode[Root][0], ValueToFind) # recursively go down to the right
    if ArrayNode[Root][1] < ValueToFind: # if the searchvalue is less than the current node data
        return SearchValue(ArrayNode[Root][2], ValueToFind) # recursively go down the left

def SearchValue2(Root, ValueToFind): # this one saja nak test. yg ni structure sama dalam github. yang atas tu soalan bagi
    if ValueToFind == ArrayNode[Root][1]:
        return Root
    elif (ArrayNode[Root][1] > ValueToFind) and (ArrayNode[Root][0] != -1): # if the searchvalue is greater than the current node data
        return SearchValue(ArrayNode[Root][0], ValueToFind) # recursively go down to the right
    elif (ArrayNode[Root][1] < ValueToFind) and (ArrayNode[Root][2] != -1): # if the searchvalue is less than the current node data
        return SearchValue(ArrayNode[Root][2], ValueToFind) # recursively go down the left
    else:
        return -1

def PostOrder(Root):
    if ArrayNode[Root][0] != -1: # is not none
        PostOrder(ArrayNode[Root][0]) # recursively go down to the left
    if ArrayNode[Root][2] != -1: # is not none
        PostOrder(ArrayNode[Root][2]) # recursively go down to the right
    print(ArrayNode[Root][1]) # once both pointers are -1, print out the node

index = SearchValue(RootPointer, 15)
if index != -1:
    print("Value is found at index", index)
else:
    print("Value is not found")
PostOrder(RootPointer)

