class Error(Exception):
    pass
class Neg(Error):
    pass
First, Second, Third= int(input()), int(input()), int(input())
try:
    if First< 0 or Second< 0 or Third< 0:
        raise Neg
    print('Addition is', (First**0.5 + Second ** 0.5 + Third ** 0.5))
except Neg:
    print("Negetive not Allowed")