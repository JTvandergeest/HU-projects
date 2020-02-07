def CheckPalindroom():
    print("Geef een woord: ")
    Gegevenwoord = str(input())
    woord = list(Gegevenwoord)
    palindroom = True
    niet = False

    for letter in woord:
        if letter == woord[-1]:
            del woord[-1]
        else:
            palindroom = niet
            break

    print(palindroom)

CheckPalindroom()