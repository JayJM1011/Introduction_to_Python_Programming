def Sum(N1, N2):
    if N2 == 0:
        return N1

    elif N2> N1:
        return Sum(N2, N1)
    else:
        N1+= 1
        N2-= 1
        return Sum(N1, N2)
print(Sum(int(input("No1: ")), int(input("No2: "))))