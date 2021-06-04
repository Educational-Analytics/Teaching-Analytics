
#Import the required packages
import random
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from numpy import median
import seaborn 
from seaborn import palettes

###################################
#Define the Path and Folders Name #
###################################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
folder_names = ['Data', 'Data-Viz', 'Figures'] #Determine the name of the sub folders for the factice example.
keywords = ['Reingenieurie', 'Factice-Example'] #Determine the keywords that will take the folder position.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures = glob_path + '/' + folder_names[2] + '/' #Path of the Figures Folder


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 1051 ) #The seed does not need to be randomize.

######################
# Class and Function #
######################


#################################
# Import the required Data file #
#################################

Text = pd.read_csv(path_Data + 'Test_text.csv')
print(Text.head(5))

Text_Ecriture = Text[Text['Action'] == 'Ecriture']
Text_Effacer = Text[Text['Action'] == 'Effacer']
"""
# plot bars in stack manner
plt.bar(Text_Ecriture['Ligne'] + 0, Text_Ecriture['Action'], color='r', width= 0.5)
plt.bar(Text_Effacer['Ligne'] + 0.5, Text_Effacer['Action'], color='r', width= 0.5)
plt.xticks(Text['Ligne'])
plt.show()

print(Text_Effacer)
"""
sns.displot(data=Text, x="Ligne", hue="Action", kde = True)
plt.xticks(Text['Ligne'])
plt.show()
