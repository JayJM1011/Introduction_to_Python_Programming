import re
def ValidPass(Pass):
    if len(Pass)> 16 and len(Pass)< 6:
        return False
    elif not re.search("[a-z]", Pass): 
        return False
    elif not re.search("[A-Z]", Pass): 
        return False
    elif not re.search("[0-9]", Pass): 
#        return False
#    elif not re.search("[_@$]", Pass): 
#        return False
#    return True
#Pass= input("Enter Password: ")
#if ValidPass(Pass):
#    print("Valid Password")
#else:
#    print("Invalid Password")