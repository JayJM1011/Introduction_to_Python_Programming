#To show nested loops
for i in range(1, 11):
    Str= ""
    for j in range(1, 11):
        temp= str(i* j)
        Str= Str+ temp+ ', '
    print (Str)