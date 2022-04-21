def factorial(num) :
  if num ==0:
      return 1
  else:
      return num*factorial(num-1)
a = factorial(8)
print("The factorial of the number is :",a)