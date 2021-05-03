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
random.seed( 1052 ) #The seed does not need to be randomize


######################
# Class and Function #
######################

#A class of functions to implement the «Interval» from a value with range
class Interval(object):
    def __init__(self, middle, deviation):
        self.lower = middle - abs(deviation)
        self.upper = middle + abs(deviation)

    def __contains__(self, item):
        return self.lower <= item <= self.upper

def interval(middle, deviation):
    return Interval(middle, deviation)


def Digit_Ratio(CourseID, lst_CoursesID, Lst_Ratio):
    if CourseID in lst_CoursesID:  #In case the selected ID has been already implemented (for a previous year), we keep the same duration.
        inside = True #Set the variable to «False».
        ins = [courses for courses in range(0, len(lst_CoursesID)) if lst_CoursesID[courses] == CourseID] #Find the index of the identical ID as the current «course» selected ID.    
        #Create a while loop to compute the ratio/percentage of digitalization.
        while (inside == True): 
            if Lst_Ratio[ins[-1]] == 0:
                ratio = round(random.uniform(0.05,0.5),2)
            else:
                ratio = Lst_Ratio[ins[-1]] * round(random.uniform(1,1.5),2) #Compute the new ratio from the previous one.
            
            if ratio <= 1: #We can not have a ratio above 1.
                inside = False #Since the conditions is respe
    else:
        ratio = round(random.uniform(0,0.5),2) #Ratio of digitalization.
    return(ratio)

################
# Factice Data #
################

###################################################
# Build the factice Departments (number and type) #
###################################################

#Define a list of departements.
depts_type = ['Economy', 'History', 'Law', 'Management', 'Art', 'Sociology', 'Mathematics', 'Engineering', 'Philosophy', 'Computer Science', 'Languages']
depts_descrp = []

#Take a random integer representing the number of departments (at least 10 departments).
num_depts = random.randint(10, len(depts_type))

#Append the type of each department.
temp_Depts = []
num = 0
while num < num_depts: #Loop to implement the type of each department.
    ran_num = random.randint(0, len(depts_type)-1) #Randomly select a type of department.
    if depts_type[ran_num] not in temp_Depts: #Verify that the selected department is not already implemented in the list.
        temp_Depts.append(depts_type[ran_num]) #Append the select department into the list.
        num += 1  #Incremente the number of department in the list. 

#Display the number of departments and the type of each of them.
print('\nNumber of Departments:', num_depts)   
print('List of Departments:', temp_Depts, '\n')


#####################################
# Build the factice Year (interval) #
#####################################

#Create a list to represent the year interval (from 2013 to 2020).
temp_Years = [year for year in range(2013, 2021)]

#Display the number of departments and the type of each of them.
print('Number of Years:', len(temp_Years))   
print('Year Interval:', temp_Years, '\n')


#########################################################################
# Build the factice Teaching-research Personnel (number per department) #
#########################################################################

#Define the number of teacher per department
temp_NumbTRP = []
num_teachers = 0
for depts in temp_Depts:
    ran_ppl = random.randint(5, 15)  #Random number that represents the number of teachers in the current department.
    num_teachers += ran_ppl
    temp_NumbTRP.append(ran_ppl)

#Display the number of departments and the type of each of them.
print('Total Number of Teachers:', num_teachers)   
print('Number of Teachers per Department', temp_NumbTRP, '\n')

######################################################################################################################
# Build the factice Teaching-research Personnel (name, identification) and Taught Courses (duration, identification) #
######################################################################################################################

#Import a CSV file containing the most common names from the US (sample of 6,000).
Random_ComName = pd.read_csv('Digitalization/Example/Data/Names/Random_Common_Names.csv').reset_index() #Import the CSV containing some common names

#Initial Teaching-research Personnel Information.
PRAG_Hour = 384 #Average Minimal (Hours of teaching) - PRAG.
PRCE_Hour = 192 #Average Minimal (Hours of teaching) - PRCE.
Prop_PRAG_on_PRCE = (8000)/(8000+6000) #PRAG/(PRAG+PRCE)

#Set plenty of empty lists
lst_Teacher_ID = []         #List that represents the identification of all the teachers.
lst_Teacher_Name = []       #List that represents the name of all the teachers.
lst_Depts = []              #List that represents the departement of the teachers and courses.
lst_NumbTeachers = []       #List that represents the number of teachers per department.

lst_Course_ID = []          #List that represents the identification of all courses.
lst_Courses_Duration = []   #List that represents the duration (in hours) of all courses.
lst_Years = []              #List that represents the year of all courses.
lst_Courses_Digit = []      #List that represents the duration (in hours) from online ressources of all courses.
lst_Courses_Present = []    #List that represents the duration (in hours) from lectures of all courses.

lst_Digit_Ratio = []        #List that represents the digitalization ratio of all courses.
lst_Digit_Percent = []      #List that represents the digitalization percentage of all courses.

dep = 0                     #Variable used to implement «lst_Depts» and «lst_NumbTeachers». 
teacher_ID = 0              #Variable used to implement «lst_Teacher_ID».
course_ID = 1               #Variable used to implement «lst_Course_ID».

#Loop to implemente the above lists.
for teachers in temp_NumbTRP: #Loop that take the number of teachers per departments.
    dep += 1  #Increase the dep corresponding the index of the lists to implement.
    for i in range(0, teachers): #Loop that take all the teachers for the current department.
        teacher_ID += 1 #Increase the teacher_ID
        rand_name = random.randint(0, len(Random_ComName['Name'])-1) #Select randomly a name from the database of most common names.
        rand_num = random.random() #Define a random number to find the type of teacher (PRAG/PRCE).
        if (0 <= rand_num <= Prop_PRAG_on_PRCE):
            temp = 0 #Set the temporary variable to compute the total hours worked by a teacher
            while temp not in interval(middle=PRAG_Hour, deviation=PRAG_Hour*0.05):
                ran_courses = random.random()  #Define a random number to choose the time interval of a course.
                if (0 <= ran_courses < 0.4) : 
                    course_Duration = random.randint(5, 15)   #Define a random number to have a course between 5H and 15H.
                elif (0.4 <= ran_courses < 0.9) :
                    course_Duration = random.randint(15, 40)   #Define a random number to have a course between 15H and 40H.
                elif (0.9 <= ran_courses < 1):
                    course_Duration = random.randint(40, 60)   #Define a random number to have a course between 40H and 60H.
                elif (ran_courses == 1):
                    course_Duration = random.randint(60, 90)   #Define a random number to have a course between 60H and 90H.

                if temp + course_Duration <= PRAG_Hour*1.05: #Verify that the possible number of courses teached is lower than the amount of hours to teach.
                    for year in temp_Years: #Loop to implement all the years.
                        ratio = Digit_Ratio(course_ID, lst_Course_ID, lst_Digit_Ratio) #Find the ratio of digitalization

                        #Append the lists
                        lst_Years.append(year) 
                        lst_Course_ID.append(course_ID)
                        lst_Courses_Duration.append(course_Duration)
                        lst_Teacher_ID.append(teacher_ID)
                        lst_Teacher_Name.append(Random_ComName['Name'][rand_name])
                        lst_Depts.append(temp_Depts[dep-1])
                        lst_NumbTeachers.append(temp_NumbTRP[dep-1])
                        lst_Digit_Ratio.append(round(ratio,2))  
                        lst_Digit_Percent.append(int(ratio * 100))   
                        lst_Courses_Digit.append(round(course_Duration * ratio))
                        lst_Courses_Present.append(round(course_Duration - (course_Duration * ratio)))


                    course_ID += 1 #Increase the course_ID
                    temp += course_Duration #Add the course_duration to the temporary variable

                
        if (Prop_PRAG_on_PRCE <= rand_num <= 1) :
            temp = 0 #Set the temporary variable to compute the total hours worked by a teacher
            while temp not in interval(middle=PRCE_Hour, deviation=PRCE_Hour*0.05):
                ran_courses = random.random()  #Define a random number to choose the time interval of a course.
                if (0 <= ran_courses < 0.4) : 
                    course_Duration = random.randint(5, 15)   #Define a random number to have a course between 5H and 15H.
                elif (0.4 <= ran_courses < 0.9) :
                    course_Duration = random.randint(15, 40)   #Define a random number to have a course between 15H and 40H.
                elif (0.9 <= ran_courses < 1):
                    course_Duration = random.randint(40, 60)   #Define a random number to have a course between 40H and 60H.
                elif (ran_courses == 1):
                    course_Duration = random.randint(60, 90)   #Define a random number to have a course between 60H and 90H.

                if temp + course_Duration <= PRCE_Hour*1.05: #Verify that the possible number of courses teached is lower than the amount of hours to teach.
                    for year in temp_Years: #Loop to implement all the years.
                        ratio = Digit_Ratio(course_ID, lst_Course_ID, lst_Digit_Ratio) #Find the ratio of digitalization

                        #Append the lists
                        lst_Years.append(year) 
                        lst_Course_ID.append(course_ID)
                        lst_Courses_Duration.append(course_Duration)
                        lst_Teacher_ID.append(teacher_ID)
                        lst_Teacher_Name.append(Random_ComName['Name'][rand_name])
                        lst_Depts.append(temp_Depts[dep-1])
                        lst_NumbTeachers.append(temp_NumbTRP[dep-1])
                        lst_Digit_Ratio.append(round(ratio,2))  
                        lst_Digit_Percent.append(int(ratio * 100))   
                        lst_Courses_Digit.append(round(course_Duration * ratio))
                        lst_Courses_Present.append(round(course_Duration - (course_Duration * ratio)))


                    course_ID += 1 #Increase the course_ID
                    temp += course_Duration #Add the course_duration to the temporary variable


###############################################
# Build the Dataframe from the previous lists #
###############################################

Digitalization = pd.DataFrame({'Teacher_ID': lst_Teacher_ID,
                               'Teacher_Name': lst_Teacher_Name,
                               'Department': lst_Depts,
                               'Year': lst_Years,
                               'Course_ID': lst_Course_ID,
                               'Course_Duration': lst_Courses_Duration,      
                               'Course_Digit': lst_Courses_Digit,
                               'Course_Present': lst_Courses_Present,
                               'Digit_Ratio': lst_Digit_Ratio,
                               'Digit_Percentage': lst_Digit_Percent,                 
}).sort_values(by = ['Year', 'Teacher_ID', 'Course_ID'], ascending = True)

#Create a list of conditions to define the level of digitalization.
conditions_digit = [
    (Digitalization['Digit_Percentage'] > 80),
    (Digitalization['Digit_Percentage'] > 50) & (Digitalization['Digit_Percentage'] <= 80),
    (Digitalization['Digit_Percentage'] > 20) & (Digitalization['Digit_Percentage'] <= 50),
    (Digitalization['Digit_Percentage'] <= 20),
]

#Create a list of values to assign to each condition from the above list
type_digit = ['High Digitalization', 'Medium-High Digitalization', 'Medium-Low Digitalization', 'Low Digitalization']

#Implement the level of digitalization on the dataframe
Digitalization['Digitalization'] = np.select(conditions_digit, type_digit)

print(Digitalization.head(10))

# Sauvegarder le dataframe en CSV
Digitalization = Digitalization.sort_values(by = ['Year', 'Teacher_ID', 'Course_ID'], ascending = True)
Digitalization.to_csv('Digitalization/Example/Data/Digitalization.csv')

#########################
# Data Preparation DONE #
#########################