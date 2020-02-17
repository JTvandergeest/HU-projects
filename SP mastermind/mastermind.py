import random
import math

kleuren = ["blauw", "rood", "geel", "groen", "wit", "zwart"]
teGokkenCode = []
gegokteCode = []

def genereer_code(y,z):
    for i in range(0,4):
        x = random.randint(0,5)
        y.append(z[x])
    return y

def geef_code(y):
    print("Geef een code. De mogelijke kleuren zijn: 'blauw, rood, geel, groen, wit en zwart'. "
          "Kies een code van 4 kleuren met een spatie tussen 2 kleuren. "
          "Gebruik exclusief kleine letters.")
    x = input().split(" ")
    for i in range(len(x)):
        y.append(x[i])
    return y

def speler_gok(y):
    print("De mogelijke kleuren zijn: 'blauw, rood, geel, groen, wit en zwart'. "
          "Doe een gok van 4 kleuren met een spatie tussen 2 kleuren. "
          "Gebruik exclusief kleine letters en spaties tussen de kleuren.")

    for i in range(0,11):
        print("Doe een gok.")
        y = input().split(" ")
        check(y, teGokkenCode)
        print("Jouw gok: ", y)
        print(feedback(y, teGokkenCode))

    print("Helaas, je gokken zijn op. De code was: ", teGokkenCode)

def check(y, x):
    if x == y:
        print("Dat is de juiste code, gefeliciteerd!")
        exit()
    else:
        print("Dat is helaas niet de juiste code.")

def litterally_guessing(y, x):
    for i in range(0, 11):
        for ii in range(0, 4):
            z = random.randint(0, 5)
            y.append(x[z])
        print(y)
        check(y, teGokkenCode)
        feedback(y, teGokkenCode)
        y.clear()
    print("Helaas, dat was de laatste gok. De code was: ", teGokkenCode)


def a_simple_strategy(y, z):
    possibleCombinations = []

    for ii in range(6 ** 4):    #Alle mogelijke codes in een lijst zetten.
        index0 = math.floor(ii / (6 ** 3)) % 6
        index1 = math.floor(ii/ (6 ** 2)) % 6
        index2 = math.floor(ii / 6) % 6
        index3 = ii % 6

        singleCombination = (y[index0] + " " + y[index1] + " " + y[index2] + " " + y[index3]).split(" ")
        possibleCombinations.append([singleCombination])

    for i in range(0, 11):
        if len(possibleCombinations) >= 3:
            z = possibleCombinations[0][0]#random.randint(0, len(possibleCombinations)) <--- Is om de gok willekeurig te maken, gekozen uit de overige mogelijke codes.
        else:
            z = possibleCombinations[0][0]
        print("Computer gok: ", z)
        if z == teGokkenCode:
            print("Dat is de juiste code, gefeliciteerd!")
            exit()
        else:
            print("Dat is helaas niet de juiste code.")

        fb = feedback(z, teGokkenCode).copy()
        print(fb)

        for iii in range(len(possibleCombinations)):
            if feedback(possibleCombinations[iii][0], z) != fb:
                possibleCombinations[iii] = 0

        while 0 in possibleCombinations:
            possibleCombinations.remove(0)

    print("Helaas, dat was de laatste gok. De code was: ", teGokkenCode)

def feedback(y, x):
    blackpin = 0
    whitepin = 0
    gok = y.copy()
    code = x.copy()

    for i in range(len(x)):
        if gok[i] == code[i]:
            blackpin += 1
            code[i] = 0
            gok[i] = 1

    for i2 in range(len(x)):
        if gok[i2] != code[i2] and gok[i2] in code:
            whitepin += 1
            z = code.index(gok[i2])
            code[z] = 0
            gok[i2] = 1

    pinnetjes = [blackpin, whitepin]
    return pinnetjes

def player_or_computer():
    print("Kies. "
          "De speler geeft de code en de computer raad, typ dan 'x'. "
          "De computer geeft de code en de speler raad, typ dan 'y'. ")
    keuze = input()
    if keuze == "x":
        geef_code(teGokkenCode)
        #litterally_guessing(gegokteCode, kleuren) #Strategie van compleet willekeurig gokken, laag slagingspercentage, desalniettemin een strategie.
        #genereer_code(teGokkenCode, kleuren) #(Voor het compleet automatiseren, naast de keuze voor wie welke rol heeft.)
        a_simple_strategy(kleuren, gegokteCode) #Strategie, werkt door middel van het proces van eliminatie door elke mogelijke code te vergelijken met de gok op basis van de feedback op de gok.

    if keuze == "y":
        genereer_code(teGokkenCode, kleuren)
        speler_gok(gegokteCode)

def play_mastermind():
    print("Dit is het spel 'Mastermind'. ")
    player_or_computer()

play_mastermind()






"""def computer_gok(gok):
    possibleFeedback = [[0,0],[0,1],[0,2].[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[3,0],[4,0]]
    possibleAnswers = []
    teller = 0
    noemer = 0 #moet aantal mogelijke cominaties zijn

    for i in possibleAnswers: 
        if x in possibleAnswers and  == possibleFeedback[i]
    #for ai in possibleFeedback:
"""
