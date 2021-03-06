date, month, year, List= int(input("Enter Date: ")), int(input("Enter Month: ")), int(input("Enter Year: ")), []
if year% 4 != 0:
    List= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    List= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if date == List[month- 1]:
    date, month= 1, month+ 1
else:
    date+= 1
if month == 13:
    month, year= 1, year+ 1
print("Next Date is", date, "/", month, "/", year)