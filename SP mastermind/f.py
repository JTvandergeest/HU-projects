"""
import math
def a_simple_strategy(y, z):
    possibleCombinations = []
    for i in range(6**4):
        index0 = math.floor(i/(6**3))%6 #floor gives
        index1 = math.floor(i/(6**2))%6
        index2 = math.floor(i/6)%6
        index3 = i%6

        singleCombination = y[index0] + " " + y[index1]+ " " + y[index2] + " " + y[index3]
        possibleCombinations.append([singleCombination])

    check(y, teGokkenCode)
    z = possibleCombinations[0]
    print("Computer gok: ", z)

    print(possibleCombinations)
kleuren = ["blauw", "rood", "geel", "groen", "wit", "zwart"]
"""

l = []
def geef_code(y):
    print("geef code:")
    x = input().split(" ")
    for i in range(len(x)):
        y.append(x[i])
    return y

geef_code(l)
print(l)