#Task7

days= 465
years, months= 0, 0
if days >= 365:
    years= int(days/ 365)
    days= days- (years* 365)
if days >= 30:
    months= int(days/ 30)
    days= days- (months* 30)
print('The given number of days is equal to {0} Years, {1} Months, and {2} days'.format(years, months, days))