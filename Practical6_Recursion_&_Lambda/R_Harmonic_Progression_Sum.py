def HPS(a, d, n, Sum):
    if n == 1:
        return Sum+ a
    else:
        Sum+= 1/ ((1/ a)+ (n- 1)* (1/ d))
        n-= 1
        return HPS(a, d, n, Sum)
a, d, n= float(input("a= ")), float(input("d= ")), int(input("n= "))
print(HPS(a, d, n, 0))