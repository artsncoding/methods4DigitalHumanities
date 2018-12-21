import csv

#Take a list and write it to a CSV file
def writeListToCSV(filename, dataList):
    #open empty CSV file
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        #for each item in the list, write the content to the file
        for item in dataList:
            writer.writerow([item['title'],item['publisher'],item['date']])

def writeListToCSV2(filename, dataList):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in dataList:
            writer.writerow([item['title'],item['publisher'],item['date'],item['collection']])