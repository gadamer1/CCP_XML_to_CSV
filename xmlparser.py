from xml.etree import ElementTree
import os
import csv
from bs4 import BeautifulSoup

data = open('./data/data.csv','w',newline='',encoding='utf-8')
columns = ['판례정보일련번호','사건명','사건번호','선고일자','선고','법원명',
'법원종류코드','사건종류명','사건종류코드','판결유형','판시사항','판결요지','참조조문','참조판례','판례내용']
csvWriter =csv.writer(data)
csvWriter.writerow(columns)


for i in range(0,80000):
    tree = ElementTree.parse(f'./test/{i}.txt')
    csvData = []
    root = tree.getroot()
    for column in columns:
        findData = root.find(column).text
        if findData != None:
            soup = BeautifulSoup(findData)
            text_parts= soup.findAll(text=True)
            csvData.append(''.join(text_parts))
    
    csvWriter.writerow(csvData)
