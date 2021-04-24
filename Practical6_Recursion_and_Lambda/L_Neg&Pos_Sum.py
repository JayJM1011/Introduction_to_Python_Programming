Nums= [0, 5, -6, 12, 4, -8, 6, 7, -9, 10, -12, 15, 10, 25, -31]
Neg= filter(lambda x: x< 0, Nums)
NS= sum(Neg)
Pos= filter(lambda x: x> 0, Nums)
PS= sum(Pos)
print(NS)
print(PS)