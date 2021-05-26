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

#################################
# Import the required Data file #
#################################

#Import the dataframe
Course_PerYear = pd.read_csv(path_data + 'Digitalization.csv')

#Drop the first column of the dataframe (empty)
Course_PerYear = Course_PerYear.iloc[: , 1:]

######################################
# Factice digitources Additional Data #
######################################

Course_PerYear = Course_PerYear[Course_PerYear['Course_ID'] < 5]

duration_digit_video = []
duration_digit_qcm = []
duration_digit_exam = []
number_digit_video = []
number_digit_qcm = []
number_digit_exam = []

duration_present_lecture = []
duration_present_exercise = []
duration_present_exam = []
number_present_lecture = []
number_present_exercise = []
number_present_exam = []

banned_id = []

temp_ID = []
for (digit, pres, course_ID) in zip(Course_PerYear['Course_Digit'], Course_PerYear['Course_Present'], Course_PerYear['Course_ID']):
    if course_ID not in temp_ID:
        if digit > 0:
            while digit != 0:
                random_vid = random.randint(0, ceil(digit*0.75))
                random_QCM = random.randint(0, ceil(digit*0.60))
                if digit <= 10:
                    random_exam = random.randint(0, 1)
                elif (digit > 10) and (digit <= 20):
                    random_exam = random.randint(0, 2)
                else:
                    random_exam = random.randint(0, 4)

                digit = digit - (random_vid + random_QCM + random_exam) 
                if digit != 0:
                    digit = digit + random_vid + random_QCM + random_exam
                elif random_QCM <= random_exam:
                    digit = digit + random_vid + random_QCM + random_exam
                elif random_vid < random_exam:
                    digit = digit + random_vid + random_QCM + random_exam
                elif digit == 0:
                    duration_digit_video.append(random_vid)
                    duration_digit_qcm.append(random_QCM)
                    duration_digit_exam.append(random_exam)

                    number_digit_video.append(random.randint(ceil(random_vid/4), random_vid))
                    number_digit_qcm.append(random.randint(ceil(random_QCM/2), random_QCM))
                    number_digit_exam.append(random.randint(ceil(random_exam/4), random_exam))

        else :
            duration_digit_video.append(0)
            duration_digit_qcm.append(0)
            duration_digit_exam.append(0)
            number_digit_video.append(0)
            number_digit_qcm.append(0)
            number_digit_exam.append(0)

        if pres > 0:
            while pres != 0:
                random_lecture = random.randint(0, ceil(pres*0.75))
                random_exercise =  random.randint(0, ceil(pres*0.40))
                if pres <= 10:
                    random_exam = random.randint(0, 1)
                elif (pres > 10) and (pres <= 20):
                    random_exam = random.randint(0, 2)
                else:
                    random_exam = random.randint(0, 3)
                
                pres = pres - (random_lecture + random_exercise + random_exam)

                if pres != 0:
                    pres = pres + random_lecture + random_exercise + random_exam
                elif random_exercise <= random_exam:
                    pres = pres + random_lecture + random_exercise + random_exam
                elif random_lecture < random_exam:
                    pres = pres + random_lecture + random_exercise + random_exam
                elif pres == 0:
                    duration_present_lecture.append(random_lecture)
                    duration_present_exercise.append(random_exercise)
                    duration_present_exam.append(random_exam)
                    number_present_lecture.append(random.randint(ceil(random_lecture/4), random_lecture))
                    number_present_exercise.append(random.randint(ceil(random_exercise/2), random_exercise))
                    number_present_exam.append(random.randint(ceil(random_exam/4), random_exam))

        else:
            duration_present_lecture.append(0)
            duration_present_exercise.append(0)
            duration_present_exam.append(0)
            number_present_lecture.append(0)
            number_present_exercise.append(0)
            number_present_exam.append(0)

    else:
        ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        nw_digit = digit - Course_PerYear['Course_Digit'].iloc[ins[-1]]
        if nw_digit == 0:
            duration_digit_video.append(duration_digit_video[ins[-1]])
            duration_digit_qcm.append(duration_digit_qcm[ins[-1]])
            duration_digit_exam.append(duration_digit_exam[ins[-1]])

            duration_present_lecture.append(duration_present_lecture[ins[-1]])
            duration_present_exercise.append(duration_present_exercise[ins[-1]])
            duration_present_exam.append(duration_present_exam[ins[-1]])

            number_digit_video.append(number_digit_video[ins[-1]])
            number_digit_qcm.append(number_digit_qcm[ins[-1]])
            number_digit_exam.append(number_digit_exam[ins[-1]])

            number_present_lecture.append(number_present_lecture[ins[-1]])
            number_present_exercise.append(number_present_exercise[ins[-1]])
            number_present_exam.append(number_present_exam[ins[-1]])


        else:
            if course_ID in banned_id:
                break 
            else:
                count = 200
                while (nw_digit > 0 and count > 0):
                    count = count - 1
                    random_vid = 0
                    random_QCM = 0 
                    random_exam = 0
                    if duration_present_lecture[ins[-1]] > 0:
                        random_vid = random.randint(0, duration_present_lecture[ins[-1]])
                    if duration_present_exercise[ins[-1]] > 0:
                        random_QCM = random.randint(0, duration_present_exercise[ins[-1]])   
                    if duration_present_exam[ins[-1]] > 0:
                        random_exam = random.randint(0, duration_present_exam[ins[-1]])

                    nw_digit = nw_digit - (random_vid + random_QCM + random_exam)
                    num_vid = random.randint(ceil(random_vid/4), random_vid)
                    num_qcm = random.randint(ceil(random_QCM/2), random_QCM)
                    num_exam = random.randint(ceil(random_exam/4), random_exam)

                    if (nw_digit != 0):
                        nw_digit = nw_digit + random_vid + random_QCM + random_exam

                    else:
                        if (number_present_lecture[ins[-1]] - num_vid < 0) or ((number_present_lecture[ins[-1]] - num_vid == 0) and (duration_present_lecture[ins[-1]] - random_vid > 0)):
                            nw_digit = nw_digit + random_vid + random_QCM + random_exam
                        elif (number_present_exercise[ins[-1]] - num_qcm < 0) or (number_present_exercise[ins[-1]] - num_qcm== 0) and (duration_present_exercise[ins[-1]] - random_QCM > 0):
                            nw_digit = nw_digit + random_vid + random_QCM + random_exam
                        elif (number_present_exam[ins[-1]] - num_exam < 0) or (number_present_exam[ins[-1]] - num_exam == 0) and (duration_present_exam[ins[-1]] - random_exam > 0):    
                            nw_digit = nw_digit + random_vid + random_QCM + random_exam

                        else:
                            duration_digit_video.append(duration_digit_video[ins[-1]] + random_vid)
                            duration_digit_qcm.append(duration_digit_qcm[ins[-1]] + random_QCM)
                            duration_digit_exam.append(duration_digit_exam[ins[-1]] + random_exam)
                            duration_present_lecture.append(duration_present_lecture[ins[-1]] - random_vid)
                            duration_present_exercise.append(duration_present_exercise[ins[-1]] - random_QCM)
                            duration_present_exam.append(duration_present_exam[ins[-1]] - random_exam)
                        
                            number_digit_video.append(number_digit_video[ins[-1]] + num_vid)
                            number_digit_qcm.append(number_digit_qcm[ins[-1]] + num_qcm)
                            number_digit_exam.append(number_digit_exam[ins[-1]] + num_exam)

                            number_present_lecture.append(number_present_lecture[ins[-1]] - num_vid)
                            number_present_exercise.append(number_present_exercise[ins[-1]] - num_qcm)
                            number_present_exam.append(number_present_exam[ins[-1]] - num_exam)
                
                    if count == 0:
                        banned_id.append(course_ID)
                        for ind in ins:
                            duration_digit_qcm[ind] = 'Not-Working' 
                            duration_digit_qcm[ind] = 'Not-Working' 
                            duration_digit_exam[ind] = 'Not-Working' 
                            duration_present_lecture[ind] = 'Not-Working' 
                            duration_present_exercise[ind] = 'Not-Working' 
                            duration_present_exam[ind] = 'Not-Working' 
                        
                            number_digit_video[ind] = 'Not-Working' 
                            number_digit_qcm[ind] = 'Not-Working' 
                            number_digit_exam[ind] = 'Not-Working' 

                            number_present_lecture[ind] = 'Not-Working' 
                            number_present_exercise[ind] = 'Not-Working' 
                            number_present_exam[ind] = 'Not-Working' 

    temp_ID.append(course_ID)

print(len(banned_id)/len(Course_PerYear['Course_ID'].unique()) * 100)

Course_df = Course_PerYear[['Year', 'Course_ID', 'Course_Duration']]
Course_df = pd.DataFrame({
    'Year': Course_PerYear['Year'],
    'Course_ID': Course_PerYear['Course_ID'],
    'Course_Duration': Course_PerYear['Course_Duration'],
    'Course_Digit': Course_PerYear['Course_Digit'],
    'Duration_Digit_Video': duration_digit_video,
    'Number_Digit_Video': number_digit_video,
    'Duration_Digit_QCM': duration_digit_qcm,
    'Number_Digit_QCM': number_digit_qcm,
    'Duration_Digit_Exam': duration_digit_exam,
    'Number_Digit_Exam': number_digit_exam,
    'Number_Digit_Ressources': [number_digit_video[i] + number_digit_qcm[i] + number_digit_exam[i] for i in range(len(Course_PerYear))],
    'Course_Present': Course_PerYear['Course_Present'],
    'Duration_Pres_Lecture': duration_present_lecture,
    'Number_Pres_Lecture': number_present_lecture,
    'Duration_Pres_Exercise': duration_present_exercise,
    'Number_Pres_Exercise': number_present_exercise,
    'Duration_Pres_Exam': duration_present_exam,
    'Number_Pres_Exam': number_present_exam,
    'Number_Pres_Ressources': [number_present_lecture[i] + number_present_exercise[i] + number_present_exam[i] for i in range(len(Course_PerYear))],
    'Total Ressources': [((dig_vid + dig_qcm + dig_exam) + (pres_lec + pres_exer + pres_exam)) for dig_vid, dig_qcm, dig_exam, pres_lec, pres_exer, pres_exam in zip(number_digit_video, number_digit_qcm, number_digit_exam, number_present_lecture, number_present_exercise, number_present_exam)]
})

print(Course_df)

####################################
# Factice Ressources Sequence Data #
####################################

def Prep_Seq(rng1, rng2, string):
    temp_seq = []
    rng = rng1 - rng2
    for l in range(rng):
        temp_seq.append(string)
    return(temp_seq)

def pos(array, str_array):
    index_exam = [i for i in range(len(array)) if array[i] in str_array]   #Find the index of the identical ID as the current «course» selected ID.    
    if len(index_exam) == 0:
        return array
        
    if len(index_exam) == 1:
        nw_position = len(array) -1
        old_position = index_exam[0]
        value_exchange = array[nw_position]
        array[nw_position] = array[old_position]
        array[old_position] = value_exchange
    elif len(index_exam) > 1:
        for index, i in zip(index_exam, range(1, len(index_exam)+1)):
            nw_position = round(((len(array) - 1)*i)/len(index_exam))
            old_position = index
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
#
Sequence_Course = Course_df

#Advanced/Basic Sequence Lists
basic_SeqJoint = []   #Basic List containing the sequence joint of each course

#Temporary ID:
temp_ID = []

#Loop 
for seq, course_ID in zip(range(0, len(Sequence_Course)), Sequence_Course['Course_ID']):
    if course_ID in temp_ID:
        ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        basic_SeqJoint_INS = [basic_SeqJoint[ins[-1]]]
        basic_SeqJoint_INS = basic_SeqJoint_INS[0].split('-')

        #Digit
        rng_digit_vid = Sequence_Course['Number_Digit_Video'].iloc[ins[-1]]
        rng_digit_QCM = Sequence_Course['Number_Digit_QCM'].iloc[ins[-1]]
        rng_digit_exam = Sequence_Course['Number_Digit_Exam'].iloc[ins[-1]]

    else: 
        rng_digit_vid = rng_digit_QCM = rng_digit_exam = 0
        rng_pres_lect = rng_pres_exer = rng_pres_exam = 0

    Digit_VidTemp = Prep_Seq(Sequence_Course['Number_Digit_Video'].iloc[seq], rng_digit_vid, 'Video')
    Digit_QCMTemp = Prep_Seq(Sequence_Course['Number_Digit_QCM'].iloc[seq], rng_digit_QCM, 'QCM')
    Digit_ExamTemp = Prep_Seq(Sequence_Course['Number_Digit_Exam'].iloc[seq], rng_digit_exam, 'Digit_Exam')

    if course_ID in temp_ID: 
        #Basic List
        basic_SeqTemp = swap(basic_SeqJoint_INS, Digit_VidTemp, 'Lecture')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_QCMTemp, 'Exercise')
        basic_SeqTemp = swap(basic_SeqTemp, Digit_ExamTemp, 'Presentiel_Exam')

        if basic_SeqJoint_INS == ['']:
            basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        else:
                basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
            
        basic_SeqJoint.append(basic_Seq_tempJoint)

    else:
        #Presentiel
        rng_pres_lect = 0
        rng_pres_exer = 0
        rng_pres_exam = 0
        Pres_LectTemp = Prep_Seq(Sequence_Course['Number_Pres_Lecture'].iloc[seq], rng_pres_lect, 'Lecture')
        Pres_ExerTemp = Prep_Seq(Sequence_Course['Number_Pres_Exercise'].iloc[seq], rng_pres_exer, 'Exercise')
        Pres_ExamTemp = Prep_Seq(Sequence_Course['Number_Pres_Exam'].iloc[seq], rng_pres_exam, 'Presentiel_Exam')

        #Basic List
        basic_SeqTemp = Digit_VidTemp + Digit_QCMTemp + Digit_ExamTemp + Pres_LectTemp + Pres_ExerTemp + Pres_ExamTemp
        random.shuffle(basic_SeqTemp)
        basic_SeqTemp = pos(basic_SeqTemp, ['Digit_Exam', 'Presentiel_Exam'])
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)
        
        temp_ID.append(course_ID)

Sequence_Course['Sequence'] = basic_SeqJoint


#######################
# Preparing Sequences #
#######################

list_Course_ID = []
list_Course_Year = [] 
list_Duration = []
list_Digit_Duration = []
list_Pres_Duration = []
list_Ressources = []
list_Count = []
list_BasicSeq = []

for num in range(len(Sequence_Course)):
    count = 1
    list_basic = Sequence_Course.iloc[num]['Sequence'].split("-")
    for basic in list_basic:
        list_Course_ID.append(Sequence_Course.iloc[num]['Course_ID'])
        list_Course_Year.append(Sequence_Course.iloc[num]['Year'])
        list_Duration.append(Sequence_Course.iloc[num]['Course_Duration'])
        list_Digit_Duration.append(Sequence_Course.iloc[num]['Course_Digit'])
        list_Pres_Duration.append(Sequence_Course.iloc[num]['Course_Present'])
        list_Ressources.append(Sequence_Course.iloc[num]['Total Ressources'])
        list_Count.append(count) 
        list_BasicSeq.append(basic)
        count += 1

Prepared_Sequence = pd.DataFrame({'Course_ID': list_Course_ID,
              'Year': list_Course_Year,
              'Course_Duration': list_Duration,
              'Course_Digit_Duration': list_Digit_Duration,
              'Course_Pres_Duration': list_Pres_Duration,
              'Ressources_Amount': list_Ressources,
              'Ressources_Rank': list_Count,
              'Ressources_Type_Basic': list_BasicSeq,
})


#############
# Save Data #
#############

#Save the «Prepared_Sequence» into a CSV File.
Course_df.to_csv(path_data + 'Ressources.csv')

#Save the «Sequence_Course» into a CSV file.
Sequence_Course.to_csv(path_data + 'Ressources_Sequences.csv')

#Save the «Prepared_Sequence» into a CSV File.
Prepared_Sequence.to_csv(path_data + 'Prepared_Sequences.csv')


#########################
# Data Preparation DONE #
#########################
