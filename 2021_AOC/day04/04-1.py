#! /usr/bin/env python3

from copy import copy

# Read puzzle input from file into 2D char array
data=open("./data_04.txt")
# data=open("./data_04_test.txt")
templist=data.readlines()

#generate guess list and 4 bingo boards (a, b1, b2)
#for each one given, one copy and one blank oriented each way

#check guesses, and copy matches from filled to blank board

#check blank boards for winners

#if winner found, compute score

#print(templist)



#CREATE LIST OF GUESSES AS INTS
guessesstr=templist[0].removesuffix("\n")
guessesstr=guessesstr.split(",")
guesses=[]
for string in guessesstr:
    guesses.append(int(string))


#FORMAT GAME BOARDS INTO 2D ARRAY
i=2
tempa=[]
while i<len(templist):
    x=templist[i].replace("\n","")

    if len(x)!=0:
        tempa.append(x.split())
    i+=1

#FORMAT GAME BOARDS INTO 3D ARRAY AND MAKE GUESS BOARDS
a=[]
b1=[]
b2=[]
i=0
while i<len(tempa):
    j=0
    a.append([])
    b1.append([])
    b2.append([])
    while j<len(tempa[0]):
        a[int(i/5)].append(tempa[i+j])
        b1[int(i/5)].append([])
        b2[int(i/5)].append([])
        j+=1
    i+=5
# print(len(b2))
# print(len(b2[0]))
# print(len(b2[0][0]))

#FUNCTION TO SUBMIT GUESSES TO GAME BOARD AND COPY MATCHES TO GUESS BOARDS

def submitguess(guess,a,b1,b2):
    i=0
    for board in a:
        j=0
        for row in board:
            k=0
            for column in row:
                if str(guess)==a[i][j][k]:
                    b1[i][j].append(guess)
                    b2[i][k].append(guess)
                k+=1
            j+=1
        i+=1
    return [b1,b2]

#FUNCTION TO CHECK IF THERE IS WINNING BOARD
def wincheck(b):
    i=0
    for boardset in b:
        j=0
        for board in boardset:
            for row in board:
                if len(row)==5:
                    return [1,i,j]
            j+=1
        i+=1
    return[0,0,0]

#CHECK GUESSES TO SEE IF THEY MAKE A WIN

for guess in guesses:
    x=submitguess(guess,a,b1,b2)
    y=wincheck(x)
    if y[0]==1:
        winningguess=guess
        break
    else:
        b1=x[0]
        b2=x[1]
winningboard=x[y[1]][y[2]]

#CALCULATE SCORE
negscore=0
for row in winningboard:
    for item in row:
        negscore+=item

sumscore=int(-1*negscore)
for row in a[y[2]]:
    for column in row:
        sumscore+=int(column)
score=sumscore*winningguess
print(score)