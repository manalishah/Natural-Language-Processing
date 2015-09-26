# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:46:45 2015

@author: manali
"""

import sys

predictionFile = '/Users/manali/Desktop/CSCI544/nlp2/spam.svm.75.prediction'
predictionFile = sys.argv[1]

dataset = {'spam':{1:'HAM', -1:'SPAM'}, 'sentiment':{1:'POSITIVE', -1:'NEGATIVE'}}

pred = [line for line in open(predictionFile)]

filetype = predictionFile[predictionFile.rindex('/')+1:predictionFile.index('.')]
output = []
for p in pred:
    if float(p) < 0:
        output.append(dataset[filetype][-1])
    else:
        output.append(dataset[filetype][1])



predictionFile = predictionFile[:predictionFile.rindex('.')] +'.out'
f = open(predictionFile, 'w')
for p in output:
    f.write(p + '\n')
f.close()