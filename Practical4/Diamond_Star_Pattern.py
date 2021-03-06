i, j, k= 1, 1, 2
for i in range(6):
    Str= ""
    for j in range(6):
        if k >= 0:
            if j >= k and j < 5- k:
                Str+= "*"
            else:
                Str+= " "
        else:
            if j>= -(k) and j< 5 +k:
                Str+= "*"
            else:
                Str+= " "
    k-= 1
    print(Str)