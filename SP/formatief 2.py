def compare_strings():
    print("Geef een string: ")
    string1 = str(input())

    print("Geef een string: ")
    string2 = str(input())

    counter = 1
    indexstring = 0

    if string1 == string2:
        print("De strings zijn gelijk.")

    elif string1 >= string2:
        while counter < len(string1):
            if string1[indexstring] != string2[indexstring]:
                print("Het eerste verschil zit op index: ", indexstring, ".")
                break
            elif counter > len(string2):
                print("Het eerste verschil zit op index: ", indexstring, ".")
                break
            else:
                counter += 1
                indexstring += 1
    else:
        while counter <= len(string2):
            if string2[indexstring] != string1[indexstring]:
                print("Het eerste verschil zit op index: ", indexstring, ".")
                break
            elif counter > len(string1):
                print("Het eerste verschil zit op index: ", indexstring, ".")
                break
            else:
                counter += 1
                indexstring += 1

compare_strings()