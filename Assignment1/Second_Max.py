List1, List2= [9, 5, 2, 8, 6, 5, 2, 4, 8, 1, 9], []
Max= max(List1)
for i in List1:
    if i != Max:
        List2.append(i)
SMax= max(List2)
print(SMax)