
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
keywords = ['Reingenierie', 'Factice-Example'] #Determine the keywords that will take the folder position.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures = glob_path + '/' + folder_names[2] + '/' #Path of the Figures Folder


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



#####################
# Additional Values #
#####################


############################################################################
# (HEATMAP) Success Percentage of Quizzes per Department from 2015 to 2020 #
############################################################################
"""
Quizz_Depts = Quizz.groupby(['Departement', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Departement", "Year", "Success_Prct")

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 10), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

#Axis
ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Année", size=16)
ax.set_ylabel("Départements de l'Université Factice", size=16)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Last Setting
fig.suptitle("Pourcentage de Success aux Quiz de chaque Département de l'Université Factice de 2015 à 2020", ha = 'center', size=18)

fig.subplots_adjust(
top=0.9,
bottom=0.1,
left=0.2,
right=1,
hspace=0.2,
wspace=0.2
)

#Save Figure
# fig.savefig(path_Figures + "1° Heatmap of the Quizz Success Percentage for the Factice University Departments from 2015 to 2020")

#Save CSV
Quizz_Depts.to_csv(path_DataViz + 'Pivot_Quiz_Depts_Years.csv')

#Display the Figure
plt.show()
"""

###############################################################################
# (HEATMAP) Percentage of Success for a Factice Departments from 2015 to 2020 #
###############################################################################
"""
Depts = random.choice(Quizz['Departement'])
Quizz_Depts = Quizz[Quizz['Departement'] == Depts]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Année", size=16)
ax.set_ylabel("Module du Departement de " + Depts, size=16)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=12, rotation = 0)

#Last Setting
fig.suptitle("Pourcentage de Réussite aux Quiz de certains modules du Département d'" + Depts + " de 2015 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.92, bottom=0.075, left=0.2, right=1, hspace=0.2, wspace=0.2)


#Save Figure
fig.savefig(path_Figures + "2° Heatmap of the Quizz Success Percentage of each Module for the Departments of " + Depts + " from 2015 to 2020")

#Save CSV
Quizz_Depts.to_csv(path_DataViz + 'Pivot_QuizModule' + Depts + '_Years.csv')

#Display the Figure
plt.show()
"""

##########################################################################################
# (HEATMAP) Percentage of Success for module of the Department of Math from 2015 to 2020 #
##########################################################################################
"""
Depts = 'Mathematique'
Quizz_Depts = Quizz[Quizz['Departement'] == Depts]
Quizz_Depts = Quizz_Depts.groupby(['Module', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Module", "Year", "Success_Prct")


#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 15})
ax.set_xlabel("Année", size=16)
ax.set_ylabel("Module du Departement de " + Depts, size=16)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=12, rotation = 0)

#Last Setting
fig.suptitle("Pourcentage de Réussite aux Quiz de certains modules du Département de " + Depts + " de 2015 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.92, bottom=0.075, left=0.25, right=1, hspace=0.2, wspace=0.2)


#Save Figure
fig.savefig(path_Figures + "3° Heatmap of the Quizz Success Percentage of each Module for the Departments of " + Depts + " from 2015 to 2020")

#Save CSV
Quizz_Depts.to_csv(path_DataViz + 'Pivot_QuizModule_' + Depts + '_Years.csv')

#Display the Figure
plt.show()
"""

############################################################################################
# (HEATMAP) Percentage of Success for chapters of the Department of Math from 2015 to 2020 #
############################################################################################
"""
Depts = 'Mathematique'
Quizz_Depts = Quizz[Quizz['Departement'] == Depts]
Quizz_Depts = Quizz_Depts.groupby(['Chapter', 'Year'])['Success_Prct'].mean().reset_index()
Quizz_Depts['Success_Prct'] = round(Quizz_Depts['Success_Prct']).astype(int)
Quizz_Depts_pivot = Quizz_Depts.pivot("Chapter", "Year", "Success_Prct")


#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Quizz_Depts['Success_Prct'].min(), Quizz_Depts['Success_Prct'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Quizz_Depts_pivot, annot= True, fmt="d", linewidths=1, cmap="Spectral", cbar_kws=cbar_kws)
ax.set_xlabel("Année", size=16)
ax.set_ylabel("Chapitre du Departement de " + Depts, size=16)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=10, rotation = 0)

#Last Setting
fig.suptitle("Pourcentage de Réussite aux Quiz de certains chapitres du Département de " + Depts + " de 2015 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.92, bottom=0.075, left=0.45, right=1, hspace=0.2, wspace=0.2)


#Save Figure
fig.savefig(path_Figures + "4° Heatmap of the Quizz Success Percentage of each Chapter for the Departments of " + Depts + " from 2015 to 2020")

#Save CSV
Quizz_Depts.to_csv(path_DataViz + 'Pivot_QuizChapter_' + Depts + '_Years.csv')

#Display the Figure
plt.show()
"""

###############################################################################
# Barplot of the Slip/Guess depending on the Type and Difficulty of each Quiz #
###############################################################################

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 2, figsize=(16, 9), sharey=True)

Quizz['Correct_Difficulty_Rank'] = Quizz['Correct_Difficulty'].replace(['Facile', 'Moyen', 'Difficile'],[0, 1, 2])
Quizz['Quizz_Type_Rank'] = Quizz['Quizz_Type'].replace(['QCU', 'QCM', 'QROC', 'QO'],[0, 1, 2, 3])
Quizz = Quizz.sort_values(by = ['Correct_Difficulty_Rank', 'Quizz_Type_Rank'], ascending = True)

sns.barplot(x="Quizz_Type", y="Guess", hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[0], capsize=.2)
ax[0].set_title("Répartition du 'Guess' \n en fonction du Type et du Niveau de Difficulty des Quiz", size=14)
ax[0].set_xlabel("Type des Quiz", size=13)
ax[0].set_ylabel("Répartition", size=15)
ax[0].get_legend().remove()

sns.barplot(x="Quizz_Type", y="Slip",  hue = 'Correct_Difficulty', data=Quizz, palette="Spectral", ax = ax[1], capsize=.2)
ax[1].set_title("Répartition du 'Slip' \n en fonction du Type et du Niveau de Difficulty des Quiz", size=14)
ax[1].set_xlabel("Type des Quiz", size=13)
ax[1].set_ylabel("", size=15)   

ax[1].legend(loc='center', bbox_to_anchor=(1.10, 0.5), shadow=True, title = 'Difficulté')

plt.ylim([0, 1])
fig.suptitle("Répartition du «Guess» et du «Slip» en fonction du Type et du Niveau de Difficulté de l'Intégralité des Quiz ", ha = 'center', size=16)
fig.subplots_adjust(top=0.875, bottom=0.07, left=0.05, right=0.915, hspace=0.2, wspace=0.05)

#Save Figure
fig.savefig(path_Figures + "5° Barplot of the Distribution of Slip_Guess depending on the Type and Difficulty of each Quiz")

#Display the plots
plt.show()

###############################################################################
#  #
###############################################################################

"""
Depts = random.choice(Quizz['Departement'])
Quizz_Depts = Quizz[Quizz['Departement'] == Depts]
Chapts = random.choice(Quizz_Depts['Chapter_ID'])
Quizz_ChapDepts =  Quizz_Depts[Quizz_Depts['Chapter_ID'] == Chapts]
Quizz_ChapDepts = Quizz_ChapDepts.groupby('Quizz_ID')['Avg_Attempts'].mean().reset_index()


# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='white')

label_quiz = ['Quiz ' + str(quiz_ID) for quiz_ID in Quizz_ChapDepts['Quizz_ID']]

def absolute_value(val):
    a  = np.round(val/100.*Quizz_ChapDepts['Avg_Attempts'].sum(), 2)
    return a

# Give color names
plt.pie(Quizz_ChapDepts['Avg_Attempts'], labels=label_quiz, autopct= absolute_value, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' }    )
p = plt.gcf()
p.gca().add_artist(my_circle)

# Show the graph
plt.show()

"""
###############################################################################
#  #
###############################################################################
"""
Quiz_ID = random.choice(Quizz['Quizz_ID'])
Quizz_Identif = Quizz[Quizz['Quizz_ID'] == Quiz_ID]


# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='white')

def absolute_value(val):
    a  = np.round(val/100.*Quizz_Identif['Avg_Attempts'].sum(), 2)
    return a

# Give color names
plt.pie(Quizz_Identif['Avg_Attempts'], labels=Quizz_Identif['Year'], autopct= absolute_value, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' }    )
p = plt.gcf()
p.gca().add_artist(my_circle)

# Show the graph
plt.show()
"""

#############
# Wordcloud #
#############

"""text = " ".join([Predic for Predic in Quizz['Quizz_Type']])
print(text)

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, max_words=3).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()"""
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
"""


