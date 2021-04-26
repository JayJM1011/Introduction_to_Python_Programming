Str1, Str2= input('String: '), ''
for i in Str1:
    if i.lower() == 'a' or i.lower() == 'e':
        Str2+= i
    if i.lower() == 'i' or i.lower() == 'o':
      
        Str2+= i
    if i.lower() == 'u' or i.lower() == ' ':
        Str2+= i
print(Str2)