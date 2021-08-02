import csv
import typing
import statistics


class Essay:
    def __init__(self):
        self.crit_essay_scores = []  # out of 100
        self.div_stat_scores = []  # out of 20
        self.crit_score_agg = 0  # i.e. the mean of the critical essay crit_essay_scores
        self.div_score_agg = 0  # i.e. the mean of the diversity statement crit_essay_scores
        self.editscore = 0  # out of 435
        self.perc_crit_essay_score = 0 #will multiply these values by 100 later on
        self.perc_div_stat_score = 0
        self.perc_edit_score = 0
        self.finalscore = 0
        self.z_score = 0
        self.preference = 3
        self.clr = False
        self.ilj = False
        self.jlpp = False
        self.called_Sue = False


def strip_letters(string):
    newstring = ''
    for char in string:
        if not char.isalpha() and char != "_" and char != " ":
            newstring = newstring + char
    return newstring


def zscore(data, mu, sigma):
    return (data - mu) / sigma


def no_div_stat(e: Essay) -> float:
    return 1.5*e.perc_edit_score + 1.5*e.perc_crit_essay_score

def yes_div_stat(e: Essay) -> float:
    return e.perc_edit_score + e.perc_crit_essay_score + e.perc_div_stat_score


# Read the reader responses spreadsheet, save the data as a class Essay and key it to the essay number
# save it to dictionary d.
def main():
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
            essay.perc_crit_essay_score = essay.crit_score_agg / 100
            essay.perc_crit_essay_score *= 100

    with open("Personal_Statements/Superseding_Responses_Div_Stat.csv", mode='r') as file:
        contents = csv.DictReader(file)
        for row in contents:
            essay = d["%s" % row["Competition#"]]
            essay.div_stat_scores.append(float(row["Total Score"]))
            essay.div_score_agg = statistics.mean(essay.div_stat_scores)
            essay.perc_div_stat_score = essay.div_score_agg / 20
            essay.perc_div_stat_score *= 100

    with open("EditTestScores.csv", mode='r', encoding='utf-8-sig') as file:
        contents = csv.DictReader(file)
        for row in contents:
            try:
                x = strip_letters(row["Competition#"])
                essay = d["%s" % x]
                essay.editscore = float(row["POINTS"])
                essay.perc_edit_score = essay.editscore / 435
                essay.perc_edit_score *= 100
            except:
                continue



    crit_essay_scores = []
    div_stat_scores = []
    edit_test_scores = []

    for item in d.keys():
        if yes_div_stat(d[item]) >= no_div_stat(d[item]):
            d[item].finalscore = yes_div_stat(d[item])
        else:
            d[item].finalscore = no_div_stat(d[item])
        crit_essay_scores.append(d[item].crit_score_agg)
        div_stat_scores.append(d[item].div_score_agg)
        edit_test_scores.append(float(d[item].editscore))

    with open("Final_JJWC_Scores.csv", mode="w", newline='') as file:
        fieldnames = ['Essay #', 'Diversity Statement Final', 'Critical Essay Final', 'Edit Test Final',
                      'Score with Div Statement', 'Score w/o Div Statement', 'Final Score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for essay_num in d.keys():
            writer.writerow({'Essay #': "%s" % essay_num,
                             'Diversity Statement Final': '%f' % d[essay_num].perc_div_stat_score,
                             'Critical Essay Final': '%f' % d[essay_num].perc_crit_essay_score,
                             'Edit Test Final': '%f' % d[essay_num].perc_edit_score,
                             'Score with Div Statement': "%f" % yes_div_stat(d[essay_num]),
                             'Score w/o Div Statement': '%f' % no_div_stat(d[essay_num]),
                             'Final Score': '%f' % d[essay_num].finalscore})
    testessay = d['15']
    print(testessay.div_score_agg)
    print(testessay.perc_edit_score)
    print(testessay.perc_crit_essay_score)
    print(testessay.finalscore)

if __name__ == "__main__":
    main()

