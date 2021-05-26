#Import the required packages
from math import *
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import time
import datetime


########
# Time #
########

start_time = time.time()

#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 2000 ) #The seed does not need to be randomize


######################
# Class and Function #
######################

def convertDate(d):
     new_date = datetime.datetime.strptime(d,"%Y-%m-%dT%H:%M:%S")
     return new_date.date()

#Function to modify the type of a columns which required the name of the dataframe, of the specic column(s) and associated type(s).
def type_modif(df, lst_columns, lst_type):
    for col, typ in zip(lst_columns, lst_type):
        df[col] = df[col].astype(typ)
    return df


################
# Factice Data #
################

begin_Date = 1567418400  # Date == 02/11/2019
end_Date = 1592560800 # Date = 12/06/2020
sec_Day = 86400 # Number of seconds in a day

Login_DB = pd.DataFrame({}).assign(User_ID = int(), Daily_Date_epoch = int(),Daily_Date = object(), Number_Connexion = int()) #Create empty data
                                   
ran = random.randint(1000, 5000) #Define between 10 to 20 users
random_list = [0] * 45 + [1] * 45 + [2] * 10

index = 0   #Variable used to implement values in the DataFrame.
while end_Date >= begin_Date:
    user_ID = 1 #Variable used to implement the ID of each user in the DataFrame
    for user in range(0, ran):
        Login_DB.loc[index, 'User_ID'] = user_ID #Implement the user ID
        Login_DB.loc[index, 'Daily_Date_epoch'] = begin_Date #Implement the Timestamp Date

        d_Date = convertDate(datetime.datetime.fromtimestamp(begin_Date).isoformat()) #Transform the Timestamp date into Human Date
        Login_DB.loc[index, 'Daily_Date'] = d_Date #Implement the Human Date

        if datetime.date(2019, 12, 7) <= d_Date <= datetime.date(2019, 12, 11) or datetime.date(2020, 6, 7) <= d_Date <= datetime.date(2020, 6, 11):
            Login_DB.loc[index, 'Number_Connexion'] = random.randint(4,7)
        else:
            Login_DB.loc[index, 'Number_Connexion'] = random.choice(random_list) #Implement a Random Number (0,5) corresponding to a Number of Connexion 
        
        index += 1 #Implement the index of the DataFrame
        user_ID += 1 #Implement the ID of the User

    begin_Date += sec_Day #Implement by one day

Log_column = ['User_ID', 'Daily_Date_epoch', 'Number_Connexion']
Log_type = [int for col in Log_column]
Login_DB = type_modif(Login_DB, Log_column, Log_type)


###########
# Display #
###########

print(Login_DB.head(10))
print("Total Number of Connexion for the User", Login_DB['User_ID'][Login_DB['User_ID'] == 1].unique(), ':', Login_DB['Number_Connexion'][Login_DB['User_ID'] == 1].sum())


########################
# Data Ressources DONE #
########################

Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))

