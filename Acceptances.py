from EssayAnalysis import Essay
import csv
def listchecker():
    list1 = []

    list2 = []

    def samelist(l1, l2):
        discrepancy = []
        for x in l1:
            if x not in l2:
                discrepancy.append(x)
        for y in l2:
            if y not in l1:
                discrepancy.append(y)
        if discrepancy == []:
            print("All good")
            return True
        else:
            print("Error: %s" % discrepancy)
            return False

    with open("Davids_List.txt") as contents:
        for item in contents:
            try:
                list1.append(int(item))
            except:
                continue

    with open("MannysList.txt") as contents:
        for item in contents:
            try:
                list2.append(int(item))
            except:
                continue

    samelist(list1, list2)
    print(138 in list1)

