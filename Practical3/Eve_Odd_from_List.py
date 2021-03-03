List= [1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 20, 22, 24, 25]
Eve, Odd= [], []
for i in range(len(List)):
  if List[i]% 2==0:
    Eve.append(List[i])
  else:
    Odd.append(List[i])
print(Eve, Odd)