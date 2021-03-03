#List l
l= [10, 20, 30, 40, 50]
i= len(l)- 1
while i>=0:
    print(l[i])
    i-= 1
for i in reversed(l):
    print(i)
for i in range(len(l)- 1, -2, -1):
    print (l[i])
print(l[::-1])