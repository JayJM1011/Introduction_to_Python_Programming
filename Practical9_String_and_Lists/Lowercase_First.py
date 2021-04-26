Str= list(input('String: '))
for i in range(len(Str)- 1):
    for j in range(0, len(Str)- i- 1):
        if Str[j].isupper():
            Str[j], Str[j+ 1]= Str[j+ 1], Str[j]
print(''.join(Str))