def Square(num):
    if num< 1:
        return False
    for i in range(num+ 1):
        if i*i == num:
            return True
    return False
num= int(input("Enter Number: "))
if(Square(num)):
    print("Perfect Square")
else:
    print("Not a Valid Square")