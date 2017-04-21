'''
Created on 16-Apr-2017

@author: manoj
'''
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import csv

wiki = "https://en.wikipedia.org/wiki/Indian_states_and_territories_ranked_by_incidents_of_human_trafficking"

page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,'lxml')

data = soup.prettify()
#print(data)

title = soup.title.string
print(title)

all_links = soup.find_all("a")
print(all_links)


#count number of links
count = 0
linklist = []
for links in all_links:
    count = count + 1
print(count)
    
    
#get href links
#for links in all_links:
    #print links.get("href")
    


#all_tables = soup.find_all('table')
#print(all_tables)


#find the right table
right_table = soup.find('table', class_='wikitable sortable')
print(right_table)
    
    
list_of_rows = []
for row in right_table.findAll('tr')[1:]: #Skipping the first row
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        print text
        list_of_cells.append(text)
    #print(list_of_cells)
    list_of_rows.append(list_of_cells)
print(list_of_rows)

outfile = open("./HumanTrafficking.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Number","State","Count"])
writer.writerows(list_of_rows)
    
    
    
    
    
    
    
    
    
    
    
    
    