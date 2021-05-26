###
#  #        
####

#Import the required packages

import random
from math import *
import datetime
from datetime import datetime
import numpy as np
from numpy.core.numeric import NaN
from numpy.lib.arraysetops import isin
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import time
#


##################
# Initialization #
##################


#Set the start_time
start_time = time.time()

################
#Find the Path #
################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Teacher_Improve', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder

#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 1001 ) #The seed does not need to be randomize


######################
# Class and Function #
######################


#################################
# Import the required Data file #
#################################

Date_Teacher = pd.read_csv(path_data + 'Date_Teacher.csv')
Date_Teacher = Date_Teacher.iloc[: , 1:]

################################################
# Create Digitalisation Ressources Improvement #
################################################

Scolar_Months = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août") #List of Months.

Date_Teacher_UniQ = Date_Teacher[['Teacher_ID', 'Year', 'Month', 'Course_Ress_Digit']].drop_duplicates().assign(Digit_Improve = int()).sort_values(by = ['Teacher_ID', 'Year']).reset_index().iloc[: , 1:]

for index in Date_Teacher_UniQ.index:
    if index == 0 or Date_Teacher_UniQ.at[index,"Teacher_ID"] != Date_Teacher_UniQ.at[index-1,"Teacher_ID"]:
        Date_Teacher_UniQ.loc[index,"Digit_Improve"] = 0
    elif Date_Teacher_UniQ.at[index,"Year"] != Date_Teacher_UniQ.at[index-1,"Year"] and Date_Teacher_UniQ.at[index,"Month"] in Scolar_Months:
        Date_Teacher_UniQ.loc[index,"Digit_Improve"] = Date_Teacher_UniQ.loc[index-1,"Digit_Improve"]

    else:
        Date_Teacher_UniQ.loc[index,"Digit_Improve"] = Date_Teacher_UniQ.at[index,"Course_Ress_Digit"] - Date_Teacher_UniQ.at[index-1,"Course_Ress_Digit"]

#Merge_db = pd.merge(Date_Teacher, Date_Teacher_UniQ[['Teacher_ID', 'Year', 'Digit_Improve']] , on = ['Teacher_ID', 'Year'])
print(Date_Teacher_UniQ)

"""
####################################
# Create Day and Time of Connexion #
####################################

Merge_db.assign(Number_Connexion = int(), Time_Connexion = int())

random_num = [0] * 80 + [1] * 15 + 2 * [5]
random_time_one = [1] * 50 + [2] * 24 + [3] * 12 + [4] * 8 + [5] * 1 
random_time_list = [1] * 60 + [2] * 30 + [3] * 5 + [4] * 4 + [5] * 1
number_connexion = []
time_connexion = []

for index in Merge_db.index:
    if Merge_db.at[index,"Is_Weekend"] == 'Oui':
        num_con = random.choice(random_num) if random.random(0, 1) >= 0.80 else 0
    else:
        num_con = random.choice(random_num) if random.random(0, 1) >= 0.75 else 0

    time_con = 0
    for tme in range(0, num_con):
        if num_con == 1:
           time_con = random.choice(random_time_one)     
        else:
            time_con = random.choice(random_time_one) 
    
    number_connexion.append(num_con)
    time_connexion.append(time_con)

Merge_db["Number_Connexion"] = number_connexion
Merge_db["Time_Connexion"] = time_connexion

print(len(Merge_db[Merge_db.Year == 2013]))
print(len(Merge_db[(Merge_db.Year == 2014) & (Merge_db.Teacher_ID == 1) & (Merge_db.Number_Connexion > 0)]))
print(Merge_db[(Merge_db.Year == 2014) & (Merge_db.Teacher_ID == 1) & (Merge_db.Number_Connexion > 0)]['Time_Connexion'].sum())
print(Merge_db[(Merge_db.Year == 2014) & (Merge_db.Teacher_ID == 1) & (Merge_db.Number_Connexion > 0)]['Digit_Improve'].unique())
print(Merge_db[(Merge_db.Year == 2014) & (Merge_db.Number_Connexion > 0)].groupby('Teacher_ID')['Time_Connexion'].sum())
print(Merge_db[(Merge_db.Year == 2014) & (Merge_db.Number_Connexion > 0)].groupby('Teacher_ID')['Digit_Improve'].mean())


Merge_db_1 = Merge_db[Merge_db.Teacher_ID == 1].groupby(['Year', 'Trimester'])['Number_Connexion'].sum().reset_index()
sns.lineplot(data=Merge_db_1, x = 'Year', y = 'Number_Connexion', hue = 'Trimester')
plt.show()

#############
# Save Data #
#############

#Save the Login into a CSV File.
#Merge_db.to_csv(path_data + 'Lst_Date_Teacher.csv')

#######################
# Time Execution DONE #
#######################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))

"""