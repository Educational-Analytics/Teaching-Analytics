###################
# Names (Factice) #        
###################

#Import the required packages
import json
import urllib
import requests
import pandas as pd


#Set the data names from the url
url_large = 'https://parseapi.back4app.com/classes/Complete_List_Names?count=1&limit=200000'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_large = json.loads(requests.get(url_large, headers=headers).content.decode('utf-8')) # Here you have the data that you need


url_common = 'https://parseapi.back4app.com/classes/NamesList?limit=6800'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_common = json.loads(requests.get(url_common, headers=headers).content.decode('utf-8')) # Here you have the data that you need


where = urllib.parse.quote_plus("""
{
    "Letter": "C"
}
""")
url_small = 'https://parseapi.back4app.com/classes/NamesList?limit=10&order=Name&where=%s' % where
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data_small = json.loads(requests.get(url_small, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(data_small)


#Create the Dataframe with 50K Names
Large_df = pd.DataFrame({
    'Name': [data_large['results'][i]['Name'] for i in range(0, len(data_large['results']))],
    'Gender': [data_large['results'][i]['Gender'] for i in range(0, len(data_large['results']))],
})
Large_df = Large_df.sort_values(by = 'Name', ascending = True)

#Create the Dataframe with common names
Common_df = pd.DataFrame({
    'Name': [data_common['results'][i]['Name'] for i in range(0, len(data_common['results']))],
    'Gender': [data_common['results'][i]['Genre'] for i in range(0, len(data_common['results']))],
})
Common_df = Common_df.sort_values(by = 'Name', ascending = True)

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
Large_df.to_csv('Digitalization/Example/Data/Random_200k_Names.csv')
Common_df.to_csv('Digitalization/Example/Data/Random_Common_Names.csv')
Small_df.to_csv('Digitalization/Example/Data/Random_Small_Names.csv')
