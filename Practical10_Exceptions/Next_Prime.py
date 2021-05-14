def IsPrime(N):
    while N:
        c = 0
        for i in range(1, N):
            if N% i == 0:
                c+= 1
        N+= 1
        if c==1:
            return N
print(IsPrime(int(input('Number= '))))