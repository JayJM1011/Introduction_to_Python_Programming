No= int(input("Enter Number: "))
temp, sum= No, 0
digi= len(str(No))
while temp> 0:
  sum+= (temp% 10)**digi
  temp//= 10
if sum == No:
  print("Armstrong")
else:
    print("Not Armstrong")