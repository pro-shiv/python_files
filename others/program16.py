password = input("Enter the passord : ").split(",")
def validatePassword(str):
    alpha = False
    numeric = False
    alnu = False
    for i in range(len(str)):
        if(len(str) >= 6 and len(str) <= 12):
            if((str[i].isalpha())):
                alpha = True
            elif(str[i].isnumeric()):
                numeric = True
            elif(str[i] == '@' or str[i] == '#' or str[i] == '$'):
                alnu = True
    return alpha and numeric and alnu

for i in range(len(password)):
    if(validatePassword(password[i])):
        print(password[i])
