templist = [78, 100, 69, 10, 91, 66, 150, 104, 147, 85, 130, 41, 124, 121, 55, 115, 42, 123, 105, 1, 163, 109]
with open("MadeOffer.txt", mode="w") as file:
    for x in templist:
        file.write("%s\n" % x)