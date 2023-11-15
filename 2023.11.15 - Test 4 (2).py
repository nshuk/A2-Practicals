emptyString = " "
QueueData = [emptyString for x in range (20)] # array of string [0:19]
startPointer = -1 # firstelement
endPointer = -1 #lastelement
queueSize = 20

def Enqueue(item):
    global endPointer, queueSize
    if (endPointer < queueSize -1):
        if (endPointer < queueSize -1):
            endPointer = endPointer + 1
        else:
            endPointer = 0
        QueueData[endPointer] = item
        return True
    else:
        return False

