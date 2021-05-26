#########################################
# Ressources and Courses Digitalization #        
#########################################

#Import the required packages
import random
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

###################################
#Define the Path and Folders Name #
###################################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
folder_names = ['Data', 'Data-Viz', 'Figures'] #Determine the name of the sub folders for the factice example.
keywords = ['Ressources', 'Factice-Example'] #Determine the keywords that will take the folder position.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures = glob_path + '/' + folder_names[2] + '/' #Path of the Figures Folder


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 1050 ) #The seed does not need to be randomize


######################
# Class and Function #
######################


#################################
# Import the required Data file #
#################################

Ressources = pd.read_csv(path_Data + 'Ressources_Sequence.csv')


##################
# Visualizations #
##################

########################################################
# (HISTOGRAM) Distribution of the number of Ressources #
########################################################

#Set the figure
fig, ax = plt.subplots(1, 1, figsize=(10, 5), sharey=True)

#Build the figure
ax = plt.hist(Ressources['Course_Ressources'], color = 'black', edgecolor = 'white')

#Axis 
plt.xlabel('Number of Ressources', size = 12)
plt.ylabel('Count', size = 12)

#Last Setting
fig.suptitle("Distribution of the Number of Ressources", ha = 'center', size=15, fontweight='bold')
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Histogram of the Number of Ressources")

#Display the Figure
plt.show()


#######
#     #
#######