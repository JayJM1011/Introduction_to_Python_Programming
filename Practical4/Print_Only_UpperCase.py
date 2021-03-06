Str1, Str2, StrFin= input("Enter String1: "), input("Enter String2: "), ""
for i in Str1:
    if i.isupper() == True:
        StrFin+= i
for i in Str2:
    if i.isupper() == True:
        StrFin+= i
print(StrFin)