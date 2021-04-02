def Bin(Num):
    if Num == 0:
        return 0
    N= Bin(Num // 2)
    return Num% 2+ 10* N
Num= int(input("Enter Number: "))
print(Bin(Num))