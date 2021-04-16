from array import *
Arr, N= array("i", []), int(input("No of Elements: "))
for i in range(N):
    Arr.append(int(input()))
Max, Min= max(Arr), min(Arr)
print("The Range is", Max- Min)
print("The Coefficient is", (Max- Min)/ (Max+ Min))