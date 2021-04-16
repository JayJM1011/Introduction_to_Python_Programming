M1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2= [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
M= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            M[i][j]+= M1[i][k]* M2[k][j]
print(M)