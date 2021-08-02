from EssayAnalysis import Essay
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
        essay.ilj = (essay.preference == 2 or essay.preference == 1) and essay.z_score > -2.0 and not essay.clr

with open("Acceptances_list.csv", mode="w") as file:
    file.write("Essay #,Z_Score,ILJ Preference,CLR,ILJ,JLPP\n")
    for essay in total_essays.keys():
        file.write("{},{},{},{},{},{}\n".format(essay,
                                              total_essays[essay].z_score,
                                              total_essays[essay].preference,
                                              total_essays[essay].clr,
                                              total_essays[essay].ilj,
                                              total_essays[essay].jlpp))
ilj_accepts = []

for essay in total_essays.keys():
    if total_essays[essay].ilj:
        ilj_accepts.append(essay)

print(", ".join(ilj_accepts))




