'''
install request, BeautifulSoup or bs4 and pandas library
'''
# imports and variables
import requests
import pandas as pd
from bs4 import BeautifulSoup
csvData = {}
serial_no = 0

# url input for scrapping
url = input('Please enter wikipedia URL: ')
print('requesting to website data....')

# url = 'https://en.wikipedia.org/wiki/Main_Page'
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
anchor = soup.find_all('a')

print('looking for href data....')

# loop for getting all of the href links
for link in anchor:
    data = str(link.get('href'))
    serial_no+=1

    if str(link.text) == '':
        text = link.get('title')
    else:
        text = link.text

    if data.startswith('/'):
        hrefLink = 'https://en.wikipedia.org' + data
    elif data.startswith('//'):
        hrefLink = 'https:' + data
    elif data.startswith('#'):
        hrefLink = url+data
    else:
        hrefLink = data
    
    # storing data into csvData dictionary
    csvData[serial_no] = [text,hrefLink]

# writing data to csv file using pandas library
data_df = pd.DataFrame.from_dict(csvData, orient='index', columns=['textContent', 'link'])
name_of_files = input("enter then file name: ")
data_df.to_csv(name_of_files+'.csv')
print('scrapping done')
