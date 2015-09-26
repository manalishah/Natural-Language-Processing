# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:06:42 2015

@author: manali
"""

import sys


def classify():
    testFile = sys.argv[2]
    modelFile = sys.argv[1]
    
    f = open(modelFile)
    l = f.readline()
    classes = eval(l)
    output = {}
    
    
    data = [line.rstrip() for line in open(testFile)]
    for each_class in classes.keys():
        output[each_class] = 0
    
        
    prediction = ''
    for i in range(0, len(data)):
        line = data[i].split(' ')
        for each_class in output.keys():
            prob = classes[each_class]['probability']
            for j in range(0, len(line)):
                feature_count = line[j].split(':')
                if feature_count[0] in classes[each_class]:
                    prob += classes[each_class][feature_count[0]]
            output[each_class] = prob
            prob = 0
        v=list(output.values())
        k=list(output.keys())
        prediction += k[v.index(max(v))] + '\n'
    
    index = testFile.rindex('.')
    testFile = testFile[:index]
    f = open(testFile + '.out' ,'w')
    f.write(prediction)
    f.close()    
    #print(prediction)

classify()