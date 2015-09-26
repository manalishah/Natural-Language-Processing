# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:37:21 2015

@author: manali
"""

import sys 
import random

trainData = sys.argv[1]

data = [line.strip('\n') for line in open(trainData, 'r')]
random.shuffle(data)


index = trainData.rindex('.')
trainData = trainData[:index] 
split = [0.75, 0.25]

for each_split in split:
    trainingSize = round(each_split*len(data))
    f = open(trainData + str(each_split)[1:] + '.train', 'w')
    for i in range(0,trainingSize):
        f.write(data[i] + '\n')
    f.close()
    
    f = open(trainData + str(each_split)[1:] + '.dev', 'w')
    f2 = open(trainData + str(each_split)[1:] + '.label', 'w')
    for i in range(trainingSize, len(data)):
        line = data[i].split(' ')
        f2.write(line[0] + '\n')
        s = ''
        for j in range(1,len(line)):
            s += line[j] + ' '
        f.write(s.strip(' ') + '\n')
    f.close()
    f2.close()
    