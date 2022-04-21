num = input("Enter the number separted by a comma :").split(",")
for i in  range(len(num)) :
    a = int(num[i])
    if ( a % 2 != 0):
        print(a*a)