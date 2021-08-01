import csv
import statistics

class Essay:
    def __init__(self):
        self.crit_essay_scores = []
        self.div_stat_scores = []
        self.crit_score_agg = 0 #i.e. the mean of the critical essay crit_essay_scores
        self.div_score_agg = 0 #i.e. the mean of the diversity statement crit_essay_scores
        self.editscore = 0
        self.finalscore = 0

def strip_letters(string):
    newstring = ''
    for char in string:
        if not char.isalpha() and char != "_" and char != " ":
            newstring = newstring + char
    return newstring

def zscore(data, mu, sigma):
    return (data - mu) / sigma


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
        essay.crit_essay_scores.append(float(row["Total Score"]))
        essay.crit_score_agg = statistics.mean(essay.crit_essay_scores)

with open("Personal_Statements/Superseding_Responses_Div_Stat.csv", mode='r') as file:
    contents = csv.DictReader(file)
    for row in contents:
        essay = d["%s" % row["Competition#"]]
        essay.div_stat_scores.append(float(row["Total Score"]))
        essay.div_score_agg = statistics.mean(essay.div_stat_scores)

with open("2021 JJWC Edit Test Scores.csv", mode='r') as file
    contents = csv.DictReader(file)
    for row in contents:
        essay = d["%s" % strip_letters(row["ID"])]
        essay.editscore = row["POINTS"]

crit_essay_scores = []
div_stat_scores = []
edit_test_scores = []

for item in d.keys():
    crit_essay_scores.append(d[item].)


if __name__ == "__main__":
    print(d['15'].crit_essay_scores)
    print(d['15'].crit_score_agg)
    print(d['15'].div_stat_scores)
    print(strip_letters("Essay 147"))




