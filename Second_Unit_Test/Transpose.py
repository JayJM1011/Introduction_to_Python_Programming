A=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Result is:")
for i in range(4):
    Str= ""
    for j in range(4):
        Str+= str(A[j][i])+ "\t"
    print(Str)