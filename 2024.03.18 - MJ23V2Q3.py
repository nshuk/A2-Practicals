class Employee:
    def __init__(self, hp, en, jt):
        # __HourlyPay : REAL
        # __EmployeeNumber : STRING
        # __JobTitle : STRING
        # __PayYear2022 :ARRAY[0:51] OF REAL
        self.__HourlyPay = hp
        self.__EmployeeNumber = en
        self.__JobTitle = jt
        self.__PayYear2022 = [0.0 for i in range(52)]

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, weeknum, hours):
        pay = self.__HourlyPay * hours
        self.__PayYear2022[weeknum] = pay

    def GetTotalPay(self):
        runningTotal = 0
        for i in range(52):
            runningTotal = runningTotal + self.__PayYear2022[i]
        return runningTotal

class Manager(Employee):
    def __init__(self, hp, en, jt, bv):
        # __BonusValue : REAL
        Employee.__init__(self, hp, en, jt)
        self.__BonusValue = bv

    def SetPay(self, weeknum, hours):
        bonusHours = hours * (1 + (self.__BonusValue / 100))
        Employee.SetPay(self, weeknum, bonusHours)


EmployeeArray = [Employee(0.0, "", "") for i in range(8)]
x = 0
try:
    file = open("C:/9618/Mar18/Employees.txt", "r")
    line1 = file.readline().strip()
    while line1 != "":
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        if ord(line3[0:1]) >= 48 and ord(line3[0:1]) <= 57: # if the char ascii value is numerical
            line4 = file.readline().strip() # keep reading the next line
            EmployeeArray[x] = Manager(float(line1), str(line2), str(line4), float(line3))
            x = x + 1
        else:
            EmployeeArray[x] = Employee(float(line1), str(line2), str(line3))
            x = x + 1
        line1 = file.readline().strip()
    file.close()
except IOError:
    print("File not found")

def EnterHours():
    try:
        file = open("C:/9618/Mar18/HoursWeek1.txt", "r")
        line1 = file.readline().strip()
        while line1 != "":
            line2 = file.readline().strip()
            for i in range(8):
                if line1 == EmployeeArray[i].GetEmployeeNumber():
                    location = i
                    EmployeeArray[location].SetPay(1, float(line2))
            line1 = file.readline().strip()
        file.close()
    except IOError:
        print("File not found")

EnterHours()
for i in range(8):
    print("Employee Number:", EmployeeArray[i].GetEmployeeNumber())
    print("Total Pay:", EmployeeArray[i].GetTotalPay())



# for the polymorphism part, they wanted us to update the hours by taking into account the percentage increment
# this is done under Manager's SetPay
# then, the new hours is used as the parameter for the Employee's SetPay
# they specifically said to call SetPay from the parent class (override)

# it's better to read the lines as is and leave in str first.
# after that, during instantation or assignment, only then you convert datatype

# even tho i set EmployeeArray datatype as Employee, I can actually still can instantatiate Manager inside
# i suppose child class would also be categorized under the same datatype as their parent

# during reading file, they wanted us to validate whether the string read is a realnum or string
# since we cant use isinstance as all the lines are originally string, i had to use their ascii values
# the first char of the line, (hence [0:1]), if it's a real num, it'll have ascii between 48 and 57
# otherwise, it's a symbol or alphabets.

