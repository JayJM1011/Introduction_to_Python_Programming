def Words(Num):
    Str= ''
    for i in Num:
        if i == '0':
            Str+= 'zero '
        if i == '1':
            Str+= 'one '
        if i == '2':
            Str+= 'two '
        if i == '3':
            Str+= 'three '
        if i == '4':
            Str+= 'four '
        if i == '5':
            Str+= 'five '
        if i == '6':
            Str+= 'six '
        if i == '7':
            Str+= 'seven '
        if i == '8':
            Str+= 'eight '
        if i == '9':
            Str+= 'nine '
    return Str
def Nums(Nu):
    Num= Nu.split()
    Str= ''
    for i in Num:
        if i == 'zero':
            Str+= '0'
        if i == 'one':
            Str+= '1 '
        if i == 'two':
            Str+= '2 '
        if i == 'three':
            Str+= '3 '
        if i == 'four':
            Str+= '4 '
        if i == 'five':
            Str+= '5 '
        if i == 'six':
            Str+= '6 '
        if i == 'seven':
            Str+= '7 '
        if i == 'eight':
            Str+= '8 '
        if i == 'nine':
            Str+= '9 '
    return Str
print(Words(input('Number: ')))
print(Nums(input('Words: ')))