Alp, Str, Pan= "ABCDEFGHIJKLMNOPKRSTUVWXYZ ", input("Enter String: "), True
Str= Str.upper()
for let in Alp:
    if let not in Str:
        Pan= False
        break
if Pan:
    print("Panagram")
else:
    print("Not Panagram")