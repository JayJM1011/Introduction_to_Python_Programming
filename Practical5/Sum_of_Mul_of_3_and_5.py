def ret(Lim):
    sum= 0
    for i in range(Lim+ 1):
        if i% 3 == 0:
            sum+= i
            continue
        if i% 5 == 0:
            sum+= i
    return sum
limit, sum= int(input("Enter Till: ")), 0
print(ret(limit))