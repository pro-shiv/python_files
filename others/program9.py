bin = input("Enter the binary number to check the divisiblity : ").split(",")
for i in range (len(bin)):
    if (int(bin[i],2)%5==0) :
        print("Yes",bin[i])
    else:
        print("No,",bin[i], " it is not divisible by 5")