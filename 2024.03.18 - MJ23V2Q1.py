Animals = ["" for i in range(10)]
# Animals : ARRAY [0:9] OF STRING

Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

def SortDescending():
    arrayLength = len(Animals)
    for x in range(0, arrayLength - 1):
        for y in range(0, arrayLength - x - 1):
            if Animals[y][0:1] < Animals[y+1][0:1]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp

SortDescending()

for i in range(10):
    print(Animals[i])

# use of mid function to slice out the selected characters from the function
# string[0:1] means slice out the str starting with index 0 with length 1
