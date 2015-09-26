# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:00:23 2015

@author: manali
"""

import random
import math
from copy import deepcopy
import sys


def learn():
    trainingFile = sys.argv[1]
    modelFile = sys.argv[2]
    
    
    #get data from file
    data = [line.rstrip() for line in open(trainingFile)]
    random.shuffle(data)
    
    classes = {}
    
    for l in data:
        className = l.split(' ')[0]
        if className not in classes:
            classes[className] = {}
    
    #documents and total words in each class
    document_word = deepcopy(classes)
    
    for k in document_word.keys():
        document_word[k]['docs'] = 0
        document_word[k]['words'] = 0
    
    for i in range(0,len(data)):
            line = data[i].split(' ')
            print(line[0])
            document_word[line[0]]['docs'] += 1     
            for j in range(1,len(line)):
                feature_count = line[j].split(':')
                if feature_count[0] in classes[line[0]]:
                   classes[line[0]][feature_count[0]] += int(feature_count[1])
                   document_word[line[0]]['words'] += int(feature_count[1])
                else:
                   classes[line[0]][feature_count[0]] = int(feature_count[1])
                   document_word[line[0]]['words'] += int(feature_count[1]) 
    
    
    #compute probabilities using add 1 smoothing
    union_keys = set([])
    for each_class in classes.keys():
        union_keys |= set([int(val) for val in classes[each_class].keys()])
    
    for each_class in classes.keys():
        diff = union_keys - set([int(val) for val in classes[each_class].keys()])
        for each_key in diff:
            classes[each_class][str(each_key)] = 0
    
    for each_class in classes.keys():
        for feature in classes[each_class].keys():
            v = classes[each_class][feature]
            totalWordsInClass = document_word[each_class]['words']
            classes[each_class][feature] = math.log((v + 1)/(totalWordsInClass + len(union_keys)))
            #classes[each_class][feature] = (v + 1)/(totalWordsInClass + len(union_keys))
    
    #store probability of a class given the set of documents
    for each_class in classes.keys():
        classes[each_class]['probability'] = math.log(document_word[each_class]['docs']/ len(data))
        #classes[each_class]['probability'] = document_word[each_class]['docs']/ trainingSize
        
    #dump dict in modelfile location
    f = open(modelFile, 'w')
    f.write(str(classes)) 
    f.close()

learn()    