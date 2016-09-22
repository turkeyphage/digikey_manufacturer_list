#! /usr/local/bin/python3

from openpyxl import load_workbook
import re

#file
wb = load_workbook(filename='Digi-Key_Line_Card.xlsx', read_only=True)

#sheet
ws = wb['Sheet0']


#valiable for cell
manufacturer=[]



#get cell in each row
for row in ws.rows:
    for cell in row:
        #print(cell.value)

        if cell.value != None: 
            items = cell.value.split('/')
            for item in items:
                #remove leading space and "("
                mod_item = item.strip()
                #manufacturer.append(mod_item)
   
                #print(mod_item)             

                if '(' in mod_item:
                   regex = re.compile(r'\((.*?)\)')
                   mo1 = regex.findall(mod_item)
                   #print(mo1)
                   #print(len(mo1))
                   manufacturer = manufacturer + mo1
                   del_item = '('+mo1[0]+')'
                   newitem = mod_item.replace(del_item,'')
                   newitem = newitem.strip()
                   manufacturer.append(newitem)
                   #print(newitem)
                else:
                   manufacturer.append(mod_item)

del manufacturer[0:4]
with open('Digi-Key_Line_Card.txt','w') as new_file:
    for each in manufacturer:
        new_file.write(each+'\n')



#print(manufacturer)

