import re

#Regex to find yeards
yearRe = re.compile('[0-9][0-9][0-9][0-9]')
def extractYears(date):
    #search string for a regex match
    years = yearRe.search(date)

    #if match is found, save it
    #if not, save 0
    if years:
        year = years.group(0)
    else:
        year = 0
    return year
