# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:31:37 2015

@author: manali
"""
import os
import sys
from os import listdir

main_folder = sys.argv[1]
vocabFile = sys.argv[2]
labeledData = sys.argv[3]

f = open(vocabFile, 'r', encoding = 'latin1')
vocabDict = {}

i = 0
for line in f:
    vocabDict[i] = line.strip('\t\n')
    i += 1
inv_map = {v: k for k, v in vocabDict.items()}
len(inv_map)   
f.close()


directory = listdir(main_folder)
if '.DS_Store' in directory:
            directory.remove('.DS_Store')
direct = []
for each_folder in directory:
    direct.append(main_folder + '/' + each_folder)
#direct = ['enron1', 'enron2', 'enron4', 'enron5']
#direct = ['enron5']

formattedDataFile = open(labeledData,'w')

path = ''

for curr_folder in direct:
    formatted_data = []
    folders = ['ham','spam']
    path = curr_folder
    print(path)
    for each_folder in folders:
        folder_path = path + '/' + each_folder
        emails = listdir(folder_path)
        if '.DS_Store' in emails:
            emails.remove('.DS_Store')
        
        for each_email in emails:
            email_dict = {}
            file_path = folder_path + '/' + each_email
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
            data = each_folder.upper()
            for feature_count in my_list:
                data += ' ' + feature_count
            formattedDataFile.write(data + '\n')    
            formatted_data.insert(0,data)
            
       
formattedDataFile.close()