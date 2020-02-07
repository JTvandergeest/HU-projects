def sorteren():
    LijstMetGetallen = [5, 2, 6, 9, 4, 1, 14, 3, 10, 8]

    GesoorteerdeLijst = []
    GesoorteerdeLijst.append(LijstMetGetallen[0])
    LijstMetGetallen.pop(0)
    counter = 0
    while counter < (len(LijstMetGetallen) + 1):
        if LijstMetGetallen[0] >= GesoorteerdeLijst[0]:
            GesoorteerdeLijst.append(LijstMetGetallen[0])
            LijstMetGetallen.pop(0)
            counter += 1
        elif LijstMetGetallen[0] <= GesoorteerdeLijst[0]:
            GesoorteerdeLijst.insert(0, LijstMetGetallen[0])
            LijstMetGetallen.pop(0)
            counter += 1

    print(GesoorteerdeLijst)

sorteren()

#niet af, maar de deadline kwam eraan