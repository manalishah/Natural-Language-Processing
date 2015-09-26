# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:58:40 2015

@author: manali
"""
import sys
import os.path
train = sys.argv[1]
test = sys.argv[2]

#
#train = '/Users/manali/Desktop/CSCI544/nlp2/sentiment.nb.25.train'
#test = '/Users/manali/Desktop/CSCI544/nlp2/sentiment.nb.25.dev'

f = open(train, 'r')
trainingData = [line.strip(' \n') for line in f]
f.close()

if '/' in train:
    index = train.rindex('/') +1
    full_path = train[:index] 
    train = train[index:]
else:
    full_path = ''
index1 = train.index('.') + 1
midindex = train[index1:].index('.') + 1
outputFile = full_path + train[:index1] + 'svm.' + train[index1:][midindex:]
#modify target to +1 ot -1

svmDataset = {'SPAM':'-1', 'HAM':'+1', 'NEGATIVE':'-1', 'POSITIVE':'+1'}
megamDataset = {'SPAM':'0', 'HAM':'1', 'NEGATIVE':'0', 'POSITIVE':'1'}
for i in range(0,len(trainingData)):
    line = trainingData[i]
    line_target = line.split(' ')
    for j in range(1,len(line_target)):
        feature_count = line_target[j].split(':')
        line_target[j] = str(str(int(feature_count[0])+1) + ':' + feature_count[1])
    line = ''
    for j in range(1,len(line_target)):
        line += line_target[j] + ' '
    trainingData[i] = svmDataset[line_target[0]] + ' '+ line.rstrip(' ')


f = open(outputFile, 'w')
s = ''
for line in trainingData:
    s += line + '\n'
s.rstrip('\n')
f.write(s)
f.close()


#format for megaM toolkit
f = open(train, 'r')
trainingData = [line.strip(' \n') for line in f]
f.close()

for i in range(0,len(trainingData)):
    line = trainingData[i]
    line_target = line.split(' ')
    for j in range(1,len(line_target)):
        feature_count = line_target[j].split(':')
        line_target[j] = str(str(int(feature_count[0])+1) + ' ' + feature_count[1])
    line = ''
    for j in range(1,len(line_target)):
        line += line_target[j] + ' '
    trainingData[i] = megamDataset[line_target[0]] + ' '+ line.rstrip(' ')

outputFile = full_path + train[:index1] + 'megaM.' + train[index1:][midindex:]
f = open(outputFile,'w')
s = ''
for line in trainingData:
    s += line + '\n'
s.rstrip('\n')
f.write(s)
f.close()

f = open(test, 'r')
testData = [line for line in f]
f.close()

if '/' in test:
    index = test.rindex('/') +1
    full_path = test[:index] 
    test = test[index:]
else:
    full_path = ''
# for dev data only
index = test.rindex('.')
file = test[:test.rindex('.')] + '.label'

if os.path.isfile(full_path + file):
    labels = [i.strip('\n') for i in open(file)]
    flag = True
else:
    flag = False



for i in range(0,len(testData)):
    line = testData[i]
    line_target = line.split(' ')
    for j in range(0,len(line_target)):
        feature_count = line_target[j].split(':')
        line_target[j] = str(int(feature_count[0])+1) + ':' + feature_count[1]
    line = ''
    for j in range(0,len(line_target)):
        line += line_target[j] + ' '
    if flag:
        testData[i] = svmDataset[labels[i]] + ' ' + line.rstrip(' \n')
    else:
        testData[i] = '1 ' + line.rstrip(' \n')




index1 = test.index('.') + 1
midindex = test[index1:].index('.') + 1
outputFile = full_path + test[:index1] + 'svm.' + test[index1:][midindex:]


f = open(outputFile, 'w')
s = ''
for line in testData:
    s += line + '\n'
s.rstrip('\n')

f.write(s)
f.close()


#megaM test 
f = open(test, 'r')
testData = [line for line in f]
f.close()

for i in range(0,len(testData)):
    line = testData[i]
    line_target = line.split(' ')
    for j in range(0,len(line_target)):
        feature_count = line_target[j].split(':')
        line_target[j] = str(int(feature_count[0])+1) + ' ' + feature_count[1]
    line = ''
    for j in range(0,len(line_target)):
        line += line_target[j] + ' '
    if flag:
        testData[i] = megamDataset[labels[i]] + ' ' + line.rstrip(' \n')
    else:
        testData[i] = '1 ' + line.rstrip(' \n')

outputFile = full_path + test[:index1] + 'megaM.' + test[index1:][midindex:]
f = open(outputFile,'w')
s = ''
for line in testData:
    s += line + '\n'
s.rstrip('\n')
f.write(s)
f.close()
