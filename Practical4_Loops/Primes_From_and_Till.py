def isprime(No):
    for i in range(2, No):
        if No% i == 0:
            return False
    return True
NumFrom, NumTill= int(input("Enter Number from: ")), int(input("Enter Number till: "))
Primes= []
for i in range(NumFrom, NumTill+ 1):
    if(isprime(i)):
        Primes.append(i)
print(Primes)