#############################################################################
# DataFrame of Quizzes (Difficulty, Type, Chapter, Departement, Year, ect.) #        
#############################################################################

#Import the required packages.
import numpy as np
import pandas as pd
import random
import time
import os
from math import *

#Define the path to the Data Folder (to save the DataFrame in the correct location).
dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Reingenieurie', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.
glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path.
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder.


################################################
# Initialization of the Program Execution Time #
################################################

start_time = time.time()


#####################################################
# Initialize a Pseudorandom Number Generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 182000 ) #The seed does not need to be randomize.


######################
# Class and Function #
######################

#Function that return some variables related to the type, level and number of attempts of the quiz (such as the succes percentage, ect.).
def Level_Percent(type, level, attempts):

    #Define some conditions and associated values to determine the minimum amount of learners per Quiz.
    conditions_learners = [type == 'QCU', type == 'QCM', type == 'QROC', type == 'QO'] #Define the conditions that are the type of the quiz.
    choices_learners = [ceil(attempts/3), ceil(attempts/4), ceil(attempts/2.5), ceil(attempts/2)] #Define the values corresponding to the connditions.
    learners_verif = np.select(conditions_learners, choices_learners) #Select a value representing the minimum amount of learners and depending on the above conditions and values.

    #Define some conditions and associated values to determine the true success ratio of the Quiz.
    conditions_ratio = [level == 'Trop Facile', level == 'Facile', level == 'Adapte', level == 'Difficile', level == 'Trop Difficile'] #Define the conditions that are the level of the quiz.
    choices_ratio = [round(random.uniform(0.86, 1), 4), round(random.uniform(0.76, 0.85), 4), round(random.uniform(0.60, 0.75), 4), round(random.uniform(0.25, 0.59), 4), round(random.uniform(0, 0.24), 4)] #Define the values corresponding to the connditions.
    true_ratio = np.select(conditions_ratio, choices_ratio) #Select a value representing the true success ratio of the Quiz depending on the above conditions and values.

    #Define the attempts related variables.
    success_attempts = round((true_ratio * num_attempts)) #The number of successful attempts.
    failure_attempts = attempts - success_attempts #The number of unsuccessful attempts.
    true_prct = round(true_ratio * 100, 2) #The percentage of success (from the ratio defined above).
    
    #Define the number of learners and associated variables.
    verif = False  #Set the variable "verif" to False.
    learners = round(random.uniform(success_attempts, attempts)) #The number of learners between the number of successful attempts and the total number of attempts.
    while verif == False: #Loop to verify a condition.
        if learners >= learners_verif: #Check that the defined number of learners is above or equal to the minimum number of learners (defined above).
            verif = True
            avg_learners_attempts = round( attempts / learners, 2) #The average number of attempts per Learners.
            learners_success = success_attempts #The number of successful learners.
            learners_failure = learners - learners_success #The number of unsuccessful learners.
            learners_success_prct = round((learners_success / learners) * 100, 2) #The percentage of successful learners. (do not take into account all the attempts done per user to succed).
        else:
            learners = round(random.uniform(success_attempts, attempts)) #Redetermine the number of learners if the conditions was not verified.


   #Define some conditions and associated values to determine the slip, guess per Quiz
    conditions_sgb = [type == 'QCU' and level == 'Trop Facile', type == 'QCU' and level == 'Facile', type == 'QCU' and level == 'Adapte', type == 'QCU' and level == 'Difficile', type == 'QCU' and level == 'Trop Difficile',
                      type == 'QCM' and level == 'Trop Facile', type == 'QCM' and level == 'Facile', type == 'QCM' and level == 'Adapte', type == 'QCM' and  level == 'Difficile', type == 'QCM' and  level == 'Trop Difficile',
                      type == 'QROC' and level == 'Trop Facile', type == 'QROC' and level == 'Facile', type == 'QROC' and level == 'Adapte', type == 'QROC' and  level == 'Difficile', type == 'QROC' and  level == 'Trop Difficile',
                      type == 'QO' and level == 'Trop Facile', type == 'QO' and level == 'Facile', type == 'QO' and level == 'Adapte', type == 'QO' and  level == 'Difficile', type == 'QO' and  level == 'Trop Difficile']
    choice_sgb = [ [round(random.uniform(0, 0.10), 2), round(random.uniform(0.90, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.75, 0.90), 2)], [round(random.uniform(0, 0.30), 2), round(random.uniform(0.40, 0.70), 2)], [round(random.uniform(0, 0.40), 2), round(random.uniform(0.30, 0.40), 2)], [round(random.uniform(0, 0.75), 2), round(random.uniform(0.20, 0.30), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.80, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.70, 0.80), 2)], [round(random.uniform(0, 0.30), 2), round(random.uniform(0.40, 0.70), 2)], [round(random.uniform(0, 0.50), 2), round(random.uniform(0.30, 0.40), 2)], [round(random.uniform(0, 0.75), 2), round(random.uniform(0.20, 0.30), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.50, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.40, 0.75), 2)], [round(random.uniform(0.20, 0.50), 2), round(random.uniform(0.25, 0.40), 2)], [round(random.uniform(0.50, 0.75), 2), round(random.uniform(0.15, 0.25), 2)], [round(random.uniform(0.75, 1), 2), round(random.uniform(0, 0.15), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.50, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.30, 0.75), 2)], [round(random.uniform(0.20, 0.75), 2), round(random.uniform(0.15, 0.30), 2)], [round(random.uniform(0.75, 0.90), 2), round(random.uniform(0, 0.15), 2)], [round(random.uniform(0.90, 1), 2), round(random.uniform(0, 0.10), 2)]]
    slip, guess,  = np.select(conditions_sgb, choice_sgb)
    b = true_ratio #Define the difficulty (b) of the quiz

    #Return all the defined variables related to both learners and attempts.
    return learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b


#Function that return the predicted level of difficulty and correct level of difficulty of the Quiz. (for each type)
def TyLvL_PrdCct(type, rand_num):
    
    conditions_type = [type == 'QCU', type == 'QCM', type == 'QROC', type == 'QO'] #Define the conditions.
    choices_type = [
        [rand_num <= 0.20, 0.20 < rand_num < 0.45,  0.45 <= rand_num <= 0.55, 0.55 < rand_num <= 0.80, 0.80 < rand_num <= 1],  #QCU
        [rand_num <= 0.15, 0.15 < rand_num < 0.35,  0.35 <= rand_num <= 0.50, 0.50 < rand_num <= 0.80, 0.80 < rand_num <= 1],  #QCM
        [rand_num <= 0.10, 0.10 < rand_num < 0.25,  0.25 <= rand_num <= 0.40, 0.40 < rand_num <= 0.75, 0.75 < rand_num <= 1],  #QROC
        [rand_num <= 0.05, 0.05 < rand_num < 0.15,  0.15 <= rand_num <= 0.25, 0.25 < rand_num <= 0.65, 0.65 < rand_num <= 1],]  #QO
    conditions_predict = np.select(conditions_type, choices_type)
    choices_predict = ['Trop Facile', 'Facile', 'Adapte', 'Difficile', 'Trop Difficile'] #Define the values corresponding to the connditions.
    predict_level = choices_predict[np.asarray([index for index in range(len(conditions_predict)) if conditions_predict[index] == 1]).item()]

    ran = random.random()
    condition_correct = [ran >= 0.33, ran < 0.33] #Define the conditions.
    choices_correct = [predict_level, random.choice(list(filter((predict_level).__ne__, choices_predict)))] #Define the values corresponding to the connditions.
    correct_level = np.select(condition_correct, choices_correct) #Select a value depending on the above conditions and values.

    #Return the predicted and correct level of difficulty of the Quiz.
    return predict_level, correct_level

#Function that execute the associated function to return the predict, correct level of difficulty and learners, attempts variables.
def TyLvl_ScsFlr(type, rand_num, attempts):

    #Execute the predict, correct level of difficulty function.
    predict_level, correct_level = TyLvL_PrdCct(type, rand_num)

    #Execute the learners, attempts function.
    learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b  = Level_Percent(type, correct_level, attempts)

    #Return all the variables defined through the two previous functions
    return predict_level, correct_level, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b


################
# Factice Data #
################

#Define the list of years
temp_Years = [year for year in range(2015, 2021)] #Append in a list, each year.
print('List of Years:', temp_Years) #Display the list of Years.


#Define the number of quizzes
number_Quizzes = random.randint(100, 1000) #Create a variable to represent the number of Quizzes.
print('Number of Quizzes:', number_Quizzes) #Display the number of Quizzes.


#Define the list of departements
depts_type = ['Economie', 'Histoire', 'Droit', 'Management', 'Art', 'Sociologie', 'Mathematique', 'Ingenieurie', 'Philosophie', 'Informatique', 'Langues'] #Define a list of Departements
num_depts = random.randint(ceil(number_Quizzes/150), ceil(number_Quizzes/100)) #Randomly select the number of Departements
temp_Depts = random.sample(depts_type, num_depts) #Randomly select the Departements
print('Number of Departement(s):', num_depts) #Display the number of Departements.
print('List of Departements:', temp_Depts) #Display the list of Departements.


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


########################################
# Build and Implement the set of Lists #
########################################

#Define a multiple lists that correspond to information related to each quiz.
lst_year, lst_depts, lst_quiz_ID, lst_chapt_ID, lst_quiz_chapt, lst_rank, lst_quiz_type = [], [], [], [], [], [], []
lst_attempts, lst_success_attempts, lst_failure_attempts, lst_truepercent = [], [], [], []
lst_learners, lst_learners_success, lst_learners_failure, lst_learners_successprct, lst_avg_attempts  = [], [], [], [], []
lst_levelpredict, lst_levelcorrect, lst_levelpc = [], [], []
lst_slip, lst_guess, lst_b = [], [], []

#Define some arrays of choices.
chap_percent = [1] * 4 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 8 + [6] * 10 + [7] * 15 + [8] * 10 + [9] * 10 + [10] * 8 + [11] * 5 + [12] * 5 + [13] * 5 + [14] * 4 #Array of Choice to determine the number of Quiz per chapter
quiztype_percent = ['QCU'] * 45 + ['QCM'] * 35 + ['QROC'] * 15 + ['QO'] * 5 #Array of Choice to determine the type of the Quiz
pred_level = ['Trop Facile'] + ['Facile']  + ['Adapte']  + ['Difficile'] +  ['Trop Difficile']  #Array of choice to determine the level of the Quiz


#Define the number of Quizzes per Chapter and their ID.
for year in temp_Years: #Iterate for each year from the "temp_Years" list
    quiz_ID = 1 #Define the initial state of the Quizz ID (= 1)
    for num_quiz, index in zip(lst_quizz_depts, range(0, len(lst_quizz_depts))): #Make a loop taking all quizzes for each departement.
        num = 0 #Defined a variable used to compute the number of quizzes.
        chap_ID = 1 #Defined the initial sate of the Chapter ID (= 1)

        while num != num_quiz:
            ins_chap = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
            chap_ID = lst_chapt_ID[ins_chap[-1]] if quiz_ID in lst_quiz_ID else chap_ID
            chapter_quiz = lst_quiz_chapt[ins_chap[-1]] if quiz_ID in lst_quiz_ID else random.choice(chap_percent)
            if num + chapter_quiz <= num_quiz:
                rank = 0
                for chap in range(0, chapter_quiz):
                    rank += 1
                    ins = [quiz for quiz in range(0, len(lst_quiz_ID)) if lst_quiz_ID[quiz] == quiz_ID] if quiz_ID in lst_quiz_ID else []
                    type_quiz = lst_quiz_type[ins[-1]] if quiz_ID in lst_quiz_ID else random.choice(quiztype_percent)
                    num_attempts = random.choice(list(range(round(lst_attempts[ins[-1]]*0.80), round(lst_attempts[ins[-1]]*1.20)+1))) if quiz_ID in lst_quiz_ID else  random.randint(5, 100)

                    if quiz_ID in lst_quiz_ID:
                        if lst_levelcorrect[ins[-1]] == "Adapte":
                            correct_level = lst_levelcorrect[ins[-1]] 
                            predict_level = correct_level
                            learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b  = Level_Percent(type_quiz, correct_level, num_attempts)    
                        else:
                            predict_level, correct_level, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b = TyLvl_ScsFlr(type_quiz, rand_num, num_attempts)                     

                    else:
                        rand_num = random.random()
                        predict_level, correct_level, learners, avg_learners_attempts, learners_success, learners_failure, learners_success_prct, success_attempts, failure_attempts, true_prct, slip, guess, b = TyLvl_ScsFlr(type_quiz, rand_num, num_attempts)
                    pred_crct_level = str(predict_level) + ' / ' + str(correct_level)
                    
            
                    
                    #Append the Lists
                    lst_quiz_ID.append(quiz_ID)
                    lst_year.append(year)
                    lst_depts.append(temp_Depts[index])
                    lst_chapt_ID.append(chap_ID)
                    lst_quiz_chapt.append(chapter_quiz)
                    lst_quiz_type.append(type_quiz)
                    lst_attempts.append(num_attempts)
                    lst_learners.append(learners)
                    lst_avg_attempts.append(avg_learners_attempts)
                    lst_learners_success.append(learners_success)
                    lst_learners_failure.append(learners_failure)
                    lst_learners_successprct.append(learners_success_prct)
                    lst_success_attempts.append(success_attempts)
                    lst_failure_attempts.append(failure_attempts)
                    lst_truepercent.append(true_prct)
                    lst_levelpredict.append(predict_level)
                    lst_levelcorrect.append(correct_level)
                    lst_levelpc.append(pred_crct_level)
                    lst_slip.append(slip)
                    lst_guess.append(guess)
                    lst_b.append(b)
                    lst_rank.append(rank)

                    quiz_ID += 1
                num += chapter_quiz
                chap_ID += 1


#######################
# Build the DataFrame #
#######################

#Define the First DataFrame
Quizzes_db = pd.DataFrame({'Quizz_ID': lst_quiz_ID,
                           'Year': lst_year,
                           'Departement': lst_depts,
                           'Chapter_ID': lst_chapt_ID,
                           #'Quiz_perChapter': lst_quiz_chapt,
                           'Rank_onChapter': lst_rank,
                           'Quizz_Type': lst_quiz_type, 
                           'B': lst_b,
                           'Slip': lst_slip,
                           'Guess': lst_guess,
                           'Number_Attempts': lst_attempts,
                           'UniQ_Learner': lst_learners,
                           'Sucessful_Learners': lst_learners_success,
                           'Unsucessful_Learners': lst_learners_failure,
                           'Avg_Attempts': lst_avg_attempts,
                           'Percent_Learners_Success': lst_learners_successprct,
                           'Success_Attempts': lst_success_attempts,
                           'Failure_Attempts': lst_failure_attempts,
                           'TruePrct_Succes': lst_truepercent,
                           'Predict_Difficulty': lst_levelpredict,
                           'Correct_Difficulty': lst_levelcorrect,
                           'Prediction/Correct Difficulty': lst_levelpc,
}).sort_values(by = ['Quizz_ID', 'Year'], ascending = True)

print(Quizzes_db.head(5)) #Display the DataFrame.


#############
# Save Data #
#############

#Save the Quizzes DataFrame into a CSV File using the correct path.
Quizzes_db.to_csv(path_data + 'Quizzes.csv')


######################################
# Compute the Program Execution Time #
######################################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))