#Welcome to my data crunsher for the ZLB 
#The idea is to calculate for any day what amount of orders arrives at 8am

#First I need to get the data from the relevant day as well as the preceeding day
import re #need regular expressions to find the exact index of my required data 

path = '/home/david/Documents/ZLBData/nutzbares/benutzung_20200929.txt' 
f = open(path)
dayInQ = f.read()
Ind_0708 = '2245:2248' #location of the number corresponding to AGB orders from 07am to 08am
Ind_FRUEHER = '2916:2919'
#print(dayInQ[2916:2919])

path2 = '/home/david/Documents/ZLBData/nutzbares/benutzung_20200928.txt'
f2 = open(path2)
dayBef = f2.read()
Ind_2021 = '2869:2873'
Ind_SPAETER = '2958:2960'
#print(dayBef[2869:2873])

result = [dayBef[2963:2967].strip(' '), dayBef[2869:2873].strip(' '), dayInQ[2916:2919].strip(' '), dayInQ[2245:2248].strip(' ')]

cleanList = []
for element in result:
    cleanElement = element.strip()
    try:
        cleanList.append(int(cleanElement))
    except:
        continue

#print(cleanList)

Sum = cleanList[0] + cleanList[1] + cleanList[2] + cleanList[3]

print('Am Morgen des 29.09.2020 waren vor 10 Uhr ' + str(Sum) + ' Bestellungen in der AGB rauszusuchen.')

#use this code block to find any pattern in the data
'''
pattern = '20-21'
match = re.search(pattern, dayBef)

s = match.start()
e = match.end()


print ('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, dayBef[s:e]))
    
'''