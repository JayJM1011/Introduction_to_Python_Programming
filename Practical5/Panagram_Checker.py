def Pana(Str):
    Alp= "ABCDEFGHIJKLMNOPKRSTUVWXYZ "
    for let in Alp:
        if let not in Str:
            return False
    return True
Str= (input("Enter String: ")).upper()
if Pana(Str):
    print("Panagram")
else:
    print("Not Panagram")