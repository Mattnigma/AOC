#! /usr/bin/env python3

class Transformation:
    trans_dict = {}

    @classmethod
    def fill_dict(cls, trans_list):
        for trans in trans_list:
            cls.trans_dict[trans.input] = trans

    @classmethod
    def add_poly_layer(cls):
        for trans_name in cls.trans_dict:
            trans = cls.trans_dict[trans_name]
            for target_name in trans.output:
                target = cls.trans_dict[target_name]
                target.temp_count += trans.count

    def __repr__(self):
        return f"<Trans.{self.input}>"

    def __init__(self, line):
        line = line.split(" -> ")
        self.input = line[0]
        self.output = [line[0][0] + line[1], line[1] + line[0][1]]
        self.count = 0
        self.temp_count = 0

    def finish_count(self):
        self.count = self.temp_count
        self.temp_count = 0


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
    rule_list = []
    for rule in data[2::]:
        rule_list.append(Transformation(rule))
    rule_dict = {}
    return template, rule_list


def init_system(rule_list, template):
    Transformation.fill_dict(rule_list)
    first_last = [template[0], template[-1]]
    i = 0
    while i < len(template) - 1:
        Transformation.trans_dict[template[i:i + 2]].count += 1
        i += 1
    return rule_list, first_last


def score_template(trans_list, first_last):
    char_scores = {}
    for trans in trans_list:
        for char in trans.input:
            try:
                char_scores[char] += trans.count
            except:
                char_scores[char] = trans.count
    for char in first_last:
        char_scores[char] += 1
    score_vals = [int(score / 2) for char, score in char_scores.items()]
    score = max(score_vals) - min(score_vals)
    return score


def main():
    template, rules = open_file_and_parse(run_type)
    transformations, first_last = init_system(rules, template)
    Transformation.fill_dict(transformations)
    for i in range(40):
        Transformation.add_poly_layer()
        for trans in transformations:
            trans.finish_count()
    score = score_template(transformations, first_last)
    print(score)


run_type = "main"
# run_type="temp"
# run_type = "test"

main()
