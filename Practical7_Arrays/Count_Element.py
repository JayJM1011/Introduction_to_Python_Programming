from array import *
Arr, N= array("i", []), int(input("No of Elements: "))
for i in range(N):
    Arr.append(int(input()))
FreqOf, count= int(input("Frequency of? ")), 0
for i in Arr:
    if i == FreqOf:
        count+= 1
print("Frequency of", FreqOf, "is", count)