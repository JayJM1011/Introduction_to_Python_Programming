date, month, year= int(input("Enter Date: ")), int(input("Enter Month: ")), int(input("Enter Year: "))
if date< 28:
  date+= 1
elif month == 2 and year% 4 == 0:
  if date == 29:
    date= 1
    month= 3
  else:
    date+= 1
elif date == 28 and month == 2 and year% 4 != 0:
  date= 1
  month= 3
elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
  if date==31:
    month+= 1
    date= 1
  else:
    date+= 1
elif month == 4 or 6 or 9 or 11:
  if date==30:
    month+= 1
    date= 1
  else:
    date+=1
if month == 13:
  month= 1
  year+=1
print(date,"/",month,"/",year)