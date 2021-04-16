from array import *
Arr, N= array("i",[6]), int(input("No of Elements: "))
for i in range(0, N):
    Arr.append(int(input()))
print("Reversed array is:")
for i in range(N, 0, -1):
    print(Arr[i], end=" ")