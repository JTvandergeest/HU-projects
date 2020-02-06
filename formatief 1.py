"opdr 1 for, punt rechts"    "Samengewerkt met Brandon Hillert"
print("Hoe groot?")
grootte = int(input())

for x in range(grootte):
     y = x + 1
     print("*" * y)

for x in range(grootte):
    grootte = grootte-1
    print("*" * grootte)

"for, punt links"
print("Hoe groot?")
grootte1 = int(input())

for x in range(grootte1):

    aantalspatie = str(" " * (grootte1 - (x + 1)))
    aantalster = str((x + 1) * "*")
    print(aantalspatie + aantalster)

for x in range(grootte1):
    aantalspatie = str("*" * (grootte1 - (x + 1)))
    aantalster = str((x + 1) * " ")
    print(aantalster + aantalspatie)

"while, punt rechts"
print("Hoe groot?")
grootte = int(input())
y = 0
while y < grootte:
    print(y * "*")
    y = y + 1

while grootte > 0:
    print("*"*grootte)
    grootte = grootte - 1

"while, punt links"
print("Hoe groot?")
grootte = int(input())
x = 1
y = 1
while grootte > y - 1:
    print(" " * (grootte - y), "*" * x)
    x = x + 1
    y = y + 1

x = 1
y = 1
while grootte > y - 1:
    print((" " * x), "*" * (grootte - y))
    x = x + 1
    y = y + 1

