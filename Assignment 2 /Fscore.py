# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:11:55 2015

@author: manali
"""

import sys

actual_labels = sys.argv[1]
prediction_labels = sys.argv[2]


actual_data = [line.strip('\n') for line in open(actual_labels)]
prediction_data = [line.strip('\n') for line in open(prediction_labels)]

classes = {}

for label in actual_data:
    if label not in classes:
        classes[label] = {}
for k in classes.keys():
    classes[k]['actual'] = 0
    classes[k]['correctlyClassified'] = 0
    classes[k]['totalClassified'] = 0

if len(actual_data) == len(prediction_data):
    for i in range(0,len(actual_data)):
        actual = actual_data[i]
        prediction = prediction_data[i]
        
        classes[actual]['actual'] += 1
        classes[prediction]['totalClassified'] += 1
        
        if prediction == actual:
            classes[prediction]['correctlyClassified'] +=1


index = prediction_labels.rindex('.')
if '/' in prediction_labels:
    nameIndex = prediction_labels.rindex('/') + 1
else:
    nameIndex = 0
prediction_labels = prediction_labels[nameIndex:index]
f = open(prediction_labels +'.Fscore', 'w')

s = ''
for each_class in classes.keys():
    s += 'Fscore of: ' + each_class
    recall = classes[each_class]['correctlyClassified']/classes[each_class]['actual']
    precision = classes[each_class]['correctlyClassified']/classes[each_class]['totalClassified']
    fscore = (2*precision*recall)/(precision + recall)
    s += '\nactual = ' + str(classes[each_class]['actual'])
    s += '\ncorrectly_classified = ' + str(classes[each_class]['correctlyClassified'])
    s += '\ntotal_classified = ' + str(classes[each_class]['totalClassified'])
    s += '\nFscore = ' + str(fscore) + '\n'
    f.write(s + '\n')
    s = ''



f.close()