from operator import truediv


num=int(input("Enter a number : "))
prime = True

for i in range(2,num):
    if (num%i==0):
      prime =False
      break
if prime:
   print("no. is prime")
else:
    print ("no.is not prime")

