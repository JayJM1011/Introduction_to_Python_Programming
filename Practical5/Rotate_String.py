def LeftRot(String, x):
    Left= String[x: ]+ String[0: x]
    return Left
def RightRot(String, x):
    Right= String[-(x): ]+ String[0: -(x)]
    return Right
String, x= input("Enter String: "), int(input("Enter x: "))
print("Left Rotation:", LeftRot(String, x))
print("Right Rotation:", RightRot(String, x))