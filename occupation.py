#Charles Weng Jasper Cheung
#SoftDev1 pd 4
#HW3 StI/O: Divine your Destiny!
#2017-9-15

import random

def randomcsv(file_name):
    ###open up the file
    f = open(file_name, "rU")
    lines = f.read().splitlines()
    ###begin processing of the file into a dictionary
    occupations = {}
    total = 0
    ###skip first since it's a title block and last since its the total
    i = 1
    while (i < len(lines) - 1 ):
        line = lines[i].rsplit(",", 1)
        occupations[line[0]] = line[1]
        i += 1
        #print line
    #print occupations
    total = lines[len(lines) - 1].rsplit(",")[1]
    #print total


print randomcsv("occupations.csv")
