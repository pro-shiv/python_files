string = input("Enter the sentance : ")
count = 0
count_lower = 0
count_space = 0
for i in string :
    if (i.isupper()) == True:
        count +=1
    elif (i.islower()) == True :
        count_lower +=1
    elif (i.isspace()) == True :
        count_space +=1
print(f"UPPERCASE : {count} LOWERCASE : {count_lower} SPACES :{count_space}")