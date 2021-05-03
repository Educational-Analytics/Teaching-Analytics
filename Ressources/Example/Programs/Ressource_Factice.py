###########################################
# Ressource par Cours par Année (Factice) #        
###########################################

#Import the required packages
from math import *
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt

#Set a seed to keep the same values randomly defined after each execution.
seed( 2000 )

#################################
# Import the required Data file #
#################################

#Import the dataframe
Course_PerYear = pd.read_csv('Digitalization/Example/Data/Digitalization.csv')

#Drop the first column of the dataframe (empty)
Course_PerYear = Course_PerYear.iloc[: , 1:]

###
# Function

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

Course_PerYear.to_csv('Ressources/Example/Data/Ressources.csv')


"""
####################################
# Factice Ressources Sequence Data #
####################################
Sequence_Course = Course_PerYear

#Basic Sequence Lists
bas_seq = []         #Basic List containing the sequence of each course
bas_seq_joint = []   #Basic List containing the sequence joint of each course

#Advanced Sequence Lists
adv_seq = []         #Advanced List containing the sequence of each course
adv_seq_joint = []   #Advanced List containing the sequence joint of each course

#Loop 
for course in range(len(Sequence_Course)):
    bas_seq_temp = []
    adv_seq_temp = []
    for vid in range(Sequence_Course['Number_Video'].iloc[course]):
        bas_seq_temp.append('Vid')
    for vid1H in range(Sequence_Course['Number_Video_1H'].iloc[course]):
        adv_seq_temp.append('Vid1H')
    for vid2H in range(Sequence_Course['Number_Video_2H'].iloc[course]):
        adv_seq_temp.append('Vid2H')
    for vid3H in range(Sequence_Course['Number_Video_3H'].iloc[course]):
        adv_seq_temp.append('Vid3H')
    for vid4H in range(Sequence_Course['Number_Video_4H'].iloc[course]):
        adv_seq_temp.append('Vid4H')

    for quiz in range(Sequence_Course['Number_Quiz'].iloc[course]):
        bas_seq_temp.append('Quiz')
    for quiz1H in range(Sequence_Course['Number_Quiz_1H'].iloc[course]):
        adv_seq_temp.append('Quiz1H')
    for quiz2H in range(Sequence_Course['Number_Quiz_2H'].iloc[course]):
        adv_seq_temp.append('Quiz2H')

    for exam in range(Sequence_Course['Number_Exam'].iloc[course]):
        bas_seq_temp.append('Exam')
    for exam1H in range(Sequence_Course['Number_Exam_1H'].iloc[course]):
        adv_seq_temp.append('Exam1H')
    for exam2H in range(Sequence_Course['Number_Exam_2H'].iloc[course]):
        adv_seq_temp.append('Exam2H')
    for exam3H in range(Sequence_Course['Number_Exam_3H'].iloc[course]):
        adv_seq_temp.append('Exam3H')
    for exam4H in range(Sequence_Course['Number_Exam_4H'].iloc[course]):
        adv_seq_temp.append('Exam4H')


    random.shuffle(bas_seq_temp)
    bas_seq_temp_joint = '-'.join(bas_seq_temp)
    bas_seq.append(bas_seq_temp)
    bas_seq_joint.append(bas_seq_temp_joint)

    random.shuffle(adv_seq_temp)
    adv_seq_temp_joint = '-'.join(adv_seq_temp)
    adv_seq.append(adv_seq_temp)
    adv_seq_joint.append(adv_seq_temp_joint)

Sequence_Course['Basic_Sequence'] = bas_seq_joint
Sequence_Course['Advanced_Sequence'] = adv_seq_joint

col = ['Course_ID', 'Year', 'Course_Duration', 'Course_Digit', 'Number_Ressources', 'Number_Video', 'Number_Quiz', 'Number_Exam', 'Basic_Sequence', 'Advanced_Sequence']
Sequences = Sequence_Course[col]

#############
# Save Data #
#############

#Save the dataframe into a CSV file
Sequence_Course.to_csv('Ressources/Example/Data/Ressources_Sequences.csv')

#Save the dataframe into a CSV file
Sequences.to_csv('Ressources/Example/Data/Sequences.csv')

#######################
# Preparing Sequences #
#######################

Sequence_8_30 = Sequences[(Sequences['Course_Digit'].between(8, 30))]
Sequences_8_30 = Sequence_8_30[['Course_ID', 'Year', 'Course_Digit', 'Number_Ressources', 'Basic_Sequence', 'Advanced_Sequence']]

#Fast Way
list_Course_ID = []
list_Course_Year = [] 
list_Digit_Duration = []
list_Ressources = []
list_Count = []
list_BasicSeq = []
list_AdvancedSeq = []

for num in range(len(Sequences_8_30)):
    count = 1
    list_basic = Sequences_8_30.iloc[num]['Basic_Sequence'].split("-")
    list_advanced = Sequences_8_30.iloc[num]['Advanced_Sequence'].split("-")
    for basic,advanced in zip(list_basic, list_advanced):
        list_Course_ID.append(Sequences_8_30.iloc[num]['Course_ID'])
        list_Course_Year.append(Sequences_8_30.iloc[num]['Year'])
        list_Digit_Duration.append(Sequence_8_30.iloc[num]['Course_Digit'])
        list_Ressources.append(Sequences_8_30.iloc[num]['Number_Ressources'])
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
"""
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
"""
#############
# Save Data #
#############

#Save the dataframe into a CSV file
Prepared_Sequence.to_csv('Ressources/Example/Data/Prepared_Sequences.csv')
"""