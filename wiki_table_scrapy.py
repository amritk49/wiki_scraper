from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

android_url = "https://en.wikipedia.org/wiki/Android_version_history"
android_data = urlopen(android_url)
#print(type(android_data))

android_html = android_data.read()
#print(android_html)

android_soup = BeautifulSoup(android_html,'html.parser')
#print(android_soup)

#to get all heading with H1 tag
android_soup.findAll('h1',{})

#to_get_all_table_with_class = "wiki_table"
tables = android_soup.findAll('table',{'class':'wikitable'})
android_table = tables[0]

#to get all column heading
headers = android_table.findAll('th')
column_titles = [ct.text[:-1] for ct in headers]

#to get all row headers
rows_data = android_table.findAll('tr')[1:]

#getting all data from the table
tables_rows = []
for row in rows_data:
    current_row = []
    row_data = row.findAll('td',{})
    
    for idx,data in enumerate(row_data):
        current_row.append(data.text[:-1])
    
    tables_rows.append(current_row)
#print(tables_rows)

#writing and reading CSV files
filename = 'android_version_history.csv'
with open(filename,'w',encoding='utf-8') as f:
    #write the header
    header_string = ','.join(column_titles)
    header_string += '\n'
    f.write(header_string)

    for row in tables_rows[:-1]:
        row_string = ""
        for w in row:
            w = w.replace(',','')
            row_string += w+','
        row_string = row_string[:-1]
        row_string += '\n'
        f.write(row_string)

df = pd.read_csv('android_version_history.csv')
df.head(n=10)
df.iloc[0][3]
