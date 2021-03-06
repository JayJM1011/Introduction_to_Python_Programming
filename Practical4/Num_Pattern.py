# 1
# 2 3
# 4 5 6
# 7 8 9 10

i, j, k= 0, 0, 1
while i< 4:
    Str, j= "", 0
    while j<=i:
        Str+= ' '+ str(k)
        j, k= j+ 1, k+ 1
    print(Str)
    i+= 1