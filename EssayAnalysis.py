import csv
import statistics

class Essay:
    def __init__(self):
        self.scores = []
        self.div_stat_scores = []
        self.score_agg = 0
        self.div_score_agg = 0

#Read the reader responses spreadsheet, save the data as a class Essay and key it to the essay number
#save it to dictionary d.
d = {}

with open("Grader_responses.csv", mode="r") as file:
    contents = csv.DictReader(file)

    for row in contents:
        if row["Competition Number"] not in d.keys():
            d["%s" % row["Competition Number"]] = Essay()
        essay = d["%s" % row["Competition Number"]]
        essay.number = int(row["Competition Number"])
        essay.scores.append(float(row["Total Score"]))
        essay.score_agg = statistics.mean(essay.scores)

with open("Personal_Statements/Superseding_Responses_Div_Stat.csv", mode='r') as file:
    contents = csv.DictReader(file)
    for row in contents:
        essay = d["%s" % row["Competition#"]]
        essay.div_stat_scores.append("Total Score")

print(d['1'].scores)
print(d['1'].score_agg)
print(d['1'].div_stat_scores)




