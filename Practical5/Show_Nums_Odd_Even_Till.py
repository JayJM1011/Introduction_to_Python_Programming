def ShowNumbers(Lim):
    for i in range(Lim+ 1):
        Str= ""
        if i% 2 == 0:
            Str+= str(i)+ " Even"
        if i% 2 == 1:
            Str+= str(i)+ " Odd"
        print(Str)
ShowNumbers(int(input("Enter Limit: ")))