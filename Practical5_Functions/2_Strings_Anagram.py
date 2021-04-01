def Check(Str1, Str2):
    Str1, Str2= Str1.upper()+ ' ', Str2.upper()+ ' '
    for let in Str1:
        if let not in Str2:
            return False
    return True
print(Check(input("Enter String1: "), input("Enter String2: ")))