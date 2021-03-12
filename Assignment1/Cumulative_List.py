List, CumList, Sum= [5, 2, 6, 12, 6, 4, 8, 7, 19], [], 0
for i in range(len(List)):
    Sum+= List[i]
    CumList.append(Sum)
print(CumList)