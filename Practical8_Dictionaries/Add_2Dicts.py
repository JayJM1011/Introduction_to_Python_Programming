D1= {'apple': 1800, 'banana': 2500, 'coconut': 4300}
D2= {'apple': 3000, 'banana': 2000, 'grapes': 4000}
D3= {}
for i in D1:
    if i in D2.keys():
        D3.update({i: D1[i]+ D2[i]})
    if i not in D2.keys():
        D3.update({i: D1[i]})
for j in D2:
    if j not in D1.keys():
        D3.update({j: D2[j]})
print(D3)