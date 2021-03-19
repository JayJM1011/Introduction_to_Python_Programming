Str, left, SubStr= input("Enter String: "), 0, []
for i in range(len(Str)):
    if Str[i] == ' ':
        SubStr.append(Str[left: i])
        left= i+ 1
    if (i == len(Str)- 1) and Str[i] != ' ':
        SubStr.append(Str[left: len(Str)])
print(SubStr)