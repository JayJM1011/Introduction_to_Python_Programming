#Task8

rad, height, pi= float(input('Radius ')), float(input('Height ')), 3.14159265359
area= pi* rad* (rad+ ((rad**2 + height**2)**0.5))
print('The Surface Area is', area)