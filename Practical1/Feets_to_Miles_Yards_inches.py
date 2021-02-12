#Task 5

feet= 5285.5
miles, yards, inches= 0, 0, 0
if feet >= 5280:
    miles= int(feet/ 5280.0)
    feet= feet% 5280
if feet >= 3:
    yards= int(feet/ 3.0)
    feet= feet% 3
if feet < 3:
    inches= int(feet* 12)
print('The given feets is equal to {0} Miles, {1} Yards, and {2} inches'.format(miles, yards, inches))