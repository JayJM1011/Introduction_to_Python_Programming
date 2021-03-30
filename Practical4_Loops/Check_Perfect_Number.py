def isperf(No):
    sum= 1
    for i in range(2, No):
        if No% i == 0:
            sum+= i
    if sum == No:
        return True
    return False
if(isperf(int(input("Enter the Number: ")))):
    print("Number is perfect")