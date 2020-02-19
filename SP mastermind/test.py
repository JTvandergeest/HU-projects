import math
import random

def a_simple_strategy2(y, z):
    possibleCombinations = []
    possibleFeedback = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [4, 0]]

    for ii in range(6 ** 4):    #Alle mogelijke codes in een lijst zetten.
        index0 = math.floor(ii / (6 ** 3)) % 6
        index1 = math.floor(ii / (6 ** 2)) % 6
        index2 = math.floor(ii / 6) % 6
        index3 = ii % 6

        singleCombination = (y[index0] + " " + y[index1] + " " + y[index2] + " " + y[index3]).split(" ")
        possibleCombinations.append([singleCombination])

    for i in range(0, 11):
        if len(possibleCombinations) >= 3:
            z = possibleCombinations[0][0]  #random.randint(0, len(possibleCombinations)) <--- Is om de gok willekeurig te maken, gekozen uit de overige mogelijke codes.
        else:
            z = possibleCombinations[0][0]
        print("Computer gok: ", z)

        #check(z, teGokkenCode)

        fb = feedback(z, teGokkenCode).copy()
        print(fb)

        indexPossibleFeedback = possibleFeedback.index(fb)

        for iii in range(len(possibleCombinations)):
            fbPerPosCombi = feedback(possibleCombinations[iii][0], z)
            if fbPerPosCombi != fb:
                possibleCombinations[iii] = 0
            if possibleFeedback.index(fbPerPosCombi) < indexPossibleFeedback:
                possibleFeedback[iii] = 0

        while 0 in possibleCombinations:
            possibleCombinations.remove(0)

    print("Helaas, dat was de laatste gok. De code was: ", teGokkenCode)
