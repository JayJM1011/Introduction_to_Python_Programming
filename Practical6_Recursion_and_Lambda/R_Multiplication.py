def Mul(N1, N2):
    if N2 == 1:
        return N1
    return Mul(N1, N2- 1)+ N1
N1, N2= int(input("  ")), int(input("X "))
print("=", Mul(N1, N2))