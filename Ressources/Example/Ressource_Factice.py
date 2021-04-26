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

######################
# Factice Basic Data #
######################

#Create a list to represent the year interval (2013 to 2020).
list_years = [year for year in range(2013, 2021)]

#Create a list to represent the number of courses that a factice university teached for the year interval.
#Approximate to 1000 courses per year with 10% of maximal variation.
list_year_courses = [random.randint(1000*0.9, 1000*1.1) for year in list_years]

#Create a list that implemente the ID of each courses per year.
list_courses_ID = []
for num_courses in list_year_courses:
    course_ID = 1
    for i in range(0, num_courses):
        list_courses_ID.append(course_ID)
        course_ID += 1 

#Create lists.
temp_ID = [] #Temporary list to implemente the loop.
list_course_hrs = [] #List that represents the number of hours per course.
list_digit_ratio = []  #List that represents the digitalization ratio of each course.
list_digit_percent = [] #List that represents the digitalization percentage of each course.
list_duration_digit = [] #List that represents the duration of use of online ressources.
list_ress = [] #List that represents the number of online ressources.

#Create a loop to implement the above list (duration of each courses, duration using online ressources, number of online ressources).
for course in list_courses_ID:
    if course in temp_ID:  #In case the selected ID has been already set (for a previous year), we keep the same duration.
        rt = False #Set the variable to «False».
        ins = [cours_id for cours_id in range(len(temp_ID)) if temp_ID[cours_id] == course] #Find the index of the identical ID as the current «course» selected ID.

        #Create a while loop to compute the ratio/percentage of digitalization.
        while (rt == False): 
            ran_unif = round(random.uniform(0,0.5),2) #Randomly select between 0 to 0.5 representing the increase of digitalization
            ratio = list_digit_ratio[ins[-1]] + list_digit_ratio[ins[-1]] * ran_unif #Compute the new ratio from the previous one.
            if ratio <= 1: #We can not have a ratio above 1.
                list_digit_ratio.append(round(ratio,2))  #Append a random number corresponding to the ratio of digitalization.
                list_digit_percent.append(int(ratio * 100)) #Append a random number corresponding to the percentage of digitalization.
                rt = True #Since the conditions is respected and the ratio/percentages of digitalizaton added then we set the variable to «True».

        #Create variables from the ratio/percentages of digitalization.
        duration_digit = round(list_course_hrs[ins[0]] * ratio) #Set the number of hours using online ressources. 
        num_ress = round(list_ress[ins[0]] + ceil(list_ress[ins[0]] * (ratio - list_digit_ratio[ins[0]]))) #Set the number of online ressources.
        
        #Append lists.
        temp_ID.append(course) #Append the course ID in the temporary list.
        list_course_hrs.append(list_course_hrs[ins[0]]) #Append the number of hours of the course.
        list_duration_digit.append(duration_digit) #Append the hours using online ressources of the course.
        list_ress.append(num_ress) #Append the number of ressources of the course.
    
    else: #In case the selected ID has never been set.
        rand_num = random.random()  #Define a random number to choose the time interval of a course.
        if (0 <= rand_num < 0.2) : 
            num_hrs = random.randint(5, 15)   #Define a random number to have a course between 5H and 15H.
        elif (0.2 <= rand_num < 0.8) :
            num_hrs = random.randint(15, 40)  #Define a random number to have a course between 15H and 60H.
        elif (0.8 <= rand_num < 1):
            num_hrs = random.randint(40, 60)  #Define a random number to have a course between 60H and 90H.
        elif (rand_num == 1):
            num_hrs = random.randint(60, 120) #Define a random number to have a course between 90H and 120H.

        #Create variables.
        ran_unif = round(random.uniform(0,1),2) #Ratio of digitalization.
        num_digit = round(num_hrs * ran_unif) #Number of hours using online ressources.
        num_ress = random.randint(ceil(num_digit*0.25), num_digit) #Number of online ressources.

        #Append lists.
        temp_ID.append(course) #Append the course ID in the temporary list.
        list_course_hrs.append(num_hrs) #Append the number of hours of the course.
        list_digit_ratio.append(ran_unif)  #Append a random number corresponding to the ratio of digitalization
        list_digit_percent.append(int(ran_unif * 100)) #Append a random number corresponding to the percentage of digitalization
        list_duration_digit.append(num_digit) #Append the hours using online ressources of the course.
        list_ress.append(num_ress) #Append the number of ressources of the course.
    continue

#Create two temporary lists to implementate the year of each course and the total number of course from each year.
temp_year = []
temp_course_hrs = []

dep = 0
for num_courses in list_year_courses:
    for i in range(0, num_courses):
        temp_year.append(list_years[dep])
        temp_course_hrs.append(list_year_courses[dep])
    dep += 1

# Definir le dataframe (EN) 
Course_PerYear = pd.DataFrame({'Course_ID': list_courses_ID,
                                    'Year': temp_year,
                                    'Course_Duration': list_course_hrs,
                                    'Course_Duration_Digit': list_duration_digit,
                                    'Course_Duration_Present': [round(hrs - ldg) for hrs, ldg in zip(list_course_hrs, list_duration_digit)],
                                    #'Number_Ressources': list_ress,
                                    'Digit_Ratio': list_digit_ratio,
                                    'Digit_Percentage': list_digit_percent,
                                    'Total_Courses_perYear': temp_course_hrs,

})

######################################
# Factice Ressources Additional Data #
######################################

list_rv = []
list_rq = []
list_re = []
for ress in Course_PerYear['Course_Duration_Digit']:
    if ress >0:
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
    else:
        list_rv.append(0)
        list_rq.append(0)
        list_re.append(0)
Course_PerYear['Duration_Video'] = list_rv
Course_PerYear['Duration_Quiz'] = list_rq
Course_PerYear['Duration_Exam'] = list_re

list_nb_rv = []
list_nb_rq = []
list_nb_re = []
for vid, quiz, exam in zip(list_rv, list_rq, list_re):

    nb_vid = round(random.randint(ceil(vid/4), vid))
    nb_quiz = round(random.randint(ceil(quiz/2), quiz))
    nb_exam = round(random.randint(ceil(exam/4), exam))

    list_nb_rv.append(nb_vid)
    list_nb_rq.append(nb_quiz)
    list_nb_re.append(nb_exam)
Course_PerYear['Number_Video'] = list_nb_rv
Course_PerYear['Number_Quiz'] = list_nb_rq
Course_PerYear['Number_Exam'] = list_nb_re
Course_PerYear['Number_Ressources'] =  [list_nb_rv[i] + list_nb_rq[i] + list_nb_re[i] for i in range(len(list_nb_re))]


array_video = [] 
array_quizz = []
array_exam = []
count = 0
for X, Y in zip(Course_PerYear['Duration_Video'], Course_PerYear['Number_Video']):
    if (X == 0 or Y == 0):
        array_video.append([0,0,0,0])
    else:
        array = []
        for i in range(0, Y+1):
            for j in range(0, Y+1):
                for k in range(0, Y+1):
                    for l in range(0,Y+1):
                        if X == (1*i + 2*j + 3*k + 4*l) and Y == (i + j + k + l):
                            array.append([i,j,k,l])
                    count +=1
        if len(array) == 1:
            array_video.append(array[0])
        elif len(array) == 0:
            array_video.append([0,0,0,0])
        else:
            ran = random.randint(0, len(array)-1)
            array_video.append(array[ran])

Course_PerYear['Number_Video_1H'] = [array_video[i][0] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_2H'] = [array_video[i][1] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_3H'] = [array_video[i][2] for i in range(0, len(array_video))]
Course_PerYear['Number_Video_4H'] = [array_video[i][3] for i in range(0, len(array_video))]


for X, Y in zip(Course_PerYear['Duration_Quiz'], Course_PerYear['Number_Quiz']):
    if (X == 0 or Y == 0):
        array_quizz.append([0,0])
    else:
        array = []
        for i in range(0, Y+1):
            for j in range(0, Y+1):
                if X == (1*i + 2*j) and Y == (i + j):
                    array.append([i,j])
                    count +=1
        if len(array) == 1:
            array_quizz.append(array[0])
        elif len(array) == 0:
            array_quizz.append([0,0])
        else:
            ran = random.randint(0, len(array)-1)
            array_quizz.append(array[ran])

Course_PerYear['Number_Quiz_1H'] = [array_quizz[i][0] for i in range(0, len(array_quizz))]
Course_PerYear['Number_Quiz_2H'] = [array_quizz[i][1] for i in range(0, len(array_quizz))]


for X, Y in zip(Course_PerYear['Duration_Exam'], Course_PerYear['Number_Exam']):
    if (X == 0 or Y == 0):
        array_exam.append([0,0,0,0])
    else:
        array = []
        for i in range(0, Y+1):
            for j in range(0, Y+1):
                for k in range(0, Y+1):
                    for l in range(0,Y+1):
                        if X == (1*i + 2*j + 3*k + 4*l) and Y == (i + j + k + l):
                            array.append([i,j,k,l])
                    count +=1
        if len(array) == 1:
            array_exam.append(array[0])
        elif len(array) == 0:
            array_exam.append([0,0,0,0])
        else:
            ran = random.randint(0, len(array)-1)
            array_exam.append(array[ran])

Course_PerYear['Number_Exam_1H'] = [array_exam[i][0] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_2H'] = [array_exam[i][1] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_3H'] = [array_exam[i][2] for i in range(0, len(array_exam))]
Course_PerYear['Number_Exam_4H'] = [array_exam[i][3] for i in range(0, len(array_exam))]

print(count) #14 078 586

#############
# Save Data #
#############

#Save the dataframe into a CSV file
Course_PerYear = Course_PerYear.sort_values(by = 'Course_ID', ascending = True)
Course_PerYear.to_csv('Ressources/Example/Data/Ressources.csv')

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

col = ['Course_ID', 'Year', 'Course_Duration', 'Course_Duration_Digit', 'Number_Ressources', 'Number_Video', 'Number_Quiz', 'Number_Exam', 'Basic_Sequence', 'Advanced_Sequence']
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

Sequence_8_30 = Sequences[(Sequences['Course_Duration_Digit'].between(8, 30))]
Sequences_8_30 = Sequence_8_30[['Course_ID', 'Year', 'Course_Duration_Digit', 'Number_Ressources', 'Basic_Sequence', 'Advanced_Sequence']]

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
        list_Digit_Duration.append(Sequence_8_30.iloc[num]['Course_Duration_Digit'])
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
            'Course_Digit_Duration': Sequences_8_30.iloc[num]['Course_Duration_Digit'],
            'Ressources_Amount': Sequences_8_30.iloc[num]['Number_Ressources'],
            'Ressources_Rank': count, 
            'Ressources_Type': basic}, 
            'Ressources_Type': advanced}, ignore_index=True)
        count += 1
"""

#############
# Save Data #
#############

#Save the dataframe into a CSV file
Prepared_Sequence.to_csv('Ressources/Example/Data/Prepared_Sequences.csv')
