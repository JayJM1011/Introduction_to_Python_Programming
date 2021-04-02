List1, List2= [1, 2, 3, 4, 5, 6, 7], [2, 4, 6]
Fil= filter(lambda x: x not in List2, List1)
print(list(Fil))