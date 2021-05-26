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
keywords = ['Reingenieurie', 'Factice-Example'] #Determine the keywords that will take the folder position.
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


################
# Factice Data #
################

number_Quizzes = random.randint(0, 150) #Create a variable to represent the number of Quizzes.
print('Number of Quizzes:', number_Quizzes) #Display the number of Quizzes.

#Defined list
lst_quiz_ID = []
lst_attempts = []
lst_s_attempts = []
lst_f_attempts = []
lst_succes_prct = []
lst_failure_prct = []
lst_guess = []
lst_sleep = []
lst_theta = []

quiz_ID = 0
for quiz in range(0, number_Quizzes):
    #Variables
    quiz_ID += 1 #Incremente the variable to implement the ID for each quizz

    num_attempts = random.randint(1, 50)  #Define a random number of attempts for each quizz (between 1 and 50)
    num_success = random.randint(0, num_attempts) #Define a random number of success for each quizz (between 0 and the number of attempts)
    num_failure = num_attempts - num_success #Define a random number of failure for each quizz

    succes_ratio = round((num_success/num_attempts), 2) #Compute the ratio of sucess for each quizz
    succes_percent = int(succes_ratio * 100) #Compute the percentage of sucess for each quizz

    failure_ratio = round(1 - succes_ratio, 2) #Compute the ratio of failure for each quizz
    failure_percent = int(failure_ratio * 100) #Compute the percentage of failure for each quizz

    #GUESS/SLEEP
    #Need to be modified in a more specific way
    if succes_ratio == 0:
        ran = random.random()
        if ran >= 0.8:
            sleep = random.uniform(0.90, 1)
        elif ran >= 0.5 and ran < 0.8:
            sleep = random.uniform(0.75, 0.90)
        else:
            sleep = random.uniform(0.75, 1)
        guess = 0

    elif 0 < succes_ratio <= 0.2:
        ran = random.random()
        if ran >= 0.8:
            sleep = random.uniform(0.75, 1)
        elif ran >= 0.5 and ran < 0.8:
            sleep = random.uniform(0.5, 0.75)
        else:
            sleep = random.uniform(0.5, 1)
        guess = random.uniform(0, 0.2)

    elif succes_ratio > 0.2 and succes_ratio <= 0.5:
        ran = random.random()
        if ran >= 0.8:
            sleep = random.uniform(0.5, 0.75)
        elif ran >= 0.5 and ran < 0.8:
            sleep = random.uniform(0.25, 0.50)
        else:
            sleep = random.uniform(0.25, 1)
        guess = random.uniform(0.2, 0.5)

    elif succes_ratio > 0.5 and succes_ratio <= 0.8:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.5, 0.75)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.25, 0.50)
        else:
            guess = random.uniform(0.5, 1)
        sleep = random.uniform(0.2, 0.5)

    elif succes_ratio > 0.8 and succes_ratio < 1:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.75, 1)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.5, 0.75)
        else:
            guess = random.uniform(0.75, 1)
        sleep = random.uniform(0, 0.2)

    elif succes_ratio == 1:
        ran = random.random()
        if ran >= 0.8:
            guess = random.uniform(0.90, 1)
        elif ran >= 0.5 and ran < 0.8:
            guess = random.uniform(0.75, 0.90)
        else:
            guess = random.uniform(0.75, 1)
        sleep = 0

    guess, sleep = round(guess, 2),  round(sleep, 2) 

    #Theta
    if 0 <= guess < 0.25 and 0 < sleep <= 0.25:
        theta = round(random.uniform(0.4, 0.6), 2)
    elif 0.25 <= guess < 0.5 and 0 < sleep <= 0.25:
        theta = round(random.uniform(0.4, 0.5), 2)
    elif 0.5 <= guess < 0.75 and 0 < sleep <= 0.25:
        theta = round(random.uniform(0.25, 0.4), 2)
    elif 0.75 <= guess < 1 and sleep <= 0.25:
        theta = round(random.uniform(0.1, 0.25), 2)
    elif guess == 1:
        theta = round(random.uniform(0, 0.1), 2)

    elif 0.25 <= sleep < 0.5 and 0 < guess <= 0.25:
        theta = round(random.uniform(0.5, 0.6), 2)
    elif 0.5 <= sleep < 0.75 and 0 < guess <= 0.25:
        theta = round(random.uniform(0.6, 0.75), 2)
    elif 0.75 <= sleep < 1 and guess <= 0.25:
        theta = round(random.uniform(0.75, 0.9), 2)
    elif sleep == 1:
        theta = round(random.uniform(0.9, 1), 2)

    else:
        theta = round(random.uniform(0.35, 0.65), 2)


    #Append lists
    lst_quiz_ID.append(quiz_ID)
    lst_attempts.append(num_attempts)
    lst_s_attempts.append(num_success)
    lst_f_attempts.append(num_failure)
    lst_succes_prct.append(succes_percent)
    lst_failure_prct.append(failure_percent)
    lst_guess.append(guess)
    lst_sleep.append(sleep)
    lst_theta.append(theta)


Quizzes_db = pd.DataFrame({'Quizz_ID': lst_quiz_ID,
                           'Number_Attempts': lst_attempts,
                           'Number_Success': lst_s_attempts,
                           'Number_Failure': lst_f_attempts,
                           'Success_Percent': lst_succes_prct,  
                           'Failure_Percent': lst_failure_prct,    
                           'Guess': lst_guess,
                           'Sleep': lst_sleep,
                           'Theta': lst_theta,      
}).sort_values(by = 'Quizz_ID', ascending = True)


print(Quizzes_db)

#############
# Save Data #
#############

#Save the Login into a CSV File.
Quizzes_db.to_csv(path_data + 'Quizzes.csv')

#######################
# Time Execution DONE #
#######################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))