def Fib(N):
   if N<= 1:  
       return N  
   else:  
       return(Fib(N- 1)+ Fib(N-2))
NoTerms = int(input("No of Terms: "))
if NoTerms <= 0:  
   print("No")  
else:   
   for i in range(NoTerms):
       print(Fib(i))