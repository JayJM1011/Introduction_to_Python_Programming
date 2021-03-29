#Task2

import cmath
a, b, c = 1, 6, 9
d= (b**2)- (4* a* c)
r1= (-b + cmath.sqrt(d))/ 2* a
r2= (-b - cmath.sqrt(d))/ 2* a
print('Root 1 is {0} and Root 2 is {1}'.format(r1, r2))