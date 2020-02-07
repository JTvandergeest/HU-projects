#a.
def count():
    GivenList = [5, 6, 4, 8, 9, 4, 4, 5, 1, 4, 5, 13, 4, 6, 69]
    x = 4
    aantal = GivenList.count(int(x))
    print(aantal)
count()

#b.
def Grootste_verschil():
    GivenList = [0, 3, 7, 4, 9, 12, 1]
    counter = 1
    indexGivenList = 0
    emptyList = []
    while counter < len(GivenList):
        emptyList.append(abs(GivenList[indexGivenList+1] - GivenList[indexGivenList]))
        counter += 1
        indexGivenList += 1
    print(max(emptyList))
Grootste_verschil()

#c.
def VoldoetAanEisen():
    GivenList = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1]
    if GivenList.count(0) >= GivenList.count(1)
        return False
    if GivenList.count(0) > 12
        return False
    else:
        return True

VoldoetAanEisen()
    