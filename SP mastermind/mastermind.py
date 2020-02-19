import random
import math

kleuren = ["blauw", "rood", "geel", "groen", "wit", "zwart"]
teGokkenCode = []
gegokteCode = []

def genereer_code(code,kleuren):
    for i in range(0, 4):
        randomnr = random.randint(0, 5)
        code.append(kleuren[randomnr])
    return code

def geef_code(y):
    print("Geef een code. De mogelijke kleuren zijn: 'blauw, rood, geel, groen, wit en zwart'. \n"
          "Kies een code van 4 kleuren met een spatie tussen 2 kleuren. \n"
          "Gebruik exclusief kleine letters.")
    x = input().split(" ")
    for i in range(len(x)):
        y.append(x[i])
    return y

def speler_gok(gok):
    print("De mogelijke kleuren zijn: 'blauw, rood, geel, groen, wit en zwart'. \n"
          "Doe een gok van 4 kleuren met een spatie tussen 2 kleuren. \n"
          "Gebruik exclusief kleine letters en spaties tussen de kleuren.")

    for i in range(0,11):
        print("Doe een gok.")
        gok = input().split(" ")
        check(gok, teGokkenCode)
        print("Jouw gok: ", gok)
        print(feedback(gok, teGokkenCode))

    print("Helaas, je gokken zijn op. De code was: ", teGokkenCode)

def check(y, x):
    if x == y:
        print("Dat is de juiste code, gefeliciteerd!")
        exit()
    else:
        print("Dat is helaas niet de juiste code.")

def litterally_guessing_strategy(gok, kleur):
    for i in range(0, 11):
        for ii in range(0, 4):
            z = random.randint(0, 5)
            gok.append(kleur[z])
        print(gok)
        check(gok, teGokkenCode)
        feedback(gok, teGokkenCode)
        gok.clear()
    print("Helaas, dat was de laatste gok. De code was: ", teGokkenCode)

def a_simple_strategy(kleuren, gok): #Bron: "Yet another mastermind strategy"
    possibleCombinations = []

    for ii in range(6 ** 4):    #Alle mogelijke codes in een lijst zetten.
        index0 = math.floor(ii / (6 ** 3)) % 6
        index1 = math.floor(ii / (6 ** 2)) % 6
        index2 = math.floor(ii / 6) % 6
        index3 = ii % 6

        singleCombination = (kleuren[index0] + " " + kleuren[index1] + " " + kleuren[index2] + " " + kleuren[index3]).split(" ")
        possibleCombinations.append([singleCombination])

    for i in range(0, 11):
        gok = possibleCombinations[0][0]
        print("Computer gok: ", gok)

        check(gok, teGokkenCode)

        fb = feedback(gok, teGokkenCode).copy()
        print(fb)

        for iii in range(len(possibleCombinations)):
            if feedback(possibleCombinations[iii][0], gok) != fb:
                possibleCombinations[iii] = 0

        while 0 in possibleCombinations:
            possibleCombinations.remove(0)

    print("Helaas, dat was de laatste gok. De code was: ", teGokkenCode)

def feedback_size_strat(gok, kleur): #
    possibleCombinations = []
    possibleFeedback = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [4, 0]]

    for ii in range(6 ** 4):    #Alle mogelijke codes in een lijst zetten.
        index0 = math.floor(ii / (6 ** 3)) % 6
        index1 = math.floor(ii / (6 ** 2)) % 6
        index2 = math.floor(ii / 6) % 6
        index3 = ii % 6

        singleCombination = (kleur[index0] + " " + kleur[index1] + " " + kleur[index2] + " " + kleur[index3]).split(" ")
        possibleCombinations.append([singleCombination])

    print(teGokkenCode)

    for i in range(0, 21):
        if len(possibleCombinations) < 1:
            gok = possibleCombinations[random.randint(0, len(possibleCombinations))][0]
        else:
            gok = possibleCombinations[0][0]

        print("Computer gok: ", gok)
        check(gok, teGokkenCode)

        fb = feedback(gok, teGokkenCode).copy()
        print(fb)
        fbsize = (fb[0] + fb[1])

        for iii in range(len(possibleCombinations)):
            fbPossibleCombs = feedback(possibleCombinations[iii][0], teGokkenCode)[0] + feedback(possibleCombinations[iii][0], teGokkenCode)[1]

            if fb != 4:
                if fbPossibleCombs == fbsize:
                    possibleCombinations[iii] = 0
            else:
                continue

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
    print("Kies. \n"
          "De speler geeft de code en de computer raad, typ dan 'x'. \n"
          "De computer geeft de code en de speler raad, typ dan 'y'. ")
    keuze = input()
    if keuze == "x":
        keuzestrat = input("welke strategie? \n"
                      "A: Letterlijk gokken. \n"
                      "B: Simple strategy. \n"
                      "C: Feedbacksize strategy (werkt niet volledig).")
        if keuzestrat == "A":
            geef_code(teGokkenCode)
            litterally_guessing_strategy(gegokteCode, kleuren) #Strategie van compleet willekeurig gokken, laag slagingspercentage, desalniettemin een strategie.
        elif keuzestrat == "B":
            geef_code(teGokkenCode)
            a_simple_strategy(kleuren, gegokteCode) #Strategie, werkt door middel van het proces van eliminatie door elke mogelijke code te vergelijken met de gok op basis van de feedback op de gok.
        else:
            geef_code(teGokkenCode)
            feedback_size_strat(gegokteCode, kleuren)  # Strategie werkt door de hoeveelheid pinnetjes in de feedback van elke mogelijke code te vergelijken met de hoeveelheid pinnetjes in de feedback van de gok.

    if keuze == "y":
        genereer_code(teGokkenCode, kleuren)
        speler_gok(gegokteCode)

def play_mastermind():
    print("Dit is het spel 'Mastermind'. ")
    player_or_computer()

play_mastermind()

