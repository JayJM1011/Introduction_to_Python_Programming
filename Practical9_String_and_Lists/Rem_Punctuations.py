Str= list(input('String: '))
for i in Str:
    if i in ['!', '\'', '\"', ';', ':', ',', '-', '_']:
        Str.remove(i)
print(''.join(Str))