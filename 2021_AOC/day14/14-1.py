#! /usr/bin/env python3

class Transformation:

    def __repr__(self):
        return f"<Trans.{self.input}>"

    def __init__(self, line):
        line = line.split(" -> ")
        self.input = line[0]
        self.output = line[0][0] + line[1] + line[0][1]


def open_file_and_parse(test_or_main):
    # open correct file
    if test_or_main == "test":
        data = open("./day14/data_14_test.txt")
    elif test_or_main == "temp":
        data = open("./misc/temp.txt")
    else:
        data = open("./day14/data_14.txt")
    data = data.readlines()
    data = [i.strip() for i in data]
    template = data[0]
    rule_list=[]
    for rule in data[2::]:
        rule_list.append(Transformation(rule))
    rule_dict={}
    for rule in rule_list:
        rule_dict[rule.input] = rule.output
    return template, rule_dict


def use_rules(template, rule_dict):
    i=0
    while i < len(template)-1:
        template = template[0:i] + rule_dict[template[i:i+2]] + template[i+2:]
        i+=2
    return template


def get_score(template):
    char_scores={}
    for char in template:
        try:
            char_scores[char] += 1
        except:
            char_scores[char] = 1
    score_vals=[score for char, score in char_scores.items()]
    score = max(score_vals) - min(score_vals)
    return score


def main():
    template, rules = open_file_and_parse(run_type)
    for i in range(40):
        template=use_rules(template, rules)
        print(i)
    score = get_score(template)
    print(score)


# run_type="main"
# run_type="temp"
run_type = "test"

main()