###########################################
# Ressource par Cours par Année (Factice) #        
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

def Video_Times(dv, nv, array_video, ins):
    if (dv == 0 or nv == 0):
        array_v = array_video[ins[-1]]
    else:
        array = []
        for i in range(0, nv+1):
            for j in range(0, nv+1):
                for k in range(0, nv+1):
                    for l in range(0, nv+1):
                        if dv == (1*i + 2*j + 3*k + 4*l) and nv == (i + j + k + l):
                            array.append([i,j,k,l])
        if len(array) == 1:
            array_v = [array[0][0] + array_video[ins[-1]][0], array[0][1] + array_video[ins[-1]][1], array[0][2] + array_video[ins[-1]][2], array[0][3] + array_video[ins[-1]][3]]
        elif len(array) == 0:
            array_v = array_video[ins[-1]]
        else:
            ran = random.randint(0, len(array)-1)
            array_v = [array[ran][0] + array_video[ins[-1]][0], array[ran][1] + array_video[ins[-1]][1], array[ran][2] + array_video[ins[-1]][2], array[ran][3] + array_video[ins[-1]][3]]
    return(array_v)


def Quizz_Times(dq, nq, array_quizz, ins):
    if (dq == 0 or nq == 0):
        array_q = array_quizz[ins[-1]]
    else:
        array = []
        for i in range(0, nq+1):
            for j in range(0, nq+1):
                for k in range(0, nq+1):
                    for l in range(0, nq+1):
                        if dq == (1*i + 2*j) and nq == (i + j):
                            array.append([i,j])
        if len(array) == 1:
            array_q = [array[0][0] + array_quizz[ins[-1]][0], array[0][1] + array_quizz[ins[-1]][1]]
        elif len(array) == 0:
            array_q = array_quizz[ins[-1]]
        else:
            ran = random.randint(0, len(array)-1)
            array_q = [array[ran][0] + array_quizz[ins[-1]][0], array[ran][1] + array_quizz[ins[-1]][1]]
    return(array_q)


def Exam_Times(de, ne, array_exam, ins):
    if (de == 0 or ne == 0):
        array_e = array_exam[ins[-1]]
    else:
        array = []
        for i in range(0, ne+1):
            for j in range(0, ne+1):
                for k in range(0, ne+1):
                    for l in range(0, ne+1):
                        if de == (1*i + 2*j + 3*k + 4*l) and ne == (i + j + k + l):
                            array.append([i,j,k,l])
        if len(array) == 1:
            array_e = [array[0][0] + array_exam[ins[-1]][0], array[0][1] + array_exam[ins[-1]][1], array[0][2] + array_exam[ins[-1]][2], array[0][3] + array_exam[ins[-1]][3]]
        elif len(array) == 0:
            array_e = array_exam[ins[-1]]
        else:
            ran = random.randint(0, len(array)-1)
            array_e = [array[ran][0] + array_exam[ins[-1]][0], array[ran][1] + array_exam[ins[-1]][1], array[ran][2] + array_exam[ins[-1]][2], array[ran][3] + array_exam[ins[-1]][3]]

    return(array_e)


def Prep_Seq(rng1, rng2, string):
    temp_seq = []
    rng = rng1 - rng2
    for l in range(rng):
        temp_seq.append(string)
    return(temp_seq)


#################################
# Import the required Data file #
#################################

#Import the dataframe
Course_PerYear = pd.read_csv(path_data + 'Digitalization.csv')

#Drop the first column of the dataframe (empty)
Course_PerYear = Course_PerYear.iloc[: , 1:]

######################################
# Factice Ressources Additional Data #
######################################

list_rv = []
list_rq = []
list_re = []

list_nb_rv = []
list_nb_rq = []
list_nb_re = []

array_video = [] 
array_quizz = []
array_exam = []

temp_ID = []
for (ress, course_ID) in zip(Course_PerYear['Course_Digit'], Course_PerYear['Course_ID']):
    if ress > 0:
        if course_ID in temp_ID:
            ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
            nw_ress = abs(ress - Course_PerYear['Course_Digit'][ins[-1]])
            if nw_ress == 0:
                list_rv.append(list_rv[ins[-1]])
                list_rq.append(list_rq[ins[-1]])
                list_re.append(list_re[ins[-1]])

                list_nb_rv.append(list_nb_rv[ins[-1]])
                list_nb_rq.append(list_nb_rq[ins[-1]])
                list_nb_re.append(list_nb_re[ins[-1]])

                array_video.append(array_video[ins[-1]])
                array_quizz.append(array_quizz[ins[-1]])
                array_exam.append(array_exam[ins[-1]])

            else:
                while nw_ress > 0:
                    random_vid = round(random.uniform(0, nw_ress*0.75))
                    random_quiz = round(random.uniform(0, nw_ress*0.60))
                    random_exam = round(random.uniform(0, 4))
                    nw_ress = nw_ress - (random_vid + random_quiz + random_exam) 
                    if nw_ress != 0:
                        nw_ress = nw_ress + random_vid + random_quiz + random_exam
                    elif random_quiz <= random_exam:
                        nw_ress = nw_ress + random_vid + random_quiz + random_exam
                    elif random_vid < random_exam:
                        nw_ress = nw_ress + random_vid + random_quiz + random_exam
                    elif nw_ress == 0:
                        list_rv.append(list_rv[ins[-1]] + random_vid)
                        list_rq.append(list_rq[ins[-1]] + random_quiz)
                        list_re.append(list_re[ins[-1]] + random_exam)
                        list_nb_rv.append(list_nb_rv[ins[-1]] + round(random.randint(ceil(random_vid/4), random_vid)))
                        list_nb_rq.append(list_nb_rq[ins[-1]] + round(random.randint(ceil(random_quiz/2), random_quiz)))
                        list_nb_re.append(list_nb_re[ins[-1]] + round(random.randint(ceil(random_exam/4), random_exam)))

                        dv = list_rv[-1] - list_rv[ins[-1]]
                        nv = list_nb_rv[-1] - list_nb_rv[ins[-1]]
                        array_video.append(Video_Times(dv, nv, array_video, ins))

                        dq = list_rq[-1] - list_rq[ins[-1]]
                        nq = list_nb_rq[-1] - list_nb_rq[ins[-1]]
                        array_quizz.append(Quizz_Times(dq, nq, array_quizz, ins))

                        de = list_re[-1] - list_re[ins[-1]]
                        ne = list_nb_re[-1] - list_nb_re[ins[-1]]
                        array_exam.append(Exam_Times(de, ne, array_exam, ins))

        else:
            while ress > 0:
                random_vid = round(random.uniform(0, ress*0.75))
                random_quiz = round(random.uniform(0, ress*0.60))
                random_exam = round(random.uniform(0, 4))
                ress = ress - (random_vid + random_quiz + random_exam) 
                if ress != 0:
                    ress = ress + random_vid + random_quiz + random_exam
                elif random_quiz <= random_exam:
                    ress = ress + random_vid + random_quiz + random_exam
                elif random_vid < random_exam:
                    ress = ress + random_vid + random_quiz + random_exam
                elif ress == 0:
                    list_rv.append(random_vid)
                    list_rq.append(random_quiz)
                    list_re.append(random_exam)

                    list_nb_rv.append(round(random.randint(ceil(random_vid/4), random_vid)))      
                    list_nb_rq.append(round(random.randint(ceil(random_quiz/2), random_quiz)))
                    list_nb_re.append(round(random.randint(ceil(random_exam/4), random_exam)))

                    dv = list_rv[-1]
                    nv = list_nb_rv[-1]
                    if (dv == 0 or nv == 0):
                        array_video.append([0,0,0,0])
                    else:
                        array = []
                        for i in range(0, nv+1):
                            for j in range(0, nv+1):
                                for k in range(0, nv+1):
                                    for l in range(0,nv+1):
                                        if dv == (1*i + 2*j + 3*k + 4*l) and nv == (i + j + k + l):
                                            array.append([i,j,k,l])
                        if len(array) == 1:
                            array_video.append(array[0])
                        elif len(array) == 0:
                            array_video.append([0,0,0,0])
                        else:
                            ran = random.randint(0, len(array)-1)
                            array_video.append(array[ran])

                    dq = list_rq[-1]
                    nq = list_nb_rq[-1]
                    if (dq == 0 or nq == 0):
                        array_quizz.append([0,0])
                    else:
                        array = []
                        for i in range(0, nq+1):
                            for j in range(0, nq+1):
                                if dq == (1*i + 2*j) and nq == (i + j):
                                    array.append([i,j])
                        if len(array) == 1:
                            array_quizz.append(array[0])
                        elif len(array) == 0:
                            array_quizz.append([0,0])
                        else:
                            ran = random.randint(0, len(array)-1)
                            array_quizz.append(array[ran])
                  
                    de = list_re[-1]
                    ne = list_nb_re[-1]
                    if (de == 0 or ne == 0):
                        array_exam.append([0,0,0,0])
                    else:
                        array = []
                        for i in range(0, ne+1):
                            for j in range(0, ne+1):
                                for k in range(0, ne+1):
                                    for l in range(0,ne+1):
                                        if de == (1*i + 2*j + 3*k + 4*l) and ne == (i + j + k + l):
                                            array.append([i,j,k,l])
                        if len(array) == 1:
                            array_exam.append(array[0])
                        elif len(array) == 0:
                            array_exam.append([0,0,0,0])
                        else:
                            ran = random.randint(0, len(array)-1)
                            array_exam.append(array[ran])

    else:
        list_rv.append(0)
        list_rq.append(0)
        list_re.append(0)
        list_nb_rv.append(0)      
        list_nb_rq.append(0)
        list_nb_re.append(0)
        array_video.append([0,0,0,0])
        array_quizz.append([0,0])
        array_exam.append([0,0,0,0])


    temp_ID.append(course_ID)


Course_PerYear['Duration_Video'] = list_rv
Course_PerYear['Duration_Quiz'] = list_rq
Course_PerYear['Duration_Exam'] = list_re
Course_PerYear['Number_Video'] = list_nb_rv
Course_PerYear['Number_Quiz'] = list_nb_rq
Course_PerYear['Number_Exam'] = list_nb_re
Course_PerYear['Number_Ressources'] =  [list_nb_rv[i] + list_nb_rq[i] + list_nb_re[i] for i in range(len(list_nb_re))]


Course_PerYear['Number_Video_1H'] = [array_video[i][0] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_2H'] = [array_video[i][1] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_3H'] = [array_video[i][2] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_4H'] = [array_video[i][3] for i in range(0, len(array_video))]

Course_PerYear['Number_Quiz_1H'] = [array_quizz[i][0] for i in range(0, len(array_quizz))]
Course_PerYear['Number_Quiz_2H'] = [array_quizz[i][1] for i in range(0, len(array_quizz))]


Course_PerYear['Number_Exam_1H'] = [array_exam[i][0] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_2H'] = [array_exam[i][1] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_3H'] = [array_exam[i][2] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_4H'] = [array_exam[i][3] for i in range(0, len(array_exam))]


#print(Course_PerYear[['Course_ID', 'Year', 'Duration_Video', 'Number_Video', 'Number_Video_1H', 'Number_Video_2H', 'Number_Video_3H', 'Number_Video_4H']].sort_values(by = ['Course_ID', 'Year'], ascending = True).head(10))
#print(Course_PerYear[['Course_ID', 'Year', 'Duration_Quiz', 'Number_Quiz', 'Number_Quiz_1H', 'Number_Quiz_2H']].sort_values(by = ['Course_ID', 'Year'], ascending = True).head(10))
#print(Course_PerYear[['Course_ID', 'Year', 'Duration_Exam', 'Number_Exam', 'Number_Exam_1H', 'Number_Exam_2H', 'Number_Exam_3H', 'Number_Exam_4H']].sort_values(by = ['Course_ID', 'Year'], ascending = True).head(10))


####################################
# Factice Ressources Sequence Data #
####################################

#Import the dataframe
Sequence_Course = Course_PerYear

#Advanced/Basic Sequence Lists
basic_SeqJoint = []   #Basic List containing the sequence joint of each course
advanced_SeqJoint = []   #Advanced List containing the sequence joint of each course

#Temporary ID:
temp_ID = []
seqts = []
#Loop 
for seq, course_ID in zip(range(0, len(Sequence_Course)), Sequence_Course['Course_ID']):

    if course_ID in temp_ID:
        ins = [courses for courses in range(0, len(temp_ID)) if temp_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        basic_SeqJoint_INS = [basic_SeqJoint[ins[-1]]]
        advanced_SeqJoint_INS = [advanced_SeqJoint[ins[-1]]]

        #Video
        rng_2_vid = Sequence_Course['Number_Video'].iloc[ins[-1]]
        rng_2_vid_1H = Sequence_Course['Number_Video_1H'].iloc[ins[-1]]
        rng_2_vid_2H = Sequence_Course['Number_Video_2H'].iloc[ins[-1]]
        rng_2_vid_3H = Sequence_Course['Number_Video_3H'].iloc[ins[-1]]
        rng_2_vid_4H = Sequence_Course['Number_Video_4H'].iloc[ins[-1]]

        #Quizz
        rng_2_quizz = Sequence_Course['Number_Quiz'].iloc[ins[-1]]
        rng_2_quizz_1H = Sequence_Course['Number_Quiz_1H'].iloc[ins[-1]]
        rng_2_quizz_2H = Sequence_Course['Number_Quiz_2H'].iloc[ins[-1]]

        #Exam
        rng_2_exam = Sequence_Course['Number_Exam'].iloc[ins[-1]]
        rng_2_exam_1H = Sequence_Course['Number_Exam_1H'].iloc[ins[-1]]
        rng_2_exam_2H = Sequence_Course['Number_Exam_2H'].iloc[ins[-1]]
        rng_2_exam_3H = Sequence_Course['Number_Exam_3H'].iloc[ins[-1]]
        rng_2_exam_4H = Sequence_Course['Number_Exam_4H'].iloc[ins[-1]]

    else: 
        rng_2_vid = rng_2_vid_1H = rng_2_vid_2H = rng_2_vid_3H = rng_2_vid_4H = 0
        rng_2_quizz = rng_2_quizz_1H = rng_2_quizz_2H = 0
        rng_2_exam = rng_2_exam_1H = rng_2_exam_2H = rng_2_exam_3H = rng_2_exam_4H = 0

    #Video
    basic_VidTemp = Prep_Seq(Sequence_Course['Number_Video'].iloc[seq], rng_2_vid, 'Vid')
    advanced_VidTemp_1H = Prep_Seq(Sequence_Course['Number_Video_1H'].iloc[seq], rng_2_vid_1H, 'Vid1H')
    advanced_VidTemp_2H = Prep_Seq(Sequence_Course['Number_Video_2H'].iloc[seq], rng_2_vid_2H, 'Vid2H')
    advanced_VidTemp_3H = Prep_Seq(Sequence_Course['Number_Video_3H'].iloc[seq], rng_2_vid_3H, 'Vid3H')
    advanced_VidTemp_4H = Prep_Seq(Sequence_Course['Number_Video_4H'].iloc[seq], rng_2_vid_4H, 'Vid4H')

    #Quizz
    basic_QuizzTemp = Prep_Seq(Sequence_Course['Number_Quiz'].iloc[seq], rng_2_quizz, 'Quizz')
    advanced_QuizzTemp_1H = Prep_Seq(Sequence_Course['Number_Quiz_1H'].iloc[seq], rng_2_quizz_1H, 'Quizz1H')
    advanced_QuizzTemp_2H = Prep_Seq(Sequence_Course['Number_Quiz_2H'].iloc[seq], rng_2_quizz_2H, 'Quizz2H')

    #Exam
    basic_ExamTemp = Prep_Seq(Sequence_Course['Number_Exam'].iloc[seq], rng_2_exam, 'Exam')
    advanced_ExamTemp_1H = Prep_Seq(Sequence_Course['Number_Exam_1H'].iloc[seq], rng_2_exam_1H, 'Exam1H')
    advanced_ExamTemp_2H = Prep_Seq(Sequence_Course['Number_Exam_2H'].iloc[seq], rng_2_exam_2H, 'Exam2H')
    advanced_ExamTemp_3H = Prep_Seq(Sequence_Course['Number_Exam_3H'].iloc[seq], rng_2_exam_3H, 'Exam3H')
    advanced_ExamTemp_4H = Prep_Seq(Sequence_Course['Number_Exam_4H'].iloc[seq], rng_2_exam_4H, 'Exam4H')
 

    if course_ID in temp_ID: 
        #Basic List
        basic_SeqTemp = basic_VidTemp + basic_QuizzTemp + basic_ExamTemp
        random.shuffle(basic_SeqTemp)
        basic_Seq_tempJoint = '-'.join(basic_SeqJoint_INS + basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)

        
        
        #Advanced List
        advanced_Vid = advanced_VidTemp_1H + advanced_VidTemp_2H + advanced_VidTemp_3H + advanced_VidTemp_4H
        advanced_Quizz = advanced_QuizzTemp_1H + advanced_QuizzTemp_2H
        advanced_Exam = advanced_ExamTemp_1H + advanced_ExamTemp_2H + advanced_ExamTemp_3H + advanced_ExamTemp_4H
        advanced_SeqTemp_Initial = advanced_Vid + advanced_Quizz + advanced_Exam

        advanced_SeqTemp = []
        for bsc_seq in basic_SeqTemp:
            if bsc_seq == 'Vid':
                ran_vid = random.randint(0, len(advanced_Vid)-1)
                advanced_SeqTemp.append(advanced_Vid[ran_vid])
                advanced_Vid.pop(ran_vid)

            if bsc_seq == 'Quizz':
                ran_quizz = random.randint(0, len(advanced_Quizz)-1)
                advanced_SeqTemp.append(advanced_Quizz[ran_quizz])
                advanced_Quizz.pop(ran_quizz)

            if bsc_seq == 'Exam':
                ran_exam = random.randint(0, len(advanced_Exam)-1)
                advanced_SeqTemp.append(advanced_Exam[ran_exam])
                advanced_Exam.pop(ran_exam)

        advanced_Seq_tempJoint = '-'.join(advanced_SeqJoint_INS + advanced_SeqTemp)
        advanced_SeqJoint.append(advanced_Seq_tempJoint)
    

    else:
        #Basic List
        basic_SeqTemp = basic_VidTemp + basic_QuizzTemp + basic_ExamTemp
        random.shuffle(basic_SeqTemp)
        basic_Seq_tempJoint = '-'.join(basic_SeqTemp)
        basic_SeqJoint.append(basic_Seq_tempJoint)
        
        #Advanced List
        advanced_Vid = advanced_VidTemp_1H + advanced_VidTemp_2H + advanced_VidTemp_3H + advanced_VidTemp_4H
        advanced_Quizz = advanced_QuizzTemp_1H + advanced_QuizzTemp_2H
        advanced_Exam = advanced_ExamTemp_1H + advanced_ExamTemp_2H + advanced_ExamTemp_3H + advanced_ExamTemp_4H
        advanced_SeqTemp_Initial = advanced_Vid + advanced_Quizz + advanced_Exam
        
        advanced_SeqTemp = []
        for bsc_seq in basic_SeqTemp:
            if bsc_seq == 'Vid':
                ran_vid = random.randint(0, len(advanced_Vid)-1)
                advanced_SeqTemp.append(advanced_Vid[ran_vid])
                advanced_Vid.pop(ran_vid)

            if bsc_seq == 'Quizz':
                ran_quizz = random.randint(0, len(advanced_Quizz)-1)
                advanced_SeqTemp.append(advanced_Quizz[ran_quizz])
                advanced_Quizz.pop(ran_quizz)

            if bsc_seq == 'Exam':
                ran_exam = random.randint(0, len(advanced_Exam)-1)
                advanced_SeqTemp.append(advanced_Exam[ran_exam])
                advanced_Exam.pop(ran_exam)

        advanced_Seq_tempJoint = '-'.join(advanced_SeqTemp)
        advanced_SeqJoint.append(advanced_Seq_tempJoint)

    temp_ID.append(course_ID)
    seqts.append(seq)


Sequence_Course['Basic_Sequence'] = basic_SeqJoint
Sequence_Course['Advanced_Sequence'] = advanced_SeqJoint

col = ['Course_ID', 'Year', 'Course_Duration', 'Course_Digit', 'Number_Ressources', 'Number_Video', 'Number_Quiz', 'Number_Exam', 'Basic_Sequence', 'Advanced_Sequence']
Sequences = Sequence_Course[col]


#######################
# Preparing Sequences #
#######################

#Sequence_8_30 = Sequences[(Sequences['Course_Digit'].between(8, 30))]
#Sequences_8_30 = Sequence_8_30[['Course_ID', 'Year', 'Course_Digit', 'Number_Ressources', 'Basic_Sequence', 'Advanced_Sequence']]

#Fast Way
list_Course_ID = []
list_Course_Year = [] 
list_Digit_Duration = []
list_Ressources = []
list_Count = []
list_BasicSeq = []
list_AdvancedSeq = []

for num in range(len(Sequences)):
    count = 1
    list_basic = Sequences.iloc[num]['Basic_Sequence'].split("-")
    list_advanced = Sequences.iloc[num]['Advanced_Sequence'].split("-")
    for basic,advanced in zip(list_basic, list_advanced):
        list_Course_ID.append(Sequences.iloc[num]['Course_ID'])
        list_Course_Year.append(Sequences.iloc[num]['Year'])
        list_Digit_Duration.append(Sequences.iloc[num]['Course_Digit'])
        list_Ressources.append(Sequences.iloc[num]['Number_Ressources'])
        list_Count.append(count) 
        list_BasicSeq.append(basic)
        list_AdvancedSeq.append(advanced)
        count += 1

Prepared_Sequence = pd.DataFrame({'Course_ID': list_Course_ID,
              'Year': list_Course_Year,
              'Course_Digit_Duration': list_Digit_Duration,
              'Ressources_Amount': list_Ressources,
              'Ressources_Rank': list_Count,
              'Ressources_Type_Basic': list_BasicSeq,
              'Ressources_Type_Advanced': list_AdvancedSeq,
})


#Esthetical Way
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

#############
# Save Data #
#############

#Save the «Prepared_Sequence» into a CSV File.
Prepared_Sequence.to_csv(path_data + 'Prepared_Sequences.csv')

#Save the «Course_PerYear» into a CSV File.
Course_PerYear.to_csv(path_data + 'Ressources.csv')

#Save the «Sequence_Course» into a CSV file.
Sequence_Course.to_csv(path_data + 'Ressources_Sequences.csv')

#Save the «Sequences» into a CSV file.
Sequences.to_csv(path_data + 'Sequences.csv')

#########################
# Data Preparation DONE #
#########################