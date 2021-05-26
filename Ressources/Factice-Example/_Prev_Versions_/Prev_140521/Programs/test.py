from math import *
import numpy as np
import pandas as pd
import random
import pandas as pd


inde = [0,1,2,3,4,5,2,2,2,2,2,2]
inde.pop(8)
print(inde)
"""
data0 = ['Video', 'Video', 'Video', 'Video', 'Quiz', 'Quiz']
data1 = ['Video', 'Video', 'Video', 'Video', 'Lecture', 'Quiz', 'Lecture']
data_remove_vid = []
data_vid_add = ['Video']


def swap(glob_array, add_array, strng_change):
    for add in add_array:
        if strng_change in glob_array:
            index = [i for i in range(len(glob_array)) if glob_array[i] == strng_change]   #Find the index of the identical ID as the current «course» selected ID.    
            if len(index) == 0:
                continue
            else:
                glob_array[random.choice(index)] = add
                
    return glob_array
    
glob = swap(data0, [], 'Lecture')
print(glob)

"""
"""
import datetime
date = ["01-02-21", "01-01-21", "12-12-21", '20-12-21', '12-03-21', '16-03-21', '15-06-20']
format = "%d-%m-%y" 
dt_object = []
for dat in date:
    new_date = datetime.datetime.strptime(dat, format)
    dt_object.append(new_date)
    if (new_date > datetime.datetime(2021, 1, 1)) == True:
        print(new_date)

"""

"""
date_to_datetime()
for dat in date:
    dat_split = dat.split('-')
    if (dat_split[0] == '15' and dat_split[0]):
        print(dat)


    if ((dat_split[0] >= '15') and (dat_split[1] == '3') and (dat_split[2] == '21')) or ((dat_split[1] > '3') and (dat_split[2] == '21')):
        print(dat)
"""
"""
array = [10,11,12,'Exam',14,15, 10,12,10,15,'Exam',10, 'Exam', 10, 'Exam', 10, 11, 12, 13, 14, 15, 16, 17]
from math import *
import numpy as np


basic_SeqJoint_INS = ['Quizz-Quizz-Quizz-Video-Exam']
b2 = ['exam', 'quiz']
test = '-'.join(basic_SeqJoint_INS[0].split("-") + b2)
print(test)
def n_exam(array):
    index_exam = [i for i in range(len(array)) if array[i] == 'Exam' ]   #Find the index of the identical ID as the current «course» selected ID.    
    if len(index_exam) == 0:
        return array

    if len(index_exam) == 1:
        nw_position = len(array) -1
        old_position = index_exam[0]
        value_exchange = array[nw_position]
        array[nw_position] = 'Exam'
        array[old_position] = value_exchange

    elif len(index_exam) > 1:
        for index, i in zip(index_exam, range(1, len(index_exam)+1)):
            nw_position = round(((len(array) - 1)*i)/len(index_exam))
            print(nw_position)
            old_position = index
            value_exchange = array[nw_position]
            array[nw_position] = 'Exam'
            array[old_position] = value_exchange
    
    return array

nb_exam = array.count('Exam') 
new_array = n_exam(array)

print(len(array))
print(new_array) """