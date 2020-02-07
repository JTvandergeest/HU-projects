def gemiddeldeEnkeleLijst():
    lijstMetCijfers = [5, 4, 5, 8, 5, 3, 9, 13, 14, 8, 17, 16, 5]

    print(sum(lijstMetCijfers)//len(lijstMetCijfers))

gemiddeldeEnkeleLijst()

def gemiddeldeMeerdereLijsten():
    lijstMetLijsten = [[6, 5, 4], [9, 8, 1], [5, 2, 3]]
    for lijst in lijstMetLijsten:
        print(sum(lijst)//len(lijst))

gemiddeldeMeerdereLijsten()