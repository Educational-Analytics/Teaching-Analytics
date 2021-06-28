#########################################
# Resources and Courses Digitalization #        
#########################################

#Import the required packages
import random
import math
import numpy as np
from numpy.lib.arraysetops import unique
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

###################################
#Define the Path and Folders Name #
###################################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
folder_names = ['Data', 'Data-Viz', 'Figures', 'Vrs_English', 'Vrs_Français'] #Determine the name of the sub folders for the factice example.
keywords = ['° Digit_Resources', 'Factice-Example'] #Determine the keywords that will take the folder position.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_Data = glob_path + '/' + folder_names[0] + '/'  #Path of the Data Folder
path_DataViz = path_Data + folder_names[1] + '/'  #Path of the DataViz Folder
path_Figures_EN = glob_path + '/' + folder_names[2] + '/' + folder_names[3] + '/' #Path of the English Figures Folder 
path_Figures_FR = glob_path + '/' + folder_names[2] + '/' + folder_names[4] + '/' #Path of the French Figures Folder 

#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 274825 ) #The seed does not need to be randomize


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

Resources = pd.read_csv(path_Data + 'Resources.csv')


##################
# Visualizations #
##################

############################################################################################################
# 1° - HEATMAP
# Percentage of Digitalisation for each Module of the Artificial University Departments from 2013 to 2020  #
# Pourcentage de Digitalisation pour chaque Module des Départements de l'Université Factice de 2013 à 2020 #
############################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Digitalization_Depts = Resources.groupby(['Department', 'Year'])['Digitalization_Ressource_Percent'].mean().reset_index()
Digitalization_Depts['Digitalization_Ressource_Percent'] = round(Digitalization_Depts['Digitalization_Ressource_Percent']).astype(int)
Digitalization_Depts_pivot = Digitalization_Depts.pivot("Department", "Year", "Digitalization_Ressource_Percent")

#Build the Figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Digitalization_Depts['Digitalization_Ressource_Percent'].min(), Digitalization_Depts['Digitalization_Ressource_Percent'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Digitalization_Depts_pivot, annot= True, fmt="d", linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 16})
ax.set_xlabel("Years", size=18)
ax.set_ylabel("University Departments", size=18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)
plt.text(1.2,0.5,'Percentage of Digitalisation [%]',horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)

#Final Setting
fig.suptitle("Percentage of Digitalisation for each Module of the University Departments from 2013 to 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_EN + "1° - Heatmap - Percentage of Digitalisation for each Module of the University Departments from 2013 to 2020")

#Display the Figure
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Digitalization_Depts = Resources.groupby(['Departement', 'Year'])['Digitalization_Ressource_Percent'].mean().reset_index()
Digitalization_Depts['Digitalization_Ressource_Percent'] = round(Digitalization_Depts['Digitalization_Ressource_Percent']).astype(int)
Digitalization_Depts_pivot = Digitalization_Depts.pivot("Departement", "Year", "Digitalization_Ressource_Percent")

#Build the Figure
#Primary Settings
sns.set(font_scale=1.4) # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
cbar_kws = {"orientation":"vertical", 
            "shrink":1,
            'extend':'both', 
            'ticks': np.arange(Digitalization_Depts['Digitalization_Ressource_Percent'].min(), Digitalization_Depts['Digitalization_Ressource_Percent'].max(), 3),
           } # color bar keyword arguments

ax = sns.heatmap(Digitalization_Depts_pivot, annot= True, fmt="d", linewidths=1, linecolor="w", cmap="Spectral", cbar_kws=cbar_kws, annot_kws={'size': 16})
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Departements de l'Université", size=18)
plt.text(1.2,0.5,'Pourcentage de Digitalisation [%]', horizontalalignment='right', verticalalignment='center', transform = ax.transAxes, rotation = 90, fontsize = 18)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14, rotation = 0)

#Final Setting
fig.suptitle("Pourcentage de Digitalisation de chaque Module des Départements de l'Université de 2013 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_FR + "1° - Heatmap - Pourcentage de Digitalisation de chaque Module des Départements de l'Université de 2013 à 2020")

#Display the Figure
plt.show()
"""


############################################################################################################################################
# 2° - BOXPLOTS
# Distribution of the Digitalization Percentage for each Module of the Factice University Department of Computer Science from 2013 to 2020 #
# Répartition du Pourcentage de Digitalisation pour chaque Module du Département d'Informatique de l'Université Factice de 2013 à 2020     #
############################################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Digitalization_CptScs = Resources[Resources['Department'] == 'Computer Science']

#Build the Figure
#Primary Settings
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.boxplot(x="Year", y="Digitalization_Ressource_Percent", hue = "Year", dodge = False, data=Digitalization_CptScs, palette = 'Spectral')
ax.set_xlabel("Years", size=18)
ax.set_ylabel("Percentage of Digitalisation [%]", size=18)
ax.set_xticklabels(Digitalization_CptScs['Year'].unique(), fontsize=16)
ax.get_legend().remove()

#Final Setting
fig.suptitle("Distribution of the Digitalisation Percentage for each Module of the University Department of Computer Science from 2013 to 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_EN + "2° - Boxplots - Distribution of the Digit Prct for each Module of the Department of Computer Science from 2013 to 2020")

#Display the Figure
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Digitalization_CptScs = Resources[Resources['Departement'] == 'Informatique']

#Build the Figure
#Primary Settings
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.boxplot(x="Year", y="Digitalization_Ressource_Percent", hue = "Year", dodge = False, data=Digitalization_CptScs, palette = 'Spectral')
ax.set_xlabel("Années", size=18)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=18)
ax.set_xticklabels(Digitalization_CptScs['Year'].unique(), fontsize=16)
ax.get_legend().remove()

#Final Setting
fig.suptitle("Répartition du Pourcentage de Digitalisation pour chaque Module du Département d'Informatique de 2013 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures_FR + "2° - Boxplots - Répartition du Prct de Digit pour chaque Module du Département d'Informatique de 2013 à 2020")

#Display the Figure
plt.show()
"""
            

################################################################################################################################################
# 3° - Barplots
# Percentage of Digitalisation for each Module of all Teachers from the Artificial University Department of Computer Science from 2017 to 2020 #  
# Pourcentage de Digitalisation de chaque Module des Enseignants du Département d'Informatique de l'Université Factice de 2017 à 2020          #         
################################################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Department'] == 'Computer Science']
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2015]
#Build the Figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.barplot(x ="Teacher_Name", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral", ci = 50, capsize=0.1)
ax.set_xlabel("Teachers Name ", size=18)
ax.set_ylabel("Percentage of Digitalisation [%]", size=18)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
#show_values_on_bars(ax)

#Final Setting
plt.ylim([0, 55]) #Set the y-axis lim
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
fig.suptitle("Distribution of the Digitalisation Percentage for each Module of all Teachers from the Department of Computer Science from 2017 to 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.900,
                    bottom=0.075,
                    left=0.060,
                    right=0.9,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures_EN + "3° - Barplots - Distribution of the Digit Prct of all Teachers from the Department of Computer Science from 2017 to 2020")
#Display
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Departement'] == 'Informatique']
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2015]

#Build the Figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.barplot(x ="Teacher_Name", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral", ci = 50, capsize=0.1)
ax.set_xlabel("Nom des Enseignants ", size=18)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=18)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
#show_values_on_bars(ax)

#Final Setting
plt.ylim([0, 55]) #Set the y-axis lim
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
fig.suptitle("Répartition du Pourcentage de Digitalisation de chaque Module des Enseignants du Département d'Informatique de 2015 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.900,
                    bottom=0.075,
                    left=0.060,
                    right=0.9,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures_FR + "3° - Barplots - Répartition du Pourcentage de Digitalisation des Enseignants du Département d'Informatique de 2015 à 2020")

#Display
plt.show()
"""


##############################################################################################################################################
# 4° - Barplots
# Percentage of Digitalisation for some Modules of Mr ROGIER from the Artificial University Department of Computer Science from 2013 to 2020 #  
# Pourcentage de Digitalisation de certains Modules de Mr ROGIER du Département d'Informatique de l'Université Factice de 2013 à 2020        #         
##############################################################################################################################################

###################
# ENGLISH Version #
###################
"""
#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Course_ID'].isin([60,64,41,68,70])]
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2015]
Module_Title_EN = ["Structure of the Computer", "Language Processing", "Concept of Algorithm", "Basic Instruction", "Computer Network"]
Digitalization_Teach_CptSc['Module_Title'] = Digitalization_Teach_CptSc['Course_ID'].replace([60,64,41,68,70], Module_Title_EN)

#Build the Figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.barplot(x ="Course_ID", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral")
ax.set_xlabel("Modules", size=18)
ax.set_ylabel("Percentage of Digitalisation [%]", size=18)
ax.set_xticklabels(unique(Digitalization_Teach_CptSc['Module_Title']), size = 14)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
show_values_on_bars(ax)

#Final Setting
plt.ylim([0, 100]) #Set the y-axis lim
plt.setp(ax.get_yticklabels(), fontsize=12)
fig.suptitle("Percentage of Digitalisation for some Modules of Mr ROGIER from the University Department of Computer Science from 2015 to 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.925,
                    bottom=0.075,
                    left=0.060,
                    right=0.9,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures_EN + "4° - Barplots - Percentage of Digitalisation of Mr ROGIER from the Department of Computer Science from 2015 to 2020")
#Display
plt.show()
"""

#####################
# Version Française #
#####################
"""
#Build the Data
Digitalization_Teach_CptSc = Resources[Resources['Course_ID'].isin([60,64,41,68,70])]
Digitalization_Teach_CptSc = Digitalization_Teach_CptSc[Digitalization_Teach_CptSc['Year'] >= 2015]
Module_Title_FR = ["Structure de l'Ordinateur", "Traitement de Texte", "Notion d'Algorithme", "Instruction de Base", "Noion de Reseau Informatique"]
Digitalization_Teach_CptSc['Module_Title'] = Digitalization_Teach_CptSc['Course_ID'].replace([60,64,41,68,70], Module_Title_FR)

#Build the Figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.barplot(x ="Course_ID", y = 'Digitalization_Ressource_Percent', data = Digitalization_Teach_CptSc, hue = "Year", palette = "Spectral")
ax.set_xlabel("Modules", size=18)
ax.set_ylabel("Pourcentage de Digitalisation [%]", size=18)
ax.set_xticklabels(unique(Digitalization_Teach_CptSc['Module_Title']), size = 14)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
show_values_on_bars(ax)

#Final Setting
plt.ylim([0, 100]) #Set the y-axis lim
plt.setp(ax.get_yticklabels(), fontsize=12)
fig.suptitle("Pourcentage de Digitalisation de certains Modules de Mr ROGIER du Département d'Informatique de 2015 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.925,
                    bottom=0.075,
                    left=0.060,
                    right=0.9,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures_FR + "4° - Barplots - Pourcentage de Digitalisation de Mr ROGIER du Département d'Informatique de 2015 à 2020")

#Display
plt.show()
"""


###############
# END Program #
###############