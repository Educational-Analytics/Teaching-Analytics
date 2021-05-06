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


###############################################################################
# Percentage of Digitalization three University Departments from 2013 to 2020 #        
###############################################################################

#Select three departments to build a figure
department = []
while len(department) != 3:
    ran_num = random.randint(0, (len(Digitalization['Department'].unique())-1))
    if Digitalization['Department'].unique()[ran_num] not in department:
            department.append(Digitalization['Department'].unique()[ran_num])
print(department)

Digitalization_Grp = Digitalization.groupby(['Year', 'Department'])['Digit_Percentage'].mean().reset_index()
Digitalization_Grp['Digit_Percentage'] = round(Digitalization_Grp['Digit_Percentage']).astype(int)
Digitalization_Dept_D1 = Digitalization_Grp[Digitalization_Grp['Department'] == department[0]].sort_values(by = ['Year'], ascending = True)
Digitalization_Dept_D2 = Digitalization_Grp[Digitalization_Grp['Department'] == department[1]].sort_values(by = ['Year'], ascending = True)
Digitalization_Dept_D3 = Digitalization_Grp[Digitalization_Grp['Department'] == department[2]].sort_values(by = ['Year'], ascending = True)


#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(3, 1, figsize=(16, 9), sharey=True)

#

sns.barplot(x="Year", y="Digit_Percentage", hue="Year", data=Digitalization_Dept_D1, dodge=False, palette="Greens", ax = ax[0])
sns.despine()
ax[0].set_title("Percentage of Digitalization from the department of " + str(department[0]) + " from 2013 to 2020", size=14)
ax[0].set_xlabel("Year", size=14)
ax[0].set_ylabel("Percentage of Digitalization", size=12)
ax[0].get_legend().remove()
show_values_on_bars(ax[0])

#
sns.barplot(x="Year", y="Digit_Percentage", hue="Year", data=Digitalization_Dept_D2, dodge=False, palette="Blues", ax = ax[1])
sns.despine(offset=3)
ax[1].set_title("Percentage of Digitalization from the department of " + str(department[1]) + " from 2013 to 2020", size=14)
ax[1].set_xlabel("Year", size=14)
ax[1].set_ylabel("Percentage of Digitalization", size=12)
ax[1].get_legend().remove()
show_values_on_bars(ax[1])

#
sns.barplot(x="Year", y="Digit_Percentage", hue="Year", data=Digitalization_Dept_D3, dodge=False, palette="Reds", ax = ax[2])
sns.despine(offset=3)
ax[2].set_title("Percentage of Digitalization from the department of " + str(department[2]) + " from 2013 to 2020", size=14)
ax[2].set_xlabel("Year", size=14)
ax[2].set_ylabel("Percentage of Digitalization", size=12)
ax[2].get_legend().remove()
show_values_on_bars(ax[2])


#Last Setting
plt.ylim([0, 120]) #Set the y-axis lim
fig.subplots_adjust(left=0.075,
                    bottom=0.075, 
                    right=0.950, 
                    top=0.875, 
                    wspace=0.4, 
                    hspace=1)

#Create the label departments
label_dep = ' '
for dep in range (0, len(department)):
    if dep == len(department) -2:
        label_dep = label_dep + department[dep] + ' and '
    elif dep == len(department) -1:
        label_dep = label_dep + department[dep] + ' '
    else:
        label_dep = label_dep + department[dep] + ', '

fig.suptitle("Percentage of Digitalization of respectively the" + label_dep + "University Departments from 2013 to 2020", ha = 'center', size=16, fontweight='bold')

#Save Figure
fig.savefig("Digitalization/Example/Figures/Barplots of the Digitalization per Department from 2013 to 2020")

#Display
plt.show()
