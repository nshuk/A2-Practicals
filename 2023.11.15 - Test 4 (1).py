MyList = [15,2,3,6,11,89,7,35,4] # declare array [0:8] of integer
lowerBound = 0
upperBound = len(MyList) -1

def InsertionSort(array):
    FirstElement = 1
    for Count in range (FirstElement,len(array)):
        DataToInsert = MyList[Count]
        Inserted = 0
        NextValue = Count - 1
        while (NextValue >= 0) and (Inserted != 1):
            if (DataToInsert < MyList[NextValue]):
                temp = MyList[NextValue+1]
                MyList[NextValue + 1] = MyList[NextValue]
                MyList[NextValue] = temp
                NextValue = NextValue - 1
            else:
                Inserted = 1

def OutputArray(array):
    for x in range (0,len(array)):
        print(array[x])

print("Here are the outputs before sorting: ")
OutputArray(MyList)

InsertionSort(MyList)

print("Here are the outputs after sorting:")
OutputArray(MyList)

def Search(searchitem):
    lowerBound=0
    upperBound = len(MyList) -1
    found = False
    while (found == False) and (lowerBound != upperBound):
        index = int((lowerBound+upperBound)/2)
        if searchitem == MyList[index] :
            print("item found")
            found = True
            return True
        else:
            if searchitem < MyList[index]:
                upperBound = index - 1
            else:
                lowerBound = index + 1
    print("Item not found")
    return False

Search(35)
Search(9)