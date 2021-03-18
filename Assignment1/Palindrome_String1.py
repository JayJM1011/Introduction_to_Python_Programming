def IsPali(Str):
    right, mid= len(Str)- 1, (len(Str))//2
    for i in range(mid):
        if Str[i] is not Str[right]:
            return False
        right-= 1
    return True
Str= input("Enter String: ")
if IsPali(Str):
    print("Palindrome")
else:
    print("Not Palindrome")