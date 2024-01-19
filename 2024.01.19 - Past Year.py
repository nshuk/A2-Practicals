class NodeClass:
    def __init__(self):
        self.__Data = ""  # String
        self.__Pointer = -1  # Integer
    def SetData(self, d):
        self.__Data = d
    def SetPointer(self, p):
        self.__Pointer = p
    def GetData(self):
        return self.__Data
    def GetPointer(self):
        return self.__Pointer

class QueueClass:
    def __init__(self):
        self.__Queue = []   # 1D Array of NodeClass
        self.__Head = -1  # Integer
        self.__Tail = -1  # Integer

    def JoinQueue(self, newItem):  # newItem is in datatype NodeClass
        Node = NodeClass()  # instantation of an object of nodeclass
        Node.__Data = newItem  # paramaters passed to property Data of the object
        self.__Queue.append(Node)


