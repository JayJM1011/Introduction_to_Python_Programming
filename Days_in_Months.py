month, year = input('Enter Month: '), int(input('Enter Year: '))
if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print(31)
if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(30)
if month == 'February' and int(year% 4) != 0:
    print(28)
if month == 'February' and int(year% 4) == 0:
    print(29)