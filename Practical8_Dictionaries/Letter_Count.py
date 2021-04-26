Str, Dict= input("String: "), {}
for i in Str:
    Dict.update({i: Str.count(i)})
print(Dict)