# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:41:14 2015

@author: manali
"""


import sys
from os import listdir

testFile = sys.argv[1]
vocabFile = sys.argv[2]
formattedTestFile = sys.argv[3]


f = open(vocabFile, 'r', encoding = 'latin1')
vocabDict = {}

i = 0
for line in f:
    vocabDict[i] = line.strip('\t\n')
    i += 1
inv_map = {v: k for k, v in vocabDict.items()}
len(inv_map)   
f.close()


files = listdir(testFile)
if '.DS_Store' in files:
    files.remove('.DS_Store')
    
formattedDataFile = open(formattedTestFile,'w')
for each_email in files:
    email_dict = {}
    file_path = testFile + '/' + each_email
    email_file = open(file_path, 'r', encoding = 'latin1')
    for line in email_file:
        line = line.strip('\n').split(' ')
        for each_word in line:
            if each_word not in email_dict:
                email_dict[each_word] = 1
            else:
                email_dict[each_word] += 1
    email_file.close()
    #map feature:count
    my_list = []
    order_features = {}
    for k in email_dict.keys():
        if k in inv_map:
            order_features[inv_map[k]] = email_dict[k]
    sorted_keys = [k for k in order_features.keys()]
    sorted_keys.sort()
    
    for k in sorted_keys:
        s = str(k) + ':'
        s += str(order_features[k])
        my_list.append(s)
    data = ''
    for feature_count in my_list:
        data += feature_count + ' '
    formattedDataFile.write(data.strip(' ') + '\n')    

    
       
formattedDataFile.close()