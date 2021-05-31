
#Import the required packages
import random
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from numpy import median
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
random.seed( 1050 ) #The seed does not need to be randomize.

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


##################
# Visualizations #
##################


#####################
# Additional Values #
#####################

#Create a list of conditions to define the Niveau of digitalization.
conditions = [
    (Quizz['B'] > 0.80),
    (Quizz['B'] > 0.50) & (Quizz['B'] <= 0.80),
    (Quizz['B'] > 0.20) & (Quizz['B'] <= 0.50),
    (Quizz['B'] <= 0.20),
]

#Create a list of values to assign to each condition from the above list
types = ['Difficile', 'Moyen-Difficile', 'Moyen-Facile', 'Facile']

#Implement the Niveau of digitalization on the dataframe
Quizz['Niveau'] = np.select(conditions, types)
Quizz = Quizz.sort_values(by = 'B', ascending = True)


print(Quizz.head(5))

###########################################################################################
# Répartition du Nombre de Tentatives en function du Niveau de Difficultés de chaque Quiz #
###########################################################################################
"""
#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.boxplot(x = 'Niveau', y = 'Number_Attempts', data = Quizz)
ax.set_xlabel("Niveau de Difficultés", size=16)
ax.set_xticklabels(Quizz['Niveau'].unique(), fontsize=16)
ax.set_ylabel("Nombre de Tentatives", size=16)

fig.suptitle("Répartition du Nombre de Tentatives en function du Niveau de Difficultés de chaque Quiz", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Boxplot of the Distribution of Number of Attempts per Niveau of Difficulty of each Quizz")

#Display Figure
#plt.show()
"""

#########################################################################
# Répartition du Nombre de Réussites par Nombre d'Échecs de chaque Quiz #
#########################################################################
"""
#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 

#Axis
sns.relplot(data=Quizz, x='Number_Success', y = 'Number_Failure', hue = 'Niveau', height=6, aspect=1.5)
plt.title("Nombre de Réussites par le Nombre d'Échecs pour chaque Quiz", size = 18)
plt.xlabel("Nombre de Réussites", size = 16)
plt.ylabel("Nombre d'Échec", size = 16)
plt.tight_layout()

#Save Figure
#fig.savefig(path_Figures + "Relplot of the Number of Success per Number of Failures for each Quizz")

#Display Figure
plt.show()
"""

####
"""
#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.lineplot(data=Quizz, x='Quizz_ID', y = 'Number_Attempts', palette="flare", ax = ax)
ax.set_xlabel("Niveau de Difficultés", size=16)
ax.set_ylabel("Nombre de Tentatives", size=16)

plt.suptitle("Nombre de Réussites par le Nombre d'Échecs pour chaque Quiz", size = 18)
plt.subplots_adjust(
top=0.9,
bottom=0.1,
left=0.05,
right=0.9,
hspace=0.2,
wspace=0.04
)

#Save Figure
#fig.savefig(path_Figures + "Boxplot of the Distribution of Number of Attempts per Level of Difficulty of each Quiz")

#Display Figure
plt.show()
"""

####
"""
lst_randID =  random.sample(range(0, 10), 5)
lst_randID = np.arange(1, 11, 1)
print(lst_randID)

Quizz_randID = Quizz[Quizz.Quizz_ID.isin(lst_randID)]
print(len(Quizz_randID))


plt.bar(Quizz_randID['Quizz_ID'] - 0.25, Quizz_randID['Number_Attempts'], color = 'b', width = 0.25)
plt.bar(Quizz_randID['Quizz_ID'] , Quizz_randID['Number_Success'], color = 'g', width = 0.25)
plt.bar(Quizz_randID['Quizz_ID'] + 0.25, Quizz_randID['Number_Failure'], color = 'r', width = 0.25)
plt.xticks(Quizz_randID['Quizz_ID'])
plt.show()

# plot bars in stack manner
plt.bar(Quizz['Quizz_ID'], Quizz['Number_Attempts'], color='r')
plt.bar(Quizz['Quizz_ID'], Quizz['Number_Success'], color='g')
plt.bar(Quizz['Quizz_ID'], Quizz['Number_Failure'], color='b')
plt.show()
"""



##############################################################
# Difficulté et Nombre de Tentative d'un échantillon de Quiz #
##############################################################
"""
lst_randID = np.arange(1, 26, 1)
Quizz_randID = Quizz[Quizz.Quizz_ID.isin(lst_randID)].sort_values(by = "Quizz_ID", ascending = True)
print(len(Quizz_randID))

#Build the figure
sns.set_theme()
sns.set_style("white")

#Set the size of the figures 
fig, ax1 = plt.subplots(figsize=(16, 9))
ax2 = ax1.twinx()

#Define the Plots
sns.lineplot(data = Quizz_randID['B'], marker='o', sort = False, color = 'black', ax=ax1)
sns.barplot(data = Quizz_randID, x='Quizz_ID', y='Number_Attempts', ci = 95, hue = 'Niveau', palette = 'Set1', alpha = 0.6, dodge = False, ax=ax2)

#Axis
ax1.set_ylabel("Difficulté du Quiz (théta)", size=16)
ax1.set_xlabel("Identifiant du Quiz", size=16)
ax2.set_ylabel("Nombre de Tentatives", size=16)
ax2.legend(loc='center', bbox_to_anchor=(1.15, 0.5), shadow=True, title = 'Niveau')

#Last Setting
fig.suptitle("Nombre de Tentative et Difficulté d'un échantillon de Quiz", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Difficulté et Nombre de Tentative d'un échantillon de Quiz")

#Display
plt.show()
"""


##############################################################
# Difficulté et Nombre de Tentative d'un échantillon de Quiz #
##############################################################

lst_randID = np.arange(1, 26, 1)
Quizz_randID = Quizz[Quizz.Quizz_ID.isin(lst_randID)].sort_values(by = "Quizz_ID", ascending = True)
print(len(Quizz_randID))

#Build the figure
sns.set_theme()
sns.set_style("white")

#Set the size of the figures 
fig, ax1 = plt.subplots(figsize=(16, 9))
ax2 = ax1.twinx()

#Define the Plots
sns.lineplot(data = Quizz_randID['B'], marker='o', sort = False, color = 'black', ax=ax1)
sns.barplot(data = Quizz_randID, x='Quizz_ID', y='Number_Attempts', ci = 95, hue = 'Niveau', palette = 'Set1', alpha = 0.6, dodge = False, ax=ax2)

#Axis
ax1.set_ylabel("Difficulté du Quiz (B)", size=16)
ax1.set_xlabel("Identifiant du Quiz", size=16)
ax2.set_ylabel("Nombre de Tentatives", size=16)
ax2.legend(loc='center', bbox_to_anchor=(1.15, 0.5), shadow=True, title = 'Niveau')

#Last Setting
fig.suptitle("Nombre de Tentative et Difficulté d'un échantillon de Quiz", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Difficulté et Nombre de Tentative d'un échantillon de Quiz")

#Display
plt.show()
