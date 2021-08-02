from EssayAnalysis import Essay
from utilities import*
import csv

Mannys_List = []

with open("MannysList.txt") as contents:
    for item in contents:
        try:
            Mannys_List.append(int(item))
        except:
            continue


#take essay data from csv, store them as class, key them to number, store in dictionary
total_essays = {}
with open("Final_JJWC_Scores.csv", mode="r") as file:
    contents = csv.DictReader(file)
    for row in contents:
        total_essays[row["Essay #"]] = Essay()
        essay = total_essays[row["Essay #"]]
        essay.z_score = float(row["Z_Score"])
        essay.preference = int(row["ILJ Preference"])
        essay.clr = int(row["Essay #"]) in Mannys_List
        essay.jlpp = row["Essay #"] in listify_file("RachelsList.txt")
        essay.ilj = essay.z_score > -1.7 and not essay.clr and not essay.jlpp
        if row["Essay #"] in listify_file("MadeOffer.txt"):
            essay.made_offer = True
        else:
            continue

with open("Acceptances_list.csv", mode="w") as file:
    file.write("Essay #,Z_Score,ILJ Preference,CLR,ILJ,JLPP,Made Offer\n")
    for essay in total_essays.keys():
        file.write("{},{},{},{},{},{},{}\n".format(essay,
                                                   total_essays[essay].z_score,
                                                   total_essays[essay].preference,
                                                   total_essays[essay].clr,
                                                   total_essays[essay].ilj,
                                                   total_essays[essay].jlpp,
                                                   total_essays[essay].made_offer))
ilj_accepts = []


for essay in total_essays.keys():
    if total_essays[essay].ilj:
        ilj_accepts.append(essay)

for x in ilj_accepts:
    if str(int(x)) not in listify_file("MadeOffer.txt"):
        print(x)




