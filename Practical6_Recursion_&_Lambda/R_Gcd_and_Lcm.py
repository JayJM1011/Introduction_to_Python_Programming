def GCD(N1, N2, Gcd):
    if (N1% Gcd == 0 and N2% Gcd == 0):
        return Gcd
    elif (Gcd> N1 or Gcd> N2):
        return 1
    else:
        Gcd+= 1
        return GCD(N1, N2, Gcd)
def LCM(N1, N2, Lcm):
    if(Lcm% N1 == 0 and Lcm% N2 == 0):
        return Lcm
    else:
        Lcm+= 1
        return LCM(N1, N2, Lcm)
N1, N2= int(input("Num1: ")), int(input("Num2: "))
print("GCD=",GCD(N1, N2, 2),"LCM=", LCM(N1, N2, max(N1, N2)))