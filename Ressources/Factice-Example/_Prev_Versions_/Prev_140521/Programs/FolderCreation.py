###################################################
# Creation of the Folders of the Factice Examples #        
###################################################

#Import the OS packages
import os

###################################
#Define the Path and Folders Name #
###################################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
dir_Folder = 'Factice-Example'  #Determine the name of the folder for the factice example. 
main_Folders = ['Data', 'Figures', 'Programs'] #Determine the name of the sub folders for the factice example.
main_SubFolders = ['Data-Viz']
glob_path = '/'.join(dir_path.split('/')[0:(dir_path.split('/').index(dir_Folder))])  #Find the General Path

for f_names in main_Folders: #Loop that take each value among the sub folders list.
    try: #Try/Except Methods
        os.mkdir(glob_path + '/' + dir_Folder + '/' + f_names) #Create the subfolder with the associated name.
        print(f_names, 'Folder Created')
    except OSError as error: #In case the subfolder is already created.
        print(f_names, 'Folder Already Created')

for sf_names in main_SubFolders:
    try:
        os.mkdir(glob_path + '/' + dir_Folder + '/' + main_Folders[0] + '/' + sf_names) #Create the subfolder with the associated name.
        print(sf_names, 'Folder Created')
    except OSError as error: #In case the subfolder is already created.
        print(sf_names, 'Folder Already Created')

################################
#Folder and SubFolders Created #
################################
