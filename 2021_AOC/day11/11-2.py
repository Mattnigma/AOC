#! /usr/bin/env python3

class Octopus:
    flash_count=0

    @classmethod
    def add_flash(cls):
        cls.flash_count += 1

    @classmethod
    def flash_reset(cls):
        cls.flash_count = 0

    def __init__(self, energy):
        self.energy=energy
        self.has_flashed=False

    def flash(self):
        if self.energy>9:
            if self.has_flashed==False:
                self.has_flashed=True
                return True
            else:
                return False
        else:
            return False

    def energize(self):
        self.energy+=1

    def reset(self):
        if self.energy>9:
            self.energy=0
        self.has_flashed=False

def open_file_and_parse(test_or_main):
    #open correct file
    if test_or_main=="test":
        data=open("./data_11_test.txt")
    elif test_or_main=="temp":
        data=open("./temp.txt")
    else:
        data=open("./data_11.txt")
    data=data.readlines()
    data=[i.strip() for i in data]
    return data

def init_octopi(data):
    octopi=[]
    i=0
    for row in data:
        octopi.append([])
        for column in row:
            octopi[i].append(Octopus(int(column)))
        i+=1
    return octopi

def run_simulation(octopi):
    # part I
    i=0
    while i < len(octopi):
        j=0
        while j<len(octopi[i]):
            octopi[i][j].energize()
            j+=1
        i+=1
    # Part II
    finished=False
    while finished == False:
        finished=True
        i=0
        while i < len(octopi):
            j=0
            while j < len(octopi[i]):
                did_flash=octopi[i][j].flash()
                if did_flash==True:
                    Octopus.add_flash()
                    for x in range(3):
                        for y in range(3):
                            if i+x-1 in range(0,len(octopi)):
                                if j+y-1 in range(0,len(octopi[j])):
                                    octopi[i+x-1][j+y-1].energize()
                                    finished=False
                j+=1
            i+=1
    # Part III
    i=0
    while i < len(octopi):
        j=0
        while j < len(octopi[i]):
            octopi[i][j].reset()
            j+=1
        i+=1
    # Secret Day 11 Part II Sauce
    Success=False
    number_of_octopi=len(octopi)*len(octopi[0])
    if Octopus.flash_count==number_of_octopi:
        Success=True
    else:
        Octopus.flash_reset()
    return octopi , Success

def main(type):
    data=open_file_and_parse(type)
    octopi=init_octopi(data)
    i=0
    while True:
        octopi , success = run_simulation(octopi)
        i+=1
        if success == True:
            break
    print(i)

type="main"
# doc_type="temp"
# doc_type="test"



main(type)
