import csv
import statistics

class Essay:
    def __init__(self):
        self.crit_essay_scores = [] #out of 100
        self.div_stat_scores = [] #out of 20
        self.crit_score_agg = 0 #i.e. the mean of the critical essay crit_essay_scores
        self.div_score_agg = 0 #i.e. the mean of the diversity statement crit_essay_scores
        self.editscore = 0 #out of 435
        self.perc_crit_essay_score = self.crit_score_agg/100 #crit essay score as percentage
        self.perc_div_stat_score = self.div_score_agg/20
        self.perc_edit_score = self.editscore/435
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

with open("EditTestScores.csv", mode='r', encoding='utf-8-sig') as file:
    contents = csv.DictReader(file)
    error_list = []
    for row in contents:
        try:
            x = strip_letters(row["Competition#"])
            essay = d["%s" % x]
            essay.editscore = row["POINTS"]
        except:
            x = strip_letters(row["Competition#"])
            error_list.append(x)

print("Error: %s" % error_list)

crit_essay_scores = []
div_stat_scores = []
edit_test_scores = []

for item in d.keys():
    crit_essay_scores.append(d[item].crit_score_agg)
    div_stat_scores.append(d[item].div_score_agg)
    edit_test_scores.append(float(d[item].editscore))


if __name__ == "__main__":
    print(edit_test_scores)





