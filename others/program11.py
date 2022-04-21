from re import A


string =input("Enter the sentence :")
count = 0
score = 0
for i in string :
    if (i.isalpha()) == True :
        count +=1
    elif(i.isnumeric() == True):
        score += 1
print(f"LETTER = {count} and NUMBER = {score}")