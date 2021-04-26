PhNo= {'Bee': '9451315246','Ay': '8651534824',  'Di': '7954224356'}
#Print Dictionary
for i in PhNo:
    print(i,':', PhNo[i])
#Add Contact
PhNo.update({'Sea': '8214685897'})
#Remove Contact
del PhNo['Di']
#Update Value
PhNo['Sea']= '8241685897'
#Search
Search= input('Search: ')
if Search in PhNo:
    print(True)
else:
    print(False)
#Sort by Key
for i in sorted(PhNo):
    print(i, ':', PhNo[i])