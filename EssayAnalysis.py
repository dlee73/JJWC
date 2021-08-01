import csv
import statistics

def strip_letters(string):
    newstring = ''
    for char in string:
        if not char.isalpha() and char != "_":
            newstring = newstring + char
    return newstring

def no_div_stat(essay):
    pass

class Essay:
    def __init__(self):
        self.scores = []
        self.div_stat_scores = []
        self.score_agg = 0 #i.e. the mean of the critical essay scores
        self.div_score_agg = 0 #i.e. the mean of the diversity statement scores
        self.finalscore = 0

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
        essay.div_stat_scores.append(float(row["Total Score"]))
        essay.div_score_agg = statistics.mean(essay.div_stat_scores)

print(d['15'].scores)
print(d['15'].score_agg)
print(d['15'].div_stat_scores)




