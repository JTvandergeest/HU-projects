import random

randomnr = random.randint(1, 69)
gegoktenr = 0
while randomnr != gegoktenr:
    gegoktenr = int(input("Gok het nummer."))
    if gegoktenr == randomnr:
        print("Goed gegokt, het nummer was: ", randomnr)
    else:
        continue
