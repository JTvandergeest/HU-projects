getal = 0
while getal <= 100:
    if (getal % 3 == 0) and (getal % 5 == 0):
        print("fizzbuzz")
        getal += 1
    elif getal % 3 == 0:
        print("fizz")
        getal += 1
    elif getal % 5 == 0:
        print("buzz")
        getal += 1
    else:
        print(getal)
        getal += 1