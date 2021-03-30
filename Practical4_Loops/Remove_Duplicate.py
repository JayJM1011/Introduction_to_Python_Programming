List1, List2= [5, 5, 4, 6, 4, 5, 6, 6, 4], []
for i in List1:
    if i not in List2:
        List2.append(i)
print(List2)