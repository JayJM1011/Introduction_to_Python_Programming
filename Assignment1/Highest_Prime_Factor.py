def isPrime(Num):
    if Num< 1:
        return False
    for i in range(2, Num):
        if int(Num% i == 0):
            return False
    return True
def HPF(Num):
    Hpf= 0
    for i in range(1, Num+ 1):
        if int(Num% i) == 0 and isPrime(i):
            Hpf= i
    return Hpf
Hpf= HPF(int(input("Enter Number: ")))
print(Hpf, "is the HPF")