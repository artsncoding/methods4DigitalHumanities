import json
from CSVwriter import writeListToCSV, writeListToCSV2
from yearExtractor import extractYears

#Open json file and read it in
with open('fng-data-dc.json', encoding="utf8") as json_data:
    d = json.load(json_data)

#Variables to store the extracted datasets
data = {}
data['artWork'] =  []

data2 = {}
data2['artWork'] = []

#Read through the json file item by item 
#and extract and save desired content 
#to the variables 
for item in d['descriptionSet']:
    #Variables to save the desired content
    item_title='no title'
    item_publisher='no publisher'
    a_date = 'no date'
    collection = 'no collection'

    #if item has finnish title, save title 
    if('title' in item):
        for title in item['title']:
            if('fi' in title):
                item_title = title['fi']

    #if item has museum location
    #save museum location
    if('publisher' in item):
        for pub in item['publisher']:
            if('unit' in pub):
                item_publisher = pub['unit']

    #if item has acquisition date
    #save acquisition date
    if('date' in item):
        for date in item['date']:
            if('acquisition' in date):
                a_date = extractYears(date['acquisition'])
                #write item title, museum and acquisition date
                #to the first dataset
                data['artWork'].append({
                    'title': item_title,
                    'publisher': item_publisher,
                    'date': a_date
                })

    #if item has collection information
    #save collection information
    if('relation' in item):
        for relation in item['relation']:
            if('collection' in relation):
                collection = relation['collection']
                #save item title, museum, acquisition date and collection
                #to the second dataset
                data2['artWork'].append({
                    'title':item_title,
                    'publisher': item_publisher,
                    'date': a_date,
                    'collection': collection
                })

#write both datasets to CSV files 
writeListToCSV('dateData.csv', data['artWork'])
writeListToCSV2('collectionData.csv', data2['artWork'])
         




