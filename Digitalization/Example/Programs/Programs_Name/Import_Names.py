###################
# Names (Factice) #        
###################

#Import the required packages
import json
import urllib
import pandas as pd
from urllib.request import urlopen
import requests

#####################################
# Importing from the Web Last Names #
#####################################

###################################
# Large Data of Names (= 200,000) #
###################################

#Import the large data.
url_large = 'https://parseapi.back4app.com/classes/Complete_List_Names?count=1&limit=200000'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_large = json.loads(requests.get(url_large, headers=headers).content.decode('utf-8')) # Here you have the data that you need

#Create the Dataframe for the large data.
Large_df = pd.DataFrame({
    'Name': [data_large['results'][i]['Name'] for i in range(0, len(data_large['results']))],
    'Gender': [data_large['results'][i]['Gender'] for i in range(0, len(data_large['results']))],
})
Large_df = Large_df.sort_values(by = 'Name', ascending = True)


##################################
# Data of Common Names (= 6,800) #
##################################

#Import the common data.
url_common = 'https://parseapi.back4app.com/classes/NamesList?limit=6800'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_common = json.loads(requests.get(url_common, headers=headers).content.decode('utf-8')) # Here you have the data that you need

#Create the Dataframe with common names.
Common_df = pd.DataFrame({
    'Name': [data_common['results'][i]['Name'] for i in range(0, len(data_common['results']))],
    'Gender': [data_common['results'][i]['Genre'] for i in range(0, len(data_common['results']))],
})
Common_df = Common_df.sort_values(by = 'Name', ascending = True)


###############################
# Small Data of Names (= 200) #
###############################

#Import the small data.
url_small = 'https://parseapi.back4app.com/classes/NamesList?limit=200'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_small = json.loads(requests.get(url_small, headers=headers).content.decode('utf-8')) # Here you have the data that you need

#Create the Dataframe with common names
Small_df = pd.DataFrame({
    'Name': [data_small['results'][i]['Name'] for i in range(0, len(data_small['results']))],
    'Gender': [data_small['results'][i]['Genre'] for i in range(0, len(data_small['results']))],
})
Small_df = Common_df.sort_values(by = 'Name', ascending = True)


#############
# Save Data #
#############

#Save the dataframe into a CSV file
Large_df.to_csv('Digitalization/Example/Data/Names/Random_200k_Names.csv')
Common_df.to_csv('Digitalization/Example/Data/Names/Random_Common_Names.csv')
Small_df.to_csv('Digitalization/Example/Data/Names/Random_Small_Names.csv')