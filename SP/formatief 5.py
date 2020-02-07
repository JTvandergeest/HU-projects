def sorteren():
    getallenlijst = [5, 6, 2, 4, 1, 4, 7, 9, 3]

    for getal in range(len(getallenlijst)-1, 0, -1):
        for x in range(getal):
            if getallenlijst[x] > getallenlijst[x + 1]:
                getallenlijst[x + 1], getallenlijst[x] = getallenlijst[x], getallenlijst[x + 1]
    print(getallenlijst)

sorteren()