#1
#def OddCount(Arr):
#    cou, co= [], 0
#    list= []
#    for i in Arr:
#        if i not in list:
#            co= Arr.count(i)
#            cou.append(co)
#            list.append(i)
#    co= 0
#    for i in cou:
#        if i% 2 == 1:
#            co+= 1
#    return co
#Arr= [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
#print(OddCount(Arr))

#2
#def plu(Arr):
#    Ar2= []
#    for i in Arr:
#        if Arr.count(i)> 1:
#            Ar2.append(i+ 's')
#        if Arr.count(i) == 1:
#            Ar2.append(i)
#    Arr= []
#    for i in Ar2:
#        if i not in Arr:
#            Arr.append(i)
#    return Arr
#Arr= ['cow', 'pig', 'cow', 'cow']
#print(plu(Arr))