
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
folder_names = ['Data', 'Data-Viz', 'Figures', 'Vrs_English', 'Vrs_Français'] #Determine the name of the sub folders for the factice example.
keywords = ['°° Reingenierie', 'Factice-Example'] #Determine the keywords that will take the folder position.
glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures_EN = glob_path + '/' + folder_names[2] + '/' + folder_names[3] + '/' #Path of the English Figures Folder 
path_Figures_FR = glob_path + '/' + folder_names[2] + '/' + folder_names[4] + '/' #Path of the French Figures Folder 


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 2215 ) #The seed does not need to be randomize.

######################
# Class and Function #
######################

#Function to display the values above the barplots.
def show_values_on_bars(axs):
    def _show_on_single_plot(ax):        
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height() + 1
            value = '{:.0f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center") 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)


#################################
# Import the required Data file #
#################################

Quizz = pd.read_csv(path_Data + 'Quizzes.csv')
print(Quizz.head(5))


##################
# Visualizations #
##################

###################################################################################################
# 1° - HEATMAP
# Percentage of Success for each Quiz of the Artificial University Departments from 2015 to 2020  #
# Pourcentage de Réussite pour chaque Quiz des Départements de l'Université Factice de 2015 à 2020 #
###################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Quizz_Depts = Quizz.groupby(['Department', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Department", "Year", "Success_Prct")

#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 10), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Years", size=18)
ax.set_ylabel("University Departments", size=18)
plt.text(1.2,0.5,'Percentage of Success [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Final Settings
fig.suptitle("Percentage of Success for each Quiz of the University Departments from 2015 to 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_EN  + "1° - Heatmap - Percentage of Success for each Quiz of the University Departments from 2015 to 2020")

#Display the Figure
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Quizz_Depts = Quizz.groupby(['Departement', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Departement", "Year", "Success_Prct")

#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 10), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Départements de l'Université", size=18)
plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Final Settings
fig.suptitle("Pourcentage de Réussite aux Quiz de chaque Département de l'Université de 2015 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_FR  + "1° - Heatmap - Pourcentage de Réussite aux Quiz de chaque Département de l'Université de 2015 à 2020")

#Display the Figure
plt.show()
"""

###################################################################################################################
# 2° - HEATMAP
# Percentage of Success for each Quiz of the Marketing Department of the Artificial University from 2015 to 2020  #
# Pourcentage de Réussite pour chaque Quiz du Département de Marketing de l'Université Factice de 2015 à 2020     #
###################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Quizz_Depts = Quizz[Quizz['Department'] == "Marketing"]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Years", size=18)
ax.set_ylabel("Modules of the Marketing Département", size=18)
ax.set_yticklabels(["Morphological Transformation", "Functional Lexical Grammar", "Grammar and Syntax", "Introduction to the Language Study", "Neology"])
plt.text(1.2,0.5,'Percentage of Success [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
#Final Settings
fig.suptitle("Percentage of Success for the Quizzes of some Modules of the Marketing Department from 2015 to 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_EN + "2° - Heatmap - Percentage of Success for the Quizzes of some Modules of the Marketing Department from 2015 to 2020")

#Display the Figure
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Quizz_Depts = Quizz[Quizz['Departement'] == "Marketing"]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Modules du Département de Marketing", size=18)
plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Final Settings
fig.suptitle("Pourcentage de Réussite aux Quiz de certains modules du Département de Marketing de 2015 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_FR + "2° - Heatmap - Pourcentage de Réussite aux Quiz de certains modules du Département de Marketing de 2015 à 2020")

#Display the Figure
plt.show()
"""


#####################################################################################################################
# 3° - HEATMAP
# Percentage of Success for each Quiz of the Mathematics Department of the Artificial University from 2015 to 2020  #
# Pourcentage de Réussite pour chaque Quiz du Département de Mathématique de l'Université Factice de 2015 à 2020    #
#####################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Quizz_Depts = Quizz[Quizz['Department'] == "Mathematics"]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Years", size=18)
ax.set_ylabel("Modules of the Mathematics Département", size=18)
ax.set_yticklabels(["Linear Algebra", "Derivative", "Analytical Geometry", "Integral", "Pre-Hilbertiens and Hilbertiens Spaces"])
plt.text(1.2,0.5,'Percentage of Success [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)

#Final Settings
fig.suptitle("Percentage of Success for the Quizzes of some Modules of the Mathematics Department from 2015 to 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_EN + "3° - Heatmap - Percentage of Success for the Quizzes of some Modules of the Mathematics Department from 2015 to 2020")

#Display the Figure
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Quizz_Depts = Quizz[Quizz['Departement'] == "Mathématiques"]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Modules du Département de Mathématiques", size=18)
plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Final Settings
fig.suptitle("Pourcentage de Réussite aux Quiz de certains Modules du Département de Mathématiques de 2015 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_FR + "3° - Heatmap - Pourcentage de Réussite aux Quiz de certains Modules du Département de Mathématiques de 2015 à 2020")

#Display the Figure
plt.show()
"""



###################################################################################################################################
# 3_5° - HEATMAP
# Pourcentage de Réussite des Quiz de certains Chapitres du Département de Mathématique de l'Université Factice de 2015 à 2020    #
###################################################################################################################################

#####################
# Version Française #
#####################
"""
#Build the Data
Quizz_Depts = Quizz[Quizz['Departement'] == "Mathématiques"]
Quizz_Depts = Quizz_Depts.groupby(['Chapter', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Chapter", "Year", "Success_Prct")


#Build the figure
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 5),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Chapitres du Département de Mathématiques", size=18)
plt.text(1.2,0.5,'Pourcentage de Réussite [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=8, rotation = 0)

#Final Settings
fig.suptitle("Pourcentage de Réussite aux Quiz de certains Chapitres du Département de Mathématiques de 2015 à 2020", ha = 'center', size=18)
plt.subplots_adjust(top=0.93,bottom=0.075,left=0.36,right=1,hspace=0.2,wspace=0.04)

#Save Figure
fig.savefig(path_Figures_FR + "3_5° - Heatmap - Pourcentage de Réussite aux Quiz de certains Chapitres du Département de Mathématiques de 2015 à 2020")

#Display the Figure
plt.show()
"""


###########################################################################
# 3° - BARPLOTS
# Distribution of the Slip/Guess on the Type and Difficulty of each Quiz  #
# Pourcentage de Réussite pour chaque Quiz du Département de Mathématique de l'Université Factice de 2015 à 2020    #
#####################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 2, figsize=(16, 9), sharey=True)

Quizz['Correct_Difficulty_Rank'] = Quizz['Correct_Difficulty'].replace(['Facile', 'Moyen', 'Difficile'],[0, 1, 2])
Quizz['Quizz_Type_Rank'] = Quizz['Quizz_Type'].replace(['QCU', 'QCM', 'QROC', 'QO'],[0, 1, 2, 3])
Quizz = Quizz.sort_values(by = ['Correct_Difficulty_Rank', 'Quizz_Type_Rank'], ascending = True)

sns.barplot(x="Quizz_Type", y="Guess", hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[0], capsize=.2)
ax[0].set_title("Distribution of the value of the «Guess», \n depending on the Type and Dificulty of the Quizzes", size=14)
ax[0].set_xlabel("Types of Quizzes", size=13)
ax[0].set_ylabel("Values", size=15)
ax[0].get_legend().remove()

sns.barplot(x="Quizz_Type", y="Slip",  hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[1], capsize=.2)
ax[1].set_title("Distribution of the value of the «Slip», \n depending on the Type and Dificulty of the Quizzes", size=14)
ax[1].set_xlabel("Types of Quizzes", size=13)
ax[1].set_ylabel("", size=15)   

ax[1].legend(loc='center', bbox_to_anchor=(1.10, 0.5), shadow=True, title = 'Difficulté')

plt.ylim([0, 1])
fig.suptitle("Distribution of the values of the «Guess» and «Slip» depending on the Type and Dificulty of the whole Quizzes", ha = 'center', size=16)
fig.subplots_adjust(top=0.875, bottom=0.07, left=0.05, right=0.915, hspace=0.2, wspace=0.05)

#Save Figure
fig.savefig(path_Figures_EN + "4° - Barplot - Distribution of the values of the Guess and Slip depending on the Type and Dificulty of the Quizzes")

#Display the plots
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 2, figsize=(16, 9), sharey=True)

Quizz['Correct_Difficulty_Rank'] = Quizz['Correct_Difficulty'].replace(['Facile', 'Moyen', 'Difficile'],[0, 1, 2])
Quizz['Quizz_Type_Rank'] = Quizz['Quizz_Type'].replace(['QCU', 'QCM', 'QROC', 'QO'],[0, 1, 2, 3])
Quizz = Quizz.sort_values(by = ['Correct_Difficulty_Rank', 'Quizz_Type_Rank'], ascending = True)

sns.barplot(x="Quizz_Type", y="Guess", hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[0], capsize=.2)
ax[0].set_title("Répartition des valeurs du «Guess», \n en fonction du Type et du Niveau de Difficulty des Quiz", size=14)
ax[0].set_xlabel("Types des Quiz", size=13)
ax[0].set_ylabel("Valeurs", size=15)
ax[0].get_legend().remove()

sns.barplot(x="Quizz_Type", y="Slip",  hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[1], capsize=.2)
ax[1].set_title("Répartition des valeurs du «Slip», \n en fonction du Type et du Niveau de Difficulty des Quiz", size=14)
ax[1].set_xlabel("Types des Quiz", size=13)
ax[1].set_ylabel("", size=15)   

ax[1].legend(loc='center', bbox_to_anchor=(1.10, 0.5), shadow=True, title = 'Difficulté')

plt.ylim([0, 1])
fig.suptitle("Répartition des valeurs du «Guess» et du «Slip» en fonction du Type et du Niveau de Difficulté de l'Intégralité des Quiz ", ha = 'center', size=16)
fig.subplots_adjust(top=0.875, bottom=0.07, left=0.05, right=0.915, hspace=0.2, wspace=0.05)

#Save Figure
fig.savefig(path_Figures_FR + "4° - Barplot - Répartition du Guess et Slip en fonction du Type et Niveau de Difficulté de l'Intégralité des Quiz")

#Display the plots
plt.show()
"""


###############
# END Program #
###############