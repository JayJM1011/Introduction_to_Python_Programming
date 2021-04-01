# Over 130 is insta Suspend
def Judge(speed):
    if speed > 70:
        points= (speed- 70)// 5
        if points < 13:
            print("Points:", points)
        else:
            print("License Suspended")
    else:
        print("Good! Maintain the speed!")
Judge(int(input("Enter Speed:")))