#####################################################
# Ratio of Digitalization per University Department #        
#####################################################

#Import the required packages
import numpy as np
import pandas as pd
import random
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt

#Set a seed to keep the same values randomly defined after each execution.
seed( 1965  )


################
# Factice Data #
################

#Initial Information.
PRAG_Hour = 384 #Average Minimal (Hours of teaching) - PRAG.
PRCE_Hour = 192 #Average Minimal (Hours of teaching) - PRCE.
Prop_PRAG_on_PRCE = (8000)/(8000+6000) #PRAG/(PRAG+PRCE)
Prop_PRCE_on_PRAG = (6000)/(8000+6000) #PRCE/(PRAG+PRCE)

#Define a list of departements.
type_departement = ['Economy', 'History', 'Law', 'Nanagement', 'Art', 'Sociology', 'Mathematics', 'Engineering', 'Philosophy', 'Computer Science', 'Languages']
descpt_departement = []

#Take a random integer representing the number of departments.
num_dep = random.randint(10, len(type_departement))

#Append the type of each department.
department = []
num = 0
while num < num_dep:
    ran_num = random.randint(0, len(type_departement)-1)
    if type_departement[ran_num] not in department:
        department.append(type_departement[ran_num])
        num += 1 

#Display the number of departments and the type of each of them.
print('Number of Departments:', num_dep, '\nType:', department)   

#Create a list to represent the year interval (2013 to 2020).
list_years = [year for year in range(2013, 2021)]

#Create three lists 
hrs_department = [] #Total number of hours of teaching of each department.
hrs_ppl = [] #Total hours of work of each teacher.
ppl_department = []  #Total number of teachers per department.
teacher_ID = [] #The identification of each teacher

for dep in department:
    count = 0 
    ran_ppl = random.randint(5, 20)  #Random number that represents the number of teachers in the current department.
    for i in range(0, ran_ppl):
        rand_num = random.random()   #Define a random number to choose the teachers working time.
        if (0 <= rand_num <= Prop_PRAG_on_PRCE) :
            hrs_teach = random.uniform(384*0.8, 384*1.2)  #Set the current teacher as a PRAG (with 20% range from the basic working hours).
        elif (Prop_PRAG_on_PRCE < rand_num <= 1):
            hrs_teach = random.uniform(192*0.8, 192*1.2)  #Set the current teacher as a PRCE (with 20% range from the basic working hours).
        hrs_ppl.append(round(hrs_teach))  #Append the number of working hours of the current teacher.
        count += hrs_teach 

    hrs_department.append(round(count)) #Append the number of teaching hours of the current department. 
    ppl_department.append(ran_ppl) #Append the number of teacher of the current department.

#Duplicate the initial values of teaching hours for each year
hrs_ppl_y = []
for year in list_years:
    hrs_ppl_y = hrs_ppl_y + hrs_ppl


#Define a list with the name of each teacher per department
Rand_Name = pd.read_csv('Digitalization/Example/Data/Random_Common_Names.csv').reset_index() #Import the CSV
teacher_name = []

for num_ppl in ppl_department:
    for i in range(0, num_ppl):
        done = False
        while done == False:
            rand_name = random.randint(0, len(Rand_Name['Name'])-1)
            if Rand_Name['Name'][rand_name] not in teacher_name:
                teacher_name.append(Rand_Name['Name'][rand_name])
                done = True 

#Create three temporary lists
teacher_department = [] #The department of each teacher
teacher_number_department = [] #The number of teachers per department 
teaching_department = [] #The total number of hours teached by department
temp_year = [] #The year of the teacher
list_teacher_ID = [] #List that represents the identification of each teacher
list_teacher_name = [] #List that represents the name of each teacher

dep = 0
for year in list_years:
    teach_ID = 1
    dep = 0
    for num_ppl in ppl_department:
        for i in range(0, num_ppl):
            teacher_number_department.append(num_ppl)
            teacher_department.append(department[dep])
            teaching_department.append(hrs_department[dep])
            temp_year.append(year)
            list_teacher_ID.append(teach_ID)
            list_teacher_name.append(teacher_name[teach_ID-1])
            teach_ID += 1
        dep += 1

#Create three lists to represent the ratio and percentage of digitalization of each teacher over the year.
temp_ID = [] #Temporary list to implemente the loop.
list_digit_ratio = []  #List that represents the digitalization ratio of each teacher.
list_digit_percent = [] #List that represents the digitalization percentage of each teacher.
for teach in list_teacher_ID:
    if teach in temp_ID:  #In case the selected ID has been already set (for a previous year), we keep the same duration.
        rt = False #Set the variable to «False».
        ins = [teach_id for teach_id in range(len(temp_ID)) if temp_ID[teach_id] == teach] #Find the index of the identical ID as the current «course» selected ID.

        #Create a while loop to compute the ratio/percentage of digitalization.
        while (rt == False): 
            ran_unif = round(random.uniform(0,1),2) #Randomly select between 0 to 0.5 representing the increase of digitalization
            ratio = list_digit_ratio[ins[-1]] + list_digit_ratio[ins[-1]] * ran_unif #Compute the new ratio from the previous one.
            if ratio <= 1: #We can not have a ratio above 1.
                list_digit_ratio.append(round(ratio,2))  #Append a random number corresponding to the ratio of digitalization.
                list_digit_percent.append(int(ratio * 100)) #Append a random number corresponding to the percentage of digitalization.
                temp_ID.append(teach) #Append the course ID in the temporary list.
                rt = True #Since the conditions is respected and the ratio/percentages of digitalizaton added then we set the variable to «True».
    else:
        ran_unif = round(random.uniform(0,0.8),2) #Ratio of digitalization.
        list_digit_ratio.append(ran_unif)  #Append a random number corresponding to the ratio of digitalization
        list_digit_percent.append(int(ran_unif * 100)) #Append a random number corresponding to the percentage of digitalization
        temp_ID.append(teach) #Append the course ID in the temporary list.


#Make the dataframe
Digitalization_Dept = pd.DataFrame({'Teacher_ID': list_teacher_ID,
                                    'Teacher_Name': list_teacher_name,
                                    'Department': teacher_department,
                                    'Year': temp_year,
                                    'Teacing_Duration': hrs_ppl_y,
                                    'Teaching_Digit': [round(hrs * prct) for hrs, prct in zip(hrs_ppl_y, list_digit_ratio)],
                                    'Teaching_Present': [round(hrs - (hrs*prct)) for hrs, prct in zip(hrs_ppl_y, list_digit_ratio)],
                                    'Hours_Teached_Department': teaching_department,
                                    'Teacher_Department': teacher_number_department,
                                    'Digit_Ratio': list_digit_ratio,
                                    'Digit_Percentage': list_digit_percent,
                                                  
})

#Create a list of conditions to define the level of digitalization.
conditions_digit = [
    (Digitalization_Dept['Digit_Percentage'] > 80),
    (Digitalization_Dept['Digit_Percentage'] > 50) & (Digitalization_Dept['Digit_Percentage'] <= 80),
    (Digitalization_Dept['Digit_Percentage'] > 20) & (Digitalization_Dept['Digit_Percentage'] <= 50),
    (Digitalization_Dept['Digit_Percentage'] <= 20),
]

#Create a list of values to assign to each condition from the above list
type_digit = ['High Digitalization', 'Medium-High Digitalization', 'Medium-Low Digitalization', 'Low Digitalization']

#Implement the level of digitalization on the dataframe
Digitalization_Dept['Digitalization'] = np.select(conditions_digit, type_digit)

print(Digitalization_Dept.head(10))

# Sauvegarder le dataframe en CSV
Digitalization_Dept = Digitalization_Dept.sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Dept.to_csv('Digitalization/Example/Data/Digitalization_perDepartment.csv')


##################
# Visualisations #
##################

#Select three departments to build a figure
department = []
while len(department) != 3:
    ran_num = random.randint(0, (len(Digitalization_Dept['Department'].unique())-1))
    if Digitalization_Dept['Department'].unique()[ran_num] not in department:
            department.append(Digitalization_Dept['Department'].unique()[ran_num])
print(department)

Digitalization_Grp = Digitalization_Dept.groupby(['Year', 'Department'])['Digit_Percentage'].mean().reset_index()
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

fig.suptitle("Percentage of Digitalization of respectively the" + label_dep + "University Departments from 2017 to 2019", ha = 'center', size=16, fontweight='bold')

#Save Figure
fig.savefig("Digitalization/Example/Figures/Barplots of the Digitalization per Department from 2017 to 2019")

#Display
plt.show()


##########################################################################
# Ratio of Digitalization per Teacher of University Department (Factice) #        
##########################################################################


#Select three departments to build a figure
ran_dep = random.randint(0, (len(department)-1))
dep = department[ran_dep]
print(dep)

Digitalization_Teach = Digitalization_Dept[Digitalization_Dept['Department'] == dep].sort_values(by = ['Year', 'Teacher_ID'], ascending = True)
Digitalization_Teach_2017 = Digitalization_Teach[Digitalization_Teach['Year'] == 2017]
Digitalization_Teach_2018 = Digitalization_Teach[Digitalization_Teach['Year'] == 2018]
Digitalization_Teach_2019 = Digitalization_Teach[Digitalization_Teach['Year'] == 2019]

#Build the figure
sns.set() # Setting seaborn as default style even if use only matplotlib
sns.set_style("white")

#Set the size of the figures 
fig, ax = plt.subplots(3, 1, figsize=(16, 9), sharey=True)

sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Teacher_Name", data=Digitalization_Teach_2017, dodge=False, palette="icefire", ax = ax[0])
sns.despine()
ax[0].set_title("Percentage of Digitalization of each teacher from the department of " + str(dep) + " in 2017", size=14)
ax[0].set_xlabel("Teacher Name", size=14)
ax[0].set_ylabel("Percentage of Digitalization", size=12)
ax[0].get_legend().remove()
show_values_on_bars(ax[0])

#
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Year", data=Digitalization_Teach_2018, dodge=False, palette="icefire", ax = ax[1])
sns.despine(offset=3)
ax[1].set_title("Percentage of Digitalization of each teacher from the department of " + str(dep) + " in 2018", size=14)
ax[1].set_xlabel("Teacher Name", size=14)
ax[1].set_ylabel("Percentage of Digitalization", size=12)
ax[1].get_legend().remove()
show_values_on_bars(ax[1])

#
sns.barplot(x="Teacher_Name", y="Digit_Percentage", hue="Year", data=Digitalization_Teach_2019, dodge=False, palette="icefire", ax = ax[2])
sns.despine(offset=3)
ax[2].set_title("Percentage of Digitalization of each teacher from the department of " + str(dep) + " in 2019", size=14)
ax[2].set_xlabel("Teacher Name", size=14)
ax[2].set_ylabel("Percentage of Digitalization", size=12)
ax[2].get_legend().remove()
show_values_on_bars(ax[2])


#Last Setting
plt.ylim([0, 120]) #Set the y-axis lim
fig.suptitle("Percentage of Digitalization of each Teacher of the University Department of " + str(dep) + "from 2017 to 2019", ha = 'center', size=16, fontweight='bold')
fig.subplots_adjust(left=0.075,
                    bottom=0.075, 
                    right=0.950, 
                    top=0.875, 
                    wspace=0.4, 
                    hspace=1)

#Save Figure
fig.savefig("Digitalization/Example/Figures/Barplot of the Digitalization per Teacher of the" + str(dep) + "Department from 2017 to 2019")

#Display
plt.show()