def Unknown(x,y):
    if x < y:
        print(x+y)
        return (Unknown(x+1,y) * 2)
    elif x == y:
        return 1
    else:
        print(x+y)
        return (int(Unknown(x-1,y) / 2))

value1 = 10
value2 = 15

print("For x =", value1, "and y=", value2)
print(str(Unknown(value1, value2)))
print("For x =", value1, "and y=", value1)
print(str(Unknown(value1, value1)))
print("For x =", value2, "and y=", value1)
print(str(Unknown(value2, value1)))

def IterativeUnknown(x,y):
    result = 1
    if x == y:
        return result
    elif x < y:
        while x != y:
            print(x+y)
            x = x + 1
            result = result * 2
        return result
    else:
        while x != y:
            print(x+y)
            x = x - 1
            result = int(result / 2)
        return result

print("For x =", value1, "and y=", value2)
print(str(IterativeUnknown(value1, value2)))
print("For x =", value1, "and y=", value1)
print(str(IterativeUnknown(value1, value1)))
print("For x =", value2, "and y=", value1)
print(str(IterativeUnknown(value2, value1)))

# have no actual idea what these are practically used for
# wasted most of my time thinking about the logic behind it but it seemed irrelevant in the end