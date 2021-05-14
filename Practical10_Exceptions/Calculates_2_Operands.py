class Error(Exception):
    pass
class ForErr(Error):
    pass
String = str(input("Enter Formula : "))
if String.lower()=='quit':
    String= 'Ex + it'
Spl = String.split()

try:
    if len(Spl)!= 3:
        raise ForErr
    if Spl[0] != 'Ex':
        Spl[0] = float(Spl[0])
        Spl[2] = float(Spl[2])
    if Spl[1] not in ['+', '-', '*', '/', '%']:
        raise ForErr
    if Spl[1] == '+':
        print('Result =', Spl[0] + Spl[2])
    elif Spl[1] == '-':
        print('Result =', Spl[0] - Spl[2])
    elif Spl[1] == '*':
        print('Result =', Spl[0] * Spl[2])
    elif Spl[1] == '/':
        if Spl[2] == 0:
            raise ForErr
        print('Result =', Spl[0] / Spl[2])
    elif Spl[1] == '%':
        if Spl[2] == 0:
            raise ForErr
        print('Result =', Spl[0] % Spl[2])
except ForErr:
    print('Formula incorrect')