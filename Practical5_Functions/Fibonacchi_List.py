def Fibonacci(Num):
    List, j= [1, 2], 0
    for i in range(3, Num+ 1, 1):
        left, right= List[j], List[j+ 1]
        if i == (left+ right):
            List.append(i)
            j+= 1
    print(FibBool(List, Num))
def FibBool(List, Num):
    if List[len(List)- 1] == Num:
        return True
    return False
Fibonacci(int(input("Enter Number: ")))