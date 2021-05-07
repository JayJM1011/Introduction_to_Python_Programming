def boolean_and(List):
    for i in List:
        if i == False:
            return False
    return True
def boolean_or(List):
    for i in List:
        if i == True:
            return True
    return False
def boolean_xor(List1):
    Len= len(List1)- 1
    List2= []
    for i in List1:
        if i == True:
            List2.append(1)
        if i == False:
            List2.append(0)
    for i in range(Len):
        List2[i+ 1]= List2[i]^ List2[i+ 1]
    if List2[Len] == 1:
        return True
    if List2[Len] == 0:
        return False
print(boolean_and([True, True, False, True]))
print(boolean_or([True, True, False, False]))
print(boolean_xor([True, True, False, False]))