import random

kleuren = ["blauw", "rood", "geel", "groen", "wit", "zwart"]
teGokkenCode = []
gegokteCode = []

def genereer_code(y,z):
    for i in range(0,4):
        x = random.randint(0,5)
        y.append(z[x])
    return y

def geef_code(y):
    print("Geef een code.")
    y = input().split(" ")
    return y

def speler_gok(y):
    print("De mogelijke kleuren zijn: 'blauw, rood, geel, groen, wit en zwart'. "
          "Doe een gok van 4 kleuren met een spatie tussen 2 kleuren. "
          "Gebruik exclusief kleine letters en spaties tussen de kleuren.")

    for i in range(0,11):
        print("Doe een gok.")
        y = input().split(" ")
        tempcode = y
        check(y, teGokkenCode)
        print("Jouw gok: ", y)
        print(feedback(y, teGokkenCode))
        y = tempcode

    print("Helaas, je gokken zijn op. De code was: ", teGokkenCode)

def check(y, x):
    if x == y:
        print("Dat is de juiste code, gefeliciteerd!")
        exit()
    else:
        print("Dat is helaas niet de juiste code.")

def computer_gok():
    mogelijkeCodes = []
    


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

    pinnetjes = ["B", blackpin, "W", whitepin]
    return pinnetjes

def player_or_computer():
    print("Kies. "
          "De speler geeft de code en de computer raad, typ dan 'x'. "
          "De computer geeft de code en de speler raad, typ dan 'y'. ")
    keuze = input()
    if keuze == "x":
        geef_code(teGokkenCode)
        #computer_gok()

    if keuze == "y":
        genereer_code(teGokkenCode, kleuren)
        speler_gok(gegokteCode)

def play_mastermind():
    print("Dit is het spel 'Mastermind'. ")
    player_or_computer()

play_mastermind()
#genereer_code(teGokkenCode, kleuren)
#geef_code(teGokkenCode)
#print(teGokkenCode) #moet nog weggehaald worden
#speler_gok(gegokteCode)
#feedback(gegokteCode, teGokkenCode)
#teGokkenCode.clear()
