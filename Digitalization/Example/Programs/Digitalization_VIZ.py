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
            _y = p.get_y() + p.get_height() + 5
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

Digitalization = pd.read_csv('Digitalization\Example\Data\Digitalization.csv').reset_index()

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
fig.savefig("Digitalization/Example/Figures/Boxplot of the Digitalization for the Factice University Departments from 2013 to 2020")

#Display the Figure
plt.show()
"""

###################################################################################################
# (HEATMAP) Percentage of Digitalization for the Factice University Departments from 2013 to 2020 #
###################################################################################################

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
ax.set_xlabel("Years", size=13)
ax.set_ylabel("Departments", size=13)

#Last Setting
fig.suptitle("Percentage of Digitalization for the Factice University Departments from 2013 to 2020", ha = 'center', size=16, fontweight='bold')
fig.tight_layout()

#Save Figure
fig.savefig("Digitalization/Example/Figures/Heatmap of the Digitalization for the Factice University Departments from 2013 to 2020")

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
ax.set_xlabel("Years", size=13)
ax.set_ylabel("Digitalization (in percent [%])", size=13)
ax.legend(loc='center', bbox_to_anchor=(1.05, 0.5), shadow=True, title = 'Years')

#Last Setting
fig.suptitle("Distribution of the Digitalization Percentage for the Factice University Department of " + str(dep) + " from 2013 to 2020", ha = 'center', size=16, fontweight='bold')
fig.tight_layout()
fig.subplots_adjust(right=0.91)

#Save Figure
fig.savefig("Digitalization/Example/Figures/Boxplot of the Digitalization for the Factice University Department of " + str(dep) + " from 2013 to 2020")

#Display the Figure
plt.show()


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
fig.savefig("Digitalization/Example/Figures/Barplots of the Digitalization for the Factice University Departments from 2017 to 2019")

#Display
plt.show()
"""

#####################################################################################################
# (BARPLOT) Percentage of Digitalization for the Teachers of a Department of the Factice University #        
#####################################################################################################

Digitalization_Teach = Digitalization[Digitalization['Department'] == dep]
Digitalization_Teach = Digitalization_Teach.groupby(['Teacher_Name', 'Year'])['Digit_Percentage'].mean().reset_index()
Digitalization_Teach['Digit_Percentage'] = round(Digitalization_Teach['Digit_Percentage']).astype(int)

Digitalization_Teach_2017 = Digitalization_Teach[Digitalization_Teach['Year'] == 2017]
Digitalization_Teach_2018 = Digitalization_Teach[Digitalization_Teach['Year'] == 2018]
Digitalization_Teach_2019 = Digitalization_Teach[Digitalization_Teach['Year'] == 2019]
Digitalization_Teach_2020 = Digitalization_Teach[Digitalization_Teach['Year'] == 2020]

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

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
fig.savefig("Digitalization/Example/Figures/Barplots of the Digitalization for the Factice University Department of " + str(dep) + " from 2017 to 2019")

#Display
plt.show()
