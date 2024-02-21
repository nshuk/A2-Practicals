# global nameArray : ARRAY[0:10] OF STRING
# global markArray : ARRAY[0:10] OF INTEGER
nameArray = ["" for i in range(11)]
markArray = [0 for i in range(11)]

def ReadStudentMarks():
    global nameArray
    global markArray
    try:
       file = open("C:/9618/Feb21/StudentMark.txt", "r")
       for i in range(10):
           nameText = file.readline().strip()
           markText = int(file.readline())
           nameArray[i] = nameText
           markArray[i] = markText
    except IOError:
        print("File can not be found")

# correction: did for i in range 11 even tho only 10 datas in there
# didnt do strip so \n is left inside array
# open file below for i in range thus only read the first data cuz it kept reopening

def OutputStudentMarks():
    global nameArray
    global markArray
    for i in range(11):
        if nameArray[i] != "":
            print(nameArray[i], "", markArray[i])

studentName = input("Please enter a 4-character name: ")
while (len(studentName) != 4):
    studentName = input("Invalid input. Enter name that is 4 characters long: ")

studentMark = int(input("Please enter their mark: "))
while (studentMark < 1) or (studentMark>100):
    studentMark = input("Invalid input. Enter mark in between 1 and 100 inclusive: ")

def insertData(name, mark):
    global nameArray
    global markArray
    nameArray[10] = name
    markArray[10] = mark
    lowerBound = 0
    upperBound = 10
    n = upperBound - 1
    flag = False
    while (flag == False) or (n >= lowerBound):
        for i in range(lowerBound, n+1):
            if markArray[i] < markArray[i + 1]:
                # swapping marks
                temp1 = markArray[i]
                markArray[i] = markArray[i+1]
                markArray[i+1] = temp1
                # swapping names
                temp2 = nameArray[i]
                nameArray[i] = nameArray[i + 1]
                nameArray[i + 1] = temp2
                flag = True
        n = n - 1



ReadStudentMarks()
OutputStudentMarks()

print("Here is the content before inserting new student")
print(nameArray)
print(markArray)
insertData(studentName, studentMark)
print("Here is the content after new student")
print(nameArray)
print(markArray)

def WriteTopStudent():
    global nameArray
    global markArray
    file = open("C:/9618/Feb21/NewStudentMark.txt", "w")
    for i in range(10):
        nameText = nameArray[i]
        markText = str(markArray[i])
        file.write(nameText)
        file.write("\n")
        file.write(markText)
        file.write("\n")

WriteTopStudent()






