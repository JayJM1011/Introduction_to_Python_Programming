#Write a Python Program to create a mixed String using the s1 and s2.
#Print first char of s1 then the last char of s2, Next, the second
#char of s1 and second last char of s2, and so on.
#Any leftover characters should be printed at the last.

S1, S2= list(input('S1: ')), list(input('S2: '))
S, MinLen= [], min(len(S1), len(S2))
for i in range(MinLen):
    S.append(S1[i])
    S.append(S2[len(S2)- i- 1])
if len(S1)> len(S2):
    for j in range(MinLen, len(S1)):
        S.append(S1[j])
if len(S2)> len(S1):
    for j in range(len(S2)- MinLen- 1, -1, -1):
        S.append(S2[j])
print(''.join(S))