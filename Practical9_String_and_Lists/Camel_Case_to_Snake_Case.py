Str1= input('String: ')
Str2= [Str1[0].lower()]
for i in Str1[1:]:
    if i.isupper():
        Str2.append('_')
    Str2.append(i.lower())
print(''.join(Str2))