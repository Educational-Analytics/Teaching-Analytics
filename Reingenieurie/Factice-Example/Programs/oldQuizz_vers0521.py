###
#  #        
####

#Import the required packages

import random
from math import *
import numpy as np
from numpy.core.numeric import NaN
from numpy.lib.arraysetops import isin
import pandas as pd
import time
import os


################
#Find the Path #
################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Teaching-Analytics', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder


##################
# Initialization #
##################

#Set the start_time
start_time = time.time()


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 2345 ) #The seed does not need to be randomize.


######################
# Class and Function #
######################

#Function to get data from the correct level
def Level_Percent(type, level, attempts):
    conditions = [type == 'QCU',
                  type == 'QCM',
                  type == 'QROC',
                  type == 'QO']

    choices = [random.randint(ceil(attempts/3), attempts),
               random.randint(ceil(attempts/4), attempts),
               random.randint(ceil(attempts/2.5), attempts),
               random.randint(ceil(attempts/2), attempts)]

    learners = np.select(conditions, choices)

    if level == 'Trop Facile':
        success = round(random.uniform(learners*0.86, learners))
    elif level == 'Facile':
        success = round(random.uniform(learners*0.75, learners*0.85))
    elif level == 'Adapte':
        success = round(random.uniform(learners*0.60, learners*0.75))
    elif level == 'Difficile':
        success = round(random.uniform(learners*0.20, learners*0.60))
    elif level == 'Trop Difficile':
        success = round(random.uniform(learners*0, learners*0.20))
    failure = learners - success
    percent_success = round((success / attempts) * 100, 2) 

    avg_attempts = round(attempts / learners, 2) #Require to be modified
    
    return learners, success, failure, percent_success, avg_attempts


def QCU_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.20:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.20 < rand_num < 0.45:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.45 <= rand_num <= 0.55:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.55 < rand_num <= 0.80:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.80 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

def QCM_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.15:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.15 < rand_num < 0.30:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.30 <= rand_num <= 0.50:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.50 < rand_num <= 0.80:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.80 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###


###

def QROC_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.10:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.10 < rand_num < 0.25:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.25 <= rand_num <= 0.40:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.40 < rand_num <= 0.75:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.75 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

###

def QO_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.5:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.5 < rand_num < 0.15:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.15 <= rand_num <= 0.25:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.25 < rand_num <= 0.65:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.65 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

def TyLvl_ScsFlr(type, rand_num, level_array, attempts):
    if type == 'QCU':
        predict_level, correct_level = QCU_PrdCct_level(rand_num, level_array)
    elif type == 'QCM':
        predict_level, correct_level = QCM_PrdCct_level(rand_num, level_array)
    elif type == 'QROC':
        predict_level, correct_level = QROC_PrdCct_level(rand_num, level_array)
    elif type == 'QO':
        predict_level, correct_level = QO_PrdCct_level(rand_num, level_array)

    learners, success, failure, success_percent, avg_attempts  = Level_Percent(type, correct_level, attempts)

    return predict_level, correct_level, learners, success, failure, success_percent, avg_attempts 


################
# Factice Data #
################

#Define the number of quizzes
number_Quizzes = random.randint(100, 1000) #Create a variable to represent the number of Quizzes.
print('Number of Quizzes:', number_Quizzes) #Display the number of Quizzes.


#Define the list of departements
depts_type = ['Economie', 'Histoire', 'Droit', 'Management', 'Art', 'Sociologie', 'Mathématique', 'Ingénieurie', 'Philosophie', 'Informatique', 'Langues'] #Define a list of Departements
num_depts = random.randint(ceil(number_Quizzes/150), ceil(number_Quizzes/100)) #Randomly select the number of Departements
temp_Depts = random.sample(depts_type, num_depts) #Randomly select the Departements
print('Number of Departement(s):', num_depts) #Display the number of Departements.
print('List of Departements:', temp_Depts) #Display the list of Departements.


#Define the list of years
temp_Years = [year for year in range(2015, 2021)] #Append in a list, each year.
print('List of Years:', temp_Years) #Display the list of Years.

#Define the number of Quizzes per Departement
avg_quiz = round(number_Quizzes/num_depts) #Find the average number of quizzes per Departement.
print('Average Number of Quizzes per Departement:', avg_quiz) #Display the average.

lst_quizz_depts = [] #Create a list representing the number of Quizzes per Departement.
temp_quizz = number_Quizzes #Create a temporal variable.
while sum(lst_quizz_depts) != number_Quizzes: #Create a loop that will continue until the sum of the quizzes per departement is the same as the number of quizzes
    for len_dep in range(0, num_depts): #Create another loop to iterate the number of quizzes to each Departements.
        numb = round(random.uniform(avg_quiz*0.90, avg_quiz*1.1)) #Select to 10% of difference from the average.
        lst_quizz_depts.append(numb) #Append the number of quizzes into the list

    if sum(lst_quizz_depts) != number_Quizzes: #Verify if the sum of the list is different from the number of quizzes previously defined.
        lst_quizz_depts.clear() #Clear the list

print('List of Number of Quizzes per Departement:', lst_quizz_depts) #Display the number of Quizzes per Departement.


#Define a set of lists
lst_year = []
lst_depts = []
lst_quiz_ID = []
lst_chapt_ID = []
lst_quiz_chapt = []
lst_quiz_type = []
lst_attempts = []
lst_learners = []
lst_avg_attempts = []
lst_learners_success = []
lst_learners_failure = []
lst_levelpredict = []
lst_levelcorrect = []
lst_learners_successprct = []

lst_success_attempts = []
lst_failure_attempts = []

#Define arrays of choice
chap_percent = [1] * 4 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 8 + [6] * 10 + [7] * 15 + [8] * 10 + [9] * 10 + [10] * 8 + [11] * 5 + [12] * 5 + [13] * 5 + [14] * 4
quiztype_percent = ['QCU'] * 50 + ['QCM'] * 35 + ['QROC'] * 10 + ['QO'] * 5
pred_level = ['Trop Facile'] + ['Facile']  + ['Adapte']  + ['Difficile'] +  ['Trop Difficile']  

#Define the number of Quizzes per Chapter and their ID.
counta = 0
for year in temp_Years:
    quiz_ID = 1
    for num_quiz, index in zip(lst_quizz_depts, range(0, len(lst_quizz_depts))):
        num = 0
        chap_ID = 1
        count = 0 

        while num != num_quiz:
            ins_chap = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
            chap_ID = lst_chapt_ID[ins_chap[-1]] if quiz_ID in lst_quiz_ID else chap_ID
            chapter_quiz = lst_quiz_chapt[ins_chap[-1]] if quiz_ID in lst_quiz_ID else random.choice(chap_percent)
            if num + chapter_quiz <= num_quiz:
                for chap in range(0, chapter_quiz):
                    ins = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
                    type_quiz = lst_quiz_type[ins[-1]] if quiz_ID in lst_quiz_ID else random.choice(quiztype_percent)
                    num_attempts = random.choice(list(range(round(lst_attempts[ins[-1]]*0.80), round(lst_attempts[ins[-1]]*1.20)+1))) if quiz_ID in lst_quiz_ID else  random.randint(5, 100)

                    if quiz_ID in lst_quiz_ID:
                        correct_level = lst_levelcorrect[ins[-1]]
                        if correct_level == "Adapte":
                            predict_level = correct_level
                            learners, learners_success, learners_failure, success_percent, avg_attempts  = Level_Percent(type_quiz, correct_level, num_attempts)    
                            success_attempts = learners_success
                            failure_attempts = num_attempts - success_attempts
                        else:
                            predict_level = lst_levelpredict[ins[-1]]
                            correct_level = lst_levelcorrect[ins[-1]]
                            learners = lst_learners[ins[-1]]
                            learners_success = lst_learners_success[ins[-1]]
                            learners_failure = lst_learners_failure[ins[-1]]
                            success_percent = lst_learners_successprct[ins[-1]]
                            avg_attempts = lst_avg_attempts[ins[-1]]
                            success_attempts = lst_success_attempts[ins[-1]]
                            failure_attempts = lst_failure_attempts[ins[-1]]
                    else:
                        rand_num = random.random()
                        temp_pred = pred_level
                        predict_level, correct_level, learners, learners_success, learners_failure, success_percent, avg_attempts = TyLvl_ScsFlr(type_quiz, rand_num,  temp_pred, num_attempts)
                        success_attempts = learners_success
                        failure_attempts = num_attempts - success_attempts
                
                    
            
                    
                    #Append the Lists
                    lst_quiz_ID.append(quiz_ID)
                    lst_year.append(year)
                    lst_depts.append(temp_Depts[index])
                    lst_chapt_ID.append(chap_ID)
                    lst_quiz_chapt.append(chapter_quiz)
                    lst_quiz_type.append(type_quiz)
                    lst_attempts.append(num_attempts)
                    lst_learners.append(learners)
                    lst_avg_attempts.append(avg_attempts)
                    lst_learners_success.append(learners_success)
                    lst_learners_failure.append(learners_failure)
                    lst_learners_successprct.append(success_percent)
                    lst_success_attempts.append(success_attempts)
                    lst_failure_attempts.append(failure_attempts)
                    lst_levelpredict.append(predict_level)
                    lst_levelcorrect.append(correct_level)
                    quiz_ID += 1
                    counta += 1
                num += chapter_quiz
                chap_ID += 1

#Define the First DataFrame
Quizzes_db = pd.DataFrame({'Quizz_ID': lst_quiz_ID,
                           'Year': lst_year,
                           'Departement': lst_depts,
                           'Chapter_ID': lst_chapt_ID,
                           'Quiz_perChapter': lst_quiz_chapt,
                           'Quizz_Type': lst_quiz_type, 
                           'Number_Attempts': lst_attempts,
                           'UniQ_Learner_Attempts': lst_learners,
                           'Avg_Number_Attempts': lst_avg_attempts,
                           'Sucessful_Learners': lst_learners_success,
                           'Unsucessful_Learners': lst_learners_failure,
                           'Success_Attempts': lst_success_attempts,
                           'Failure_Attempts': lst_failure_attempts,
                           'Percent_Success': lst_learners_successprct,
                           'Predict_Difficulty': lst_levelpredict,
                           'Correct_Difficulty': lst_levelcorrect
}).sort_values(by = ['Quizz_ID', 'Year'], ascending = True).set_index('Quizz_ID')

print(Quizzes_db.head(5)) #Display the DataFrame.



"""
#Defined list

lst_attempts = []
lst_student = []
lst_s_attempts = []
lst_f_attempts = []
lst_succes_prct = []
lst_learners_failure_prct = []
lst_guess = []
lst_slip = []
lst_b = []
"""

"""
quiz_ID = 0
for quiz in range(0, number_Quizzes):
    #Variables
    quiz_ID += 1 #Incremente the variable to implement the ID for each quizz

    num_attempts = random.randint(1, 30)  #Define a random number of attempts for each quizz (between 1 and 50)
    num_students = random.randint(ceil(num_attempts/4), num_attempts)
    num_success = random.randint(0, num_attempts) #Define a random number of success for each quizz (between 0 and the number of attempts)
    num_failure = num_attempts - num_success #Define a random number of failure for each quizz

    succes_ratio = round((num_success/num_attempts), 2) #Compute the ratio of sucess for each quizz
    succes_percent = int(succes_ratio * 100) #Compute the percentage of sucess for each quizz

    failure_ratio = round(1 - succes_ratio, 2) #Compute the ratio of failure for each quizz
    failure_percent = int(failure_ratio * 100) #Compute the percentage of failure for each quizz

    #GUESS/slip
    #Need to be modified in a more specific way
    if succes_ratio == 0:
        ran = random.random()
        if ran >= 0.8:
            slip = random.uniform(0.90, 1)
        elif ran >= 0.5 and ran < 0.8:
            slip = random.uniform(0.75, 0.90)
        else:
            slip = random.uniform(0.75, 1)
        guess = 0

    elif 0 < succes_ratio <= 0.2:
        ran = random.random()
        if ran >= 0.8:
            slip = random.uniform(0.75, 1)
        elif ran >= 0.5 and ran < 0.8:
            slip = random.uniform(0.5, 0.75)
        else:
            slip = random.uniform(0.5, 1)
        guess = random.uniform(0, 0.2)

    elif succes_ratio > 0.2 and succes_ratio <= 0.5:
        ran = random.random()
        if ran >= 0.8:
            slip = random.uniform(0.5, 0.75)
        elif ran >= 0.5 and ran < 0.8:
            slip = random.uniform(0.25, 0.50)
        else:
            slip = random.uniform(0.25, 1)
        guess = random.uniform(0.2, 0.5)

    elif succes_ratio > 0.5 and succes_ratio <= 0.8:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.5, 0.75)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.25, 0.50)
        else:
            guess = random.uniform(0.5, 1)
        slip = random.uniform(0.2, 0.5)

    elif succes_ratio > 0.8 and succes_ratio < 1:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.75, 1)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.5, 0.75)
        else:
            guess = random.uniform(0.75, 1)
        slip = random.uniform(0, 0.2)

    elif succes_ratio == 1:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.90, 1)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.75, 0.90)
        else:
            guess = random.uniform(0.75, 1)
        slip = 0

    guess, slip = round(guess, 2),  round(slip, 2) 

    #b
    if 0 <= guess < 0.25 and 0 < slip <= 0.25:
        b = round(random.uniform(0.4, 0.6), 2)
    elif 0.25 <= guess < 0.5 and 0 < slip <= 0.25:
        b = round(random.uniform(0.4, 0.5), 2)
    elif 0.5 <= guess < 0.75 and 0 < slip <= 0.25:
        b = round(random.uniform(0.25, 0.4), 2)
    elif 0.75 <= guess < 1 and slip <= 0.25:
        b = round(random.uniform(0.1, 0.25), 2)
    elif guess == 1:
        b = round(random.uniform(0, 0.1), 2)

    elif 0.25 <= slip < 0.5 and 0 < guess <= 0.25:
        b = round(random.uniform(0.5, 0.6), 2)
    elif 0.5 <= slip < 0.75 and 0 < guess <= 0.25:
        b = round(random.uniform(0.6, 0.75), 2)
    elif 0.75 <= slip < 1 and guess <= 0.25:
        b = round(random.uniform(0.75, 0.9), 2)
    elif slip == 1:
        b = round(random.uniform(0.9, 1), 2)

    else:
        b = round(random.uniform(0.35, 0.65), 2)


    #Append lists
    lst_quiz_ID.append(quiz_ID)
    lst_attempts.append(num_attempts)
    lst_s_attempts.append(num_success)
    lst_f_attempts.append(num_failure)
    lst_succes_prct.append(succes_percent)
    lst_learners_failure_prct.append(failure_percent)
    lst_guess.append(guess)
    lst_slip.append(slip)
    lst_b.append(b)


Quizzes_db = pd.DataFrame({'Quizz_ID': lst_quiz_ID,
                           'Number_Attempts': lst_attempts,
                           'Number_Success': lst_s_attempts,
                           'Number_Failure': lst_f_attempts,
                           'Success_Percent': lst_succes_prct,  
                           'Failure_Percent': lst_learners_failure_prct,    
                           'Guess': lst_guess,
                           'Slip': lst_slip,
                           'B': lst_b,      
}).sort_values(by = 'Quizz_ID', ascending = True).set_index('Quizz_ID')

print(Quizzes_db)
"""
#############
# Save Data #
#############

#Save the Login into a CSV File.
Quizzes_db.to_csv('Reingenieurie\Factice-Example\Data\QuizzesBis.csv')

#######################
# Time Execution DONE #
#######################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))


