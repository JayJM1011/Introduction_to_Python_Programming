Number1, Number2 = int(input('Number 1: ')), int(input('Number 2: '))
MandL= max(Number1, Number2)
while (True):
    if MandL % Number1 == 0 and MandL % Number2 == 0:
        break
    MandL+= 1
print(MandL)