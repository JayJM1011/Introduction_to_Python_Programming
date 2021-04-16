M1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2= [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
for i in range(3):
    for j in range(3):
        M1[i][j]+= M2[i][j]
print(M1)