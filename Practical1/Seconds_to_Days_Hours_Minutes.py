#Task7

seconds= 90400
days, hours, minutes= 0, 0, 0
if seconds >= 86400:
    days= int(seconds/ 86400.0)
    seconds= seconds- (days* 86400)
if seconds >= 3600:
    hours= int(seconds/ 3600)
    seconds= seconds- (hours* 3600)
if seconds < 3600:
    minutes= seconds/ 60
print('The given seconds is equal to {0} Days, {1} Hours, and {2} Minutes'.format(days, hours, minutes))