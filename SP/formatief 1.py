print("Hoe groot?")
grootte = int(input())

for x in range(grootte):
    y = x + 1
    print("*" * y)

for x in range(grootte):
    grootte = grootte-1
    print("*" * grootte)

