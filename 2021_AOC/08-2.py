#! /usr/bin/env python3


from operator import truediv


def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_08_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_08.txt")
    data=data.readlines()
    data=[i.split("|") for i in data]
    i=0
    while i < len(data):
        data[i]=[data[i][j].strip().split() for j in range(len(data[i]))]
        i+=1
    decrypting_data=[]
    answer_data=[]
    i=0
    for line in data:
        decrypting_data.append([])
        answer_data.append([])
        for element in line[0]:
            decrypting_data[i].append(element)
        for element in line[1]:
            answer_data[i].append(element)
        i+=1     
    return decrypting_data , answer_data


def find_cyphers(decrypting_data):
    cypher=[]
    for string in decrypting_data:
        letter_set=["a","b","c","d","e","f","g"]
        for element in string:
            if len(element)==2:
                d1=element
            if len(element)==3:
                d7=element
            if len(element)==4:
                d4=element
            if len(element)==7:
                d8=element
        for letter in letter_set:
                occurences=0
                for element in string:
                    if letter in element:
                        occurences+=1
                if occurences==6: B=letter
                if occurences==4: E=letter
                if occurences==9: F=letter
        for letter in letter_set:
            if letter in d7 and letter not in d1:
                A=letter
            if letter !=F and letter in d1:
                C=letter
        for letter in letter_set:
            if letter !=B and letter!=C and letter!=F and letter in d4:
                D=letter
        for letter in letter_set:
            if letter!=A and letter!=B and letter!=C and letter!=D and letter!=E and letter!=F:
                G=letter
        cypher.append([[A,"A"],[B,"B"],[C,"C"],[D,"D"],[E,"E"],[F,"F"],[G,"G"]])
    return cypher

def decrypt_data(cypher_list,answer_data):
    i=0
    while i < len(answer_data):
        j=0
        while j < len(answer_data[i]):
            for letter in cypher_list[i]:
                answer_data[i][j]=answer_data[i][j].replace(letter[0],letter[1])
            answer_data[i][j]=sorted(answer_data[i][j])
            j+=1
        i+=1
    return answer_data
                
def translate_data(decrypted_data):
    final_answers=[]
    i=0
    for number in decrypted_data:
        final_answers.append(0)
        j=3
        for digit in number:
            if digit==['C','F']:
                x=1
            if digit==['A', 'C', 'D', 'E', 'G']:
                x=2
            if digit==['A', 'C', 'D', 'F', 'G']:
                x=3
            if digit==['B', 'C', 'D', 'F']:
                x=4
            if digit==['A', 'B', 'D', 'F', 'G']:
                x=5
            if digit==['A', 'B', 'D', 'E', 'F', 'G']:
                x=6
            if digit==['A', 'C', 'F']:
                x=7
            if digit==['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                x=8
            if digit==['A', 'B', 'C', 'D', 'F', 'G']:
                x=9
            if digit==['A', 'B', 'C', 'E', 'F', 'G']:
                x=0
            final_answers[i]+=10**j*x
            j-=1
        i+=1
    return final_answers

def main(type):
    decrypting_data , answer_data = open_file_and_parse(type)
    cypher_list=find_cyphers(decrypting_data)
    decrypted_data=decrypt_data(cypher_list,answer_data)
    translated_data=translate_data(decrypted_data)
    print(sum(translated_data))




type="main"
# type="temp"
# type="test"



main(type)
