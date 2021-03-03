def hcf(a, b):
  if(a<=b):
    small= a
  else:
    small= b
  for i in range(1, small+ 1):
    if((a% i==0) and (b% i==0)):
      hcf= i
  return hcf
No1, No2= int(input("No1: ")), int(input("No2: "))
print("HCF is", hcf(No1, No2))