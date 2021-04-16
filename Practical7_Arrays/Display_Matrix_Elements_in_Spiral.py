import numpy
Arr= numpy.array([[1,2,3], [4,5,6], [7,8,9]])
for i in Arr[0,:]:
    print(i, end= " ")
for i in Arr[1:,-1]:
    print(i, end= " ")
for i in Arr[-1, -2:: -1] :
    print(i, end= " ")
for i in Arr[1, :2]:
    print(i, end= " ")