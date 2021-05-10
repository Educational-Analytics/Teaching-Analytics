################################################################################################
# Ratio of Digitalization of an University (Department, Teaching-research Personnel) (Factice) #        
################################################################################################

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
keywords = ['Digitalization', 'Factice-Example'] #Determine the keywords that will take the folder position.

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

Digitalization = pd.read_csv(path_Data + 'Digitalization.csv')

#Select a departments to build a figure
ran_dep = random.randint(0, len(Digitalization['Department'].unique())-1)
dep = Digitalization['Department'].unique()[ran_dep]
print(dep)

##################
# Visualizations #
##################

#########################################################################################
# Percentage of Digitalization for the Factice University Departments from 2013 to 2020 #
#########################################################################################
"""
Digitalization_Departs = Digitalization.groupby(['Department', 'Year'])['Digit_Percentage'].mean().reset_index()
Digitalization_Departs['Digit_Percentage'] = round(Digitalization_Departs['Digit_Percentage']).astype(int)

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.boxplot(x="Department", y="Digit_Percentage", hue = "Year", data=Digitalization)
ax.set_xlabel("Departments", size=13)
ax.set_ylabel("Digitalization (%)", size=13)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Years')

#Last Setting
fig.suptitle("Distribution of the Digitalization Percentage for the Factice University Departments from 2013 to 2020", ha = 'center', size=16, fontweight='bold')
fig.tight_layout()
fig.subplots_adjust(right=0.91)


#Save Figure
fig.savefig(path_Figures + "Boxplot of the Digitalization for the Factice University Departments from 2013 to 2020")

#Save CSV
Digitalization_Departs.to_csv(path_DataViz + 'Digit_Depts_Years.csv')

#Display the Figure
plt.show()
"""


###################################################################################################
# (HEATMAP) Percentage of Digitalization for the Factice University Departments from 2013 to 2020 #
###################################################################################################
"""
Digitalization_Depts = Digitalization.groupby(['Department', 'Year'])['Digit_Percentage'].mean().reset_index()
Digitalization_Depts['Digit_Percentage'] = round(Digitalization_Depts['Digit_Percentage']).astype(int)
Digitalization_Depts = Digitalization_Depts.pivot("Department", "Year", "Digit_Percentage")

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.heatmap(Digitalization_Depts, annot= True, fmt="d", linewidths=.5, cmap = 'Spectral')
ax.set_xlabel("Année", size=16)
ax.set_ylabel("Départements de l'Université Factice", size=16)
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)

#Last Setting
#fig.suptitle("Percentage of Digitalization for the Factice University Departments from 2013 to 2020", ha = 'center', size=16, fontweight='bold')
fig.suptitle("Pourcentage de Digitalisation pour chaque Département de l'Université Factice de 2013 à 2020", ha = 'center', size=18)

fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Heatmap of the Digitalization for the Factice University Departments from 2013 to 2020")

#Save CSV
Digitalization_Depts.to_csv(path_DataViz + 'Pivot_Digit_Depts_Years.csv')

#Display the Figure
plt.show()


###################################################################################################
# (BOXPLOT) Percentage of Digitalization for the Factice University Departments from 2013 to 2020 #
###################################################################################################

Digitalization_Dep = Digitalization[Digitalization['Department'] == dep]

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
ax = sns.boxplot(x="Year", y="Digit_Percentage", hue = "Year", dodge = False, data=Digitalization_Dep, palette = 'Spectral')
ax.set_xlabel("Année", size=16)
ax.set_xticklabels(Digitalization_Dep['Year'].unique(), fontsize=16)
ax.set_ylabel("Digitalisation (en pourcentage [%])", size=16)
#ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
ax.get_legend().remove()

#Last Setting
#fig.suptitle("Distribution of the Digitalization Percentage for the Factice University Department of " + str(dep) + " from 2013 to 2020", ha = 'center', size=18)
fig.suptitle("Répartition du Pourcentage de Digitalisation pour le Département de " + str(dep) + " de l'Université Factice de 2013 à 2020", ha = 'center', size=18)
fig.tight_layout()

#Save Figure
fig.savefig(path_Figures + "Boxplot of the Digitalization for the Factice University Department of " + str(dep) + " from 2013 to 2020")

#Save CSV
Digitalization_Dep = Digitalization_Dep.sort_values(by = ['Year', 'Teacher_ID'], ascending = True).set_index('Teacher_ID')
Digitalization_Dep.to_csv(path_DataViz + 'Digit_' + str(dep) + '_Years.csv')

#Display the Figure
plt.show()

"""
###################################################################################################
# (BARPLOT) Percentage of Digitalization for the Factice University Departments from 2017 to 2020 #
###################################################################################################
"""
Digitalization_Dep = Digitalization.groupby(['Department', 'Year'])['Digit_Percentage'].mean().reset_index()
Digitalization_Dep['Digit_Percentage'] = round(Digitalization_Dep['Digit_Percentage']).astype(int)

Digitalization_Dep_2017 = Digitalization_Dep[Digitalization_Dep['Year'] == 2017]
Digitalization_Dep_2018 = Digitalization_Dep[Digitalization_Dep['Year'] == 2018]
Digitalization_Dep_2019 = Digitalization_Dep[Digitalization_Dep['Year'] == 2019]
Digitalization_Dep_2020 = Digitalization_Dep[Digitalization_Dep['Year'] == 2020]

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(4, 1, figsize=(16, 9), sharey=True)

#First Axis
sns.barplot(x="Department", y="Digit_Percentage", hue="Department", data=Digitalization_Dep_2017, dodge=False, palette="Spectral", ax = ax[0])
sns.despine()
ax[0].set_title("Percentage of Digitalization for the Departments of the Factice University in 2017", size=14)
ax[0].set_xlabel("Departments", size=13)
ax[0].set_ylabel("Digitalization (%)", size=13)
ax[0].get_legend().remove()
show_values_on_bars(ax[0])

#Second Axis
sns.barplot(x="Department", y="Digit_Percentage", hue="Department", data=Digitalization_Dep_2018, dodge=False, palette="Spectral", ax = ax[1])
sns.despine(offset=3)
ax[1].set_title("Percentage of Digitalization for the Departments of the Factice University in 2018", size=14)
ax[1].set_xlabel("Departments", size=13)
ax[1].set_ylabel("Digitalization (%)", size=13)
ax[1].get_legend().remove()
show_values_on_bars(ax[1])

#Third Axis 
sns.barplot(x="Department", y="Digit_Percentage", hue="Department", data=Digitalization_Dep_2019, dodge=False, palette="Spectral", ax = ax[2])
sns.despine(offset=3)
ax[2].set_title("Percentage of Digitalization for the Departments of the Factice University in 2019", size=14)
ax[2].set_xlabel("Departments", size=13)
ax[2].set_ylabel("Digitalization (%)", size=13)
ax[2].get_legend().remove()
show_values_on_bars(ax[2])

#Fourth Axis 
sns.barplot(x="Department", y="Digit_Percentage", hue="Department", data=Digitalization_Dep_2020, dodge=False, palette="Spectral", ax = ax[3])
sns.despine(offset=3)
ax[3].set_title("Percentage of Digitalization for the Departments of the Factice University in 2020", size=14)
ax[3].set_xlabel("Departments", size=13)
ax[3].set_ylabel("Digitalization (%)", size=13)
ax[3].get_legend().remove()
show_values_on_bars(ax[3])

#Last Setting
plt.ylim([0, 100]) #Set the y-axis lim
fig.suptitle("Percentage of Digitalization for the Factice University Departments from 2017 to 2020", ha = 'center', size=16, fontweight='bold')
fig.subplots_adjust(top=0.9,
                    bottom=0.075,
                    left=0.045,
                    right=0.99,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures + "Barplots of the Digitalization for the Factice University Departments from 2017 to 2019")

#Display
plt.show()
"""

#####################################################################################################
# (BARPLOT) Percentage of Digitalization for the Teachers of a Department of the Factice University #        
#####################################################################################################

Digitalization_Teach = Digitalization[Digitalization['Department'] == dep]
Digitalization_Teach = Digitalization_Teach[Digitalization_Teach['Year'] >= 2017]
Digitalization_Teach = Digitalization_Teach.groupby(['Teacher_Name', 'Year'])['Digit_Percentage'].mean().reset_index()
Digitalization_Teach['Digit_Percentage'] = round(Digitalization_Teach['Digit_Percentage']).astype(int)

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(1, 1, figsize=(16, 9), sharey=True)

#Axis
sns.barplot(x ="Teacher_Name", y = 'Digit_Percentage', data = Digitalization_Teach, hue = "Year")
ax.set_xlabel("Nom des Enseignants", size=13)
ax.set_ylabel("Digitalization (%)", size=13)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Année')
show_values_on_bars(ax)

#Last Setting
plt.ylim([0, 100]) #Set the y-axis lim
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
fig.suptitle("Pourcentage de Digitalisation de chaque Enseignant du Département de " + str(dep) + " de 2017 à 2020", ha = 'center', size=18)
fig.subplots_adjust(top=0.925,
                    bottom=0.075,
                    left=0.060,
                    right=0.9,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures + "Barplots of the Digitalization for the Factice University Department of " + str(dep) + " from 2017 to 2020")

#Display
plt.show()


#########################################################################################################
# BIS (BARPLOT) Percentage of Digitalization for the Teachers of a Department of the Factice University #        
#########################################################################################################

"""
Digitalization_Teach_2017 = Digitalization_Teach[Digitalization_Teach['Year'] == 2017]
Digitalization_Teach_2018 = Digitalization_Teach[Digitalization_Teach['Year'] == 2018]
Digitalization_Teach_2019 = Digitalization_Teach[Digitalization_Teach['Year'] == 2019]
Digitalization_Teach_2020 = Digitalization_Teach[Digitalization_Teach['Year'] == 2020]


#Set the size of the figures 
fig, ax = plt.subplots(4, 1, figsize=(16, 9), sharey=True)

#First Axis
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Teacher_Name", data=Digitalization_Teach_2017, dodge=False, palette="rocket", ax = ax[0])
sns.despine()
ax[0].set_title("Percentage of Digitalization for each Teacher of the " + str(dep) + " Department in 2017", size=14)
ax[0].set_xlabel("Teachers Name", size=13)
ax[0].set_ylabel("Digitalization (%)", size=13)
ax[0].get_legend().remove()
show_values_on_bars(ax[0])

#Second Axis
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Teacher_Name", data=Digitalization_Teach_2018, dodge=False, palette="rocket", ax = ax[1])
sns.despine(offset=3)
ax[1].set_title("Percentage of Digitalization for each Teacher of the " + str(dep) + " Department in 2018", size=14)
ax[1].set_xlabel("Teachers Name", size=13)
ax[1].set_ylabel("Digitalization (%)", size=13)
ax[1].get_legend().remove()
show_values_on_bars(ax[1])

#Third Axis 
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Teacher_Name", data=Digitalization_Teach_2019, dodge=False, palette="rocket", ax = ax[2])
sns.despine(offset=3)
ax[2].set_title("Percentage of Digitalization for each Teacher of the " + str(dep) + " Department in 2019", size=14)
ax[2].set_xlabel("Teachers Name", size=13)
ax[2].set_ylabel("Digitalization (%)", size=13)
ax[2].get_legend().remove()
show_values_on_bars(ax[2])

#Fourth Axis 
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Teacher_Name", data=Digitalization_Teach_2020, dodge=False, palette="rocket", ax = ax[3])
sns.despine(offset=3)
ax[3].set_title("Percentage of Digitalization for each Teacher of the " + str(dep) + " Department in 2020", size=14)
ax[3].set_xlabel("Teachers Name", size=13)
ax[3].set_ylabel("Digitalization (%)", size=13)
ax[3].get_legend().remove()
show_values_on_bars(ax[3])

#Last Setting
plt.ylim([0, 110]) #Set the y-axis lim
fig.suptitle("Percentage of Digitalization for each Teacher of the Factice University Department of " + str(dep) + " from 2017 to 2020", ha = 'center', size=16, fontweight='bold')
fig.subplots_adjust(top=0.9,
                    bottom=0.075,
                    left=0.045,
                    right=0.99,
                    hspace=1.0,
                    wspace=1.0)

#Save Figure
fig.savefig(path_Figures + "Barplots of the Digitalization for the Factice University Department of " + str(dep) + " from 2017 to 2019")

#Save CSV
Digitalization_Teach = Digitalization_Teach.sort_values(by = ['Year', 'Teacher_Name'], ascending = True).set_index('Teacher_Name')
Digitalization_Teach.to_csv(path_DataViz + 'Digit_' + str(dep) + '_Teachers_Name.csv')

#Display
plt.show()
"""