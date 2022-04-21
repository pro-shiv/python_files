import math
# taking input
num = input("Enter the number :")
num = num.split(",")
print(num)
c = 50
h = 30
for i in range(len(num)):
    d = int(num[i])
    a = math.floor(math.sqrt((2 * c * d )/h))
    print(a)
