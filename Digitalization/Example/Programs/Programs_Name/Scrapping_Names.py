###################
# Names (Factice) #        
###################

#Import the required packages
import json
import urllib
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from pathlib import Path
import timeit
import requests

##########################
# SCRAPPING French Names #
##########################

url_list = []  #Create an empty list that will contains the urls.
lst_name = [] #Create a list that will contain the  last names.

url = 'https://www.familyeducation.com/baby-names/browse-origin/surname/french'  #Initial url.
exist = True
count = 0
while exist == True: #Try to find all the existing similar url containing the names.
    if count == 0:
        url_check = url
    else:
        url_check = url + '?page=' + str(count)
    response = requests.get(url_check)
    if response.status_code == 200: #Check if the url exists.
        url_list.append(url_check) #Append the url.
        html_url = urlopen(url_check) 
        soup = BeautifulSoup(html_url, 'lxml')
        for a in soup.find_all("a", href=re.compile("https://www.familyeducation.com/baby-names/name-meaning/")): #Select the <a> from the current URL.
            if a.text != '':
                lst_name.append(a.text) #Append the text from the <a> on the specific list.
            else:
                continue
    else:
        exist = False #Whenever the url does not exist we stop the loop.

    count += 1 #Increase the count to continue the loop.
print('Amount of Link:', len(url_list)) #Display the amount of URL we saved.


###############
# Define Data #
###############  

French_Names = pd.DataFrame({'Last_Name' : lst_name})
French_Names = French_Names.drop_duplicates()
print('Number of Last French Names:', len(French_Names))

print(French_Names.head(10))

#############
# Save Data #
#############

#Save the dataframe into a CSV file
French_Names.to_csv('Digitalization/Example/Data/Names/French_Names_Lgh' + str(len(French_Names)) + '.csv')