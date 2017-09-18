#Charles Weng Jasper Cheung
#SoftDev1 pd 4
#HW3 StI/O: Divine your Destiny!
#2017-9-15

import random

test = {}
def randomcsv(file_name):
    ###open up the file
    f = open(file_name, "rU")
    lines = f.read().splitlines()

    ###begin processing of the file into a dictionary
    occupations = {}
    total = 0
    ###skip first value since it's a title block and last value since its the total
    i = 1
    while (i < len(lines) - 1 ):
        line = lines[i].rsplit(",", 1)
        occupations[line[0]] = float(line[1])
        i += 1
        #print line
    #print occupations
    total = float(lines[len(lines) - 1].rsplit(",")[1])
    #print total

	'''
    ###creating a list to choose an occupation by %
    listo = []
    for key in occupations:
        for x in range( int ( float( occupations[key] ) * 10)  ):#XD Conversions
            listo.append(key)
    #print listo
    return random.choice(listo);
	'''

    ###find highest %
    i = 0
    high = 0
    keys = occupations.keys()
    while (i < len(occupations)):
        if(high < keys[i]):
                high = occupations[keys[i]]
        i += 1

    ###get a random number between the total and the highest
        #if it was below the highest any % higher than the random number wouold have the same chance of being chosen, which is bad
        #if it was higher than total then it wouldn't get an answer
    rand = random.random() * (total - high) + high
    #print rand

    winner = ""
    while(rand > 0):
        winner = random.choice(keys)
        #print winner
        rand -= occupations[winner]
        #print rand
    return winner


print randomcsv("occupations.csv")

for x in range(0,10001):
    a = randomcsv("occupations.csv")
    try:
        test[a] += 1
    except:
        test[a] = 1

print test
