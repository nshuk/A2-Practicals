class Vehicle:
    def __init__(self, ID, MS, IA):
        # __ID : STRING
        # __MaxSpeed : INTEGER
        # __CurrentSpeed : INTEGER
        # __IncreaseAmount : INTEGER
        # __HorizontalPosition : INTEGER
        self.__ID = ID
        self.__MaxSpeed = MS
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IA
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CS):
        self.__CurrentSpeed = CS

    def SetHorizontalPosition(self, HP):
        self.__HorizontalPosition = HP

    def IncreaseSpeed(self):
        newSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if (newSpeed <= self.__MaxSpeed): # if newval has yet to exceed maximum possible val
            self.__CurrentSpeed = newSpeed # them use that val
        else:
            self.__CurrentSpeed = self.__MaxSpeed # otherwise use the maximum possible val

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def OutputDetails(self):
        print("The horizontal position of the vehicle is:", self.GetHorizontalPosition())
        print("The current speed of the vehicle is:", self.GetCurrentSpeed())


class Helicopter(Vehicle):
    def __init__(self, ID, MS, IA, VC, MH): # dont forget to include inherited para alongside new para
        # __VerticalPosition : INTEGER
        # __VerticalChange : INTEGER
        # __MaxHeight : INTEGER
        Vehicle.__init__(self, ID, MS, IA) # inherited
        self.__VerticalPosition = 0
        self.__VerticalChange = VC
        self.__MaxHeight = MH

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # right now we are trying to override, where an attribute from super is used as part of the sub's redefined method
    # you may just use self to call attributes of sub, but you cant use self to call attributes of super
    # you can't just copy and paste the super's code and put it inside the sub's because the self does not work the same way
    # therefore we override using super's setters and getters. ALWAYS REMEMBER to put self as the para

    def IncreaseSpeed(self):
        newVerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if (newVerticalPosition <= self.__MaxHeight): # if it has yet to exceed max height
            self.__VerticalPosition = newVerticalPosition # use that value
        else:
            self.__VerticalPosition = self.__MaxHeight # otherwise use max height

        newSpeed = Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self) # override (getter)
        maxSpeed = Vehicle.GetMaxSpeed(self)
        if (newSpeed <= maxSpeed):
            Vehicle.SetCurrentSpeed(self, newSpeed) # override (setter)
        else:
            Vehicle.SetCurrentSpeed(self, maxSpeed)

        newHorPos = Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self)
        Vehicle.SetHorizontalPosition(self, newHorPos)

    def OutputDetails(self):
        print("The horizontal position of the vehicle is:", Vehicle.GetHorizontalPosition(self)) # override
        print("The current speed of the vehicle is:", Vehicle.GetCurrentSpeed(self)) # override
        print("The vertical position of the vehicle is:", self.GetVerticalPosition()) # no need of override


car1 = Vehicle("Tiger", 100, 20)
heli1 = Helicopter("Lion", 350, 40, 3, 100)
car1.IncreaseSpeed()
car1.IncreaseSpeed()
car1.OutputDetails()

heli1.IncreaseSpeed()
heli1.IncreaseSpeed()
heli1.OutputDetails()


# beware. the question mentioned that a procedure is needed to output the details. they never said to do it on the main program
# never said it was a method within the class either
# tried to use main program. impossible cuz we're working on two different objects
# mark scheme used methods. on method for reach class. the sub's method has to use override
