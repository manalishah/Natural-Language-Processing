# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:26:20 2015

@author: manali
"""
import sys

trainingFile = sys.argv[1]
testingFile = sys.argv[2]

f1 = open(trainingFile,'r')
data = []
for line in f1:
    data.append(line.rstrip())
f1.close()

f = open('sentiment.nb.train', 'w')

s = ''
for line in data:
    line = line.split(' ')
    
    if int(line[0]) >= 7:  #ratings greater than 7 are positive
        line[0] = 'POSITIVE'
    else:  #ratings less than 4 are negative (data set doesn't contain 5,6 ratings)
        line[0] = 'NEGATIVE'

    for i in line:
        s += i + ' '
    s.rstrip(' ')
    s += '\n'
f.write(s.strip('\n'))
f.close()


f1 = open(testingFile,'r')
data = []
for line in f1:
    data.append(line.rstrip())
f1.close()

s  =''
f = open('sentiment.nb.test', 'w')
for line in data:
    s += line + '\n'
f.write(s.strip('\n'))
f.close()