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
from wordcloud import WordCloud
###################################
#Define the Path and Folders Name #
###################################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
folder_names = ['Data', 'Data-Viz', 'Figures'] #Determine the name of the sub folders for the factice example.
keywords = ['Reingenierie', 'Factice-Example'] #Determine the keywords that will take the folder position.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures = glob_path + '/' + folder_names[2] + '/' #Path of the Figures Folder


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
#random.seed() #The seed does not need to be randomize.

########################
dept = []
mod = []
chapter = []
quizz = []

depts_type = ['Art', 'Droit', 'Economie', 'Histoire', 'Informatique', 'Ingenierie', 'Langues', 'Management', 'Mathematique', 'Philosophie', 'Sociologie'] #Define a list of Departements
modules = [
           [], #Art
           [], #Droit
           ["Introduction a l'economie", "Ressources Humaines", "Consommation"], #Economie
           [], #Histoire
           [], #Informatique
           [], #Ingenierie
           [], #Langues
           [], #Management
           ["Fonction Affine", "Second Degré"], #Mathematique
           [], #Philosophie
           [], #Sociologie
          ]    

dep = 'Economie'
condition = [dep == 'Art', dep == 'Droit', dep == 'Economie', dep == 'Histoire', dep == 'Informatique', dep == 'Ingenierie', dep == 'Langues', dep == 'Management', dep == 'Mathematique', dep == 'Philosophie', dep == 'Sociologie']
                             
for module in modules[np.select(condition, [i for i in range(0, len(condition))])]:
    rand_chap = random.randint(3, 7)
    rand_quiz = random.randint(5, 15)
    for chap in range(1, rand_chap + 1):
        for quiz in range(1, rand_quiz + 1):
            dept.append(dep)
            mod.append(module)
            chapter.append(chap)
            quizz.append(quiz)

test_db = pd.DataFrame({'Departement': dept,
                        'Module': mod,
                        'Chapter_ID': chapter,
                        'Quizz_ID': quizz      
                        })
print(test_db)
