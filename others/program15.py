arr = input("Enter the transcations:").split(" ")
currentBalance = 0
for i in range(len(arr)):
    if(arr[i] == 'D'):
        currentBalance  = currentBalance + int(arr[i + 1])
    elif(arr[i] == 'W'):
        currentBalance  = currentBalance - int(arr[i + 1])
print(currentBalance)

