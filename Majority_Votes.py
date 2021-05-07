def Majority(List):
    Dict, Max, Who= {}, 0, ''
    for i in List:
        Dict.update({i: List.count(i)})
    for i in Dict.keys():
        if Dict[i] > Max:
            Max= Dict[i]
            Who= i
        elif Dict[i] == Max:
            return 'None'
    return Who
print(Majority(['A', 'A', 'B']))
print(Majority(['A', 'A', 'A', 'B', 'C', 'A']))
print(Majority(['A', 'B', 'B', 'A', 'C', 'C']))