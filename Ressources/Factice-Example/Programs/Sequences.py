###########################################
# digitource par Cours par Année (Factice) #        
###########################################

#Import the required packages
from math import *
import numpy as np
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt
import os 
import time


########
# Time #
########

start_time = time.time()


################
#Find the Path #
################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Ressources', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 2000 ) #The seed does not need to be randomize


######################
# Class and Function #
######################

def Prep_Seq(rng1, rng2, string):
    temp_seq = []
    rng = rng1 - rng2
    for l in range(rng):
        temp_seq.append(string)
    return(temp_seq)

def pos(array, str_array):
    index_str = [i for i in range(len(array)) if array[i] in str_array]   #Find the index of the identical ID as the current «course» selected ID.    
    if len(index_str) == 0:
        pass
    elif len(index_str) == 1:
        nw_position = len(array) - 1
        old_position = index_str[0]
        value_exchange = array[nw_position]
        array[nw_position] = array[old_position]
        array[old_position] = value_exchange
    else:
        for index, i in zip(index_str, range(1, len(index_str)+1)):
            nw_position = round(((len(array) - 1)*i)/len(index_str))
            old_position = index
            value_exchange = array[nw_position]
            array[nw_position] = array[old_position]
            array[old_position] = value_exchange

    if 'Exam' in array:
        index_exam = [i for i in range(len(array)) if array[i] == 'Exam']   #Find the index of the identical ID as the current «course» selected ID.    
        nw_position = len(array) - 1
        old_position = index_exam[0]
        value_exchange = array[nw_position]
        array[nw_position] = array[old_position]
        array[old_position] = value_exchange

    return array


def swap(glob_array, add_array, strng_change):
    for add in add_array:
        index = [i for i in range(len(glob_array)) if glob_array[i] == strng_change]   #Find the index of the identical ID as the current «course» selected ID.    
        if index != []:
            if len(index) == 0:
                continue
            else:
                glob_array[random.choice(index)] = add
                
    return glob_array


#################################
# Import the required Data file #
#################################

#Import the dataframe
Ressources_Sequence = pd.read_csv(path_data + 'Ressources.csv')

#Drop the first column of the dataframe (empty)
Ressources_Sequence = Ressources_Sequence.iloc[: , 1:]

##########################
# Factice  Sequence Data #
##########################

#Basic Sequence Lists
basic_SeqJoint = []   #Basic List containing the sequence joint of each course

#Temporary ID:
temp_ID = []

#Loop 
for seq, course_ID in zip(range(0, len(Ressources_Sequence)), Ressources_Sequence['Course_ID']):
    if course_ID in temp_ID:
        ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        basic_SeqJoint_INS = [basic_SeqJoint[ins[-1]]]
        basic_SeqJoint_INS = basic_SeqJoint_INS[0].split('-')

        #Digit
        num_Video = Ressources_Sequence['Number_Video'].iloc[ins[-1]]
        num_QCM = Ressources_Sequence['Number_QCM'].iloc[ins[-1]]
        num_Test = Ressources_Sequence['Number_Test'].iloc[ins[-1]]

    else: 
        num_Video = num_QCM = num_Test = 0
        num_Lecture = num_Exercise = num_Exam = 0

    Digit_VidTemp = Prep_Seq(Ressources_Sequence['Number_Video'].iloc[seq], num_Video, 'Video')
    Digit_QCMTemp = Prep_Seq(Ressources_Sequence['Number_QCM'].iloc[seq], num_QCM, 'QCM')
    Digit_ExamTemp = Prep_Seq(Ressources_Sequence['Number_Test'].iloc[seq], num_Test, 'Test')

    if course_ID in temp_ID: 
        #Basic List
        basic_SeqTemp = swap(basic_SeqJoint_INS, Digit_VidTemp, 'Lecture')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_QCMTemp, 'Exercise')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_ExamTemp, 'Examen')
        pos(basic_SeqTemp, ['Test', 'Examen'])
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)

    else:
        #Presentiel
        num_Lecture = 0
        num_Exercise = 0
        num_Exam = 0
        Pres_LectTemp = Prep_Seq(Ressources_Sequence['Number_Lecture'].iloc[seq], num_Lecture, 'Lecture')
        Pres_ExerTemp = Prep_Seq(Ressources_Sequence['Number_Exercise'].iloc[seq], num_Exercise, 'Exercise')
        Pres_ExamTemp = Prep_Seq(Ressources_Sequence['Number_Exam'].iloc[seq], num_Exam, 'Examen')

        #Basic List
        basic_SeqTemp = Digit_VidTemp + Pres_LectTemp +  Digit_QCMTemp + Pres_ExerTemp + Digit_ExamTemp + Pres_ExamTemp
        random.shuffle(basic_SeqTemp)
        pos(basic_SeqTemp, ['Test', 'Examen'])
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)
        
    temp_ID.append(course_ID)


Ressources_Sequence['Sequence'] = basic_SeqJoint

print(Ressources_Sequence.head(5))


#######################
# Preparing Sequences #
#######################
"""
Prepared_Sequence = pd.DataFrame(columns=['Course_ID', 'Year', 'Course_Digit_Duration', 'Ressources_Amount', 'Ressources_Rank', 'Ressources_Type_Basic', 'Ressources_Type_Advanced'])
for num in range(len(Sequences_8_30)):
    count = 1
    list_basic = Sequences_8_30.iloc[num]['Basic_Sequence'].split("-")
    list_advanced = Sequences_8_30.iloc[num]['Advanced_Sequence'].split("-")
    for basic,advanced in zip(list_basic, list_advanced):
        Prepared_Sequence = Prepared_Sequence.append({
            'Course_ID': Sequences_8_30.iloc[num]['Course_ID'], 
            'Year': Sequences_8_30.iloc[num]['Year'], 
            'Course_Digit_Duration': Sequences_8_30.iloc[num]['Course_Digit'],
            'Ressources_Amount': Sequences_8_30.iloc[num]['Number_Ressources'],
            'Ressources_Rank': count, 
            'Ressources_Type': basic}, 
            'Ressources_Type': advanced}, ignore_index=True)
        count += 1
"""

list_Course_ID = []
list_Course_Year = [] 
list_Duration = []
list_Ress_Digit = []
list_Ress_inClass = []
list_Ressources = []
list_Count = []
list_BasicSeq = []

for num in range(len(Ressources_Sequence)):
    count = 1
    list_basic = Ressources_Sequence.iloc[num]['Sequence'].split("-")
    for basic in list_basic:
        list_Course_ID.append(Ressources_Sequence.iloc[num]['Course_ID'])
        list_Course_Year.append(Ressources_Sequence.iloc[num]['Year'])
        list_Duration.append(Ressources_Sequence.iloc[num]['Course_Duration'])
        list_Ress_Digit.append(Ressources_Sequence.iloc[num]['Course_Ress_Digit'])
        list_Ress_inClass.append(Ressources_Sequence.iloc[num]['Course_Ress_inClass'])
        list_Ressources.append(Ressources_Sequence.iloc[num]['Course_Ressources'])
        list_Count.append(count) 
        list_BasicSeq.append(basic)
        count += 1

Prepared_Sequence = pd.DataFrame({'Course_ID': list_Course_ID,
              'Year': list_Course_Year,
              'Course_Duration': list_Duration,
              'Course_Ress_Digit': list_Ress_Digit,
              'Course_Ress_inClass': list_Ress_inClass,
              'Ressources_Amount': list_Ressources,
              'Ressources_Rank': list_Count,
              'Ressources_Type_Basic': list_BasicSeq,
})

print(Prepared_Sequence.head(5))

#############
# Save Data #
#############

#Save the «Ressources_Sequence» into a CSV file.
Ressources_Sequence.to_csv(path_data + 'Ressources_Sequence.csv')

#Save the «Prepared_Sequence» into a CSV File.
Prepared_Sequence.to_csv(path_data + 'Prepared_Sequences.csv')


#########################
# Data Preparation DONE #
#########################
Total_Time = round(time.time() - start_time, 2)
print("Program Execution Time: %s seconds" % (Total_Time))
