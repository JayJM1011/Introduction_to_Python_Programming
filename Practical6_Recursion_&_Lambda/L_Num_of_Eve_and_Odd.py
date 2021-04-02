List= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Eve= filter(lambda x: x% 2 == 0, List)
Odd= filter(lambda x: x% 2 == 1, List)
print("Number of Even Nums:", len(list(Eve)))
print("Number of Odd Nums:", len(list(Odd)))