'''
Created on 17-Apr-2017

@author: manoj
'''
import urllib2

from bs4 import BeautifulSoup

import pandas as pd
import csv

wiki = "https://en.wikipedia.org/wiki/Uttar_Pradesh_Legislative_Assembly_election,_2017"

page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,'lxml')

right_table = soup.find('table',class_='wikitable sortable collapsible')
#print(right_table)

list_of_rows = []
for row in right_table.findAll('tr')[1:]: #skipping the first row
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        print text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
print(list_of_rows)

outfile = open("./UPResults.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Id","Constituency","District","WininngCandidates","Party","RunnderCandidate","Party","Margin"])
writer.writerows(list_of_rows)
                 
                 
                 
                 
                 