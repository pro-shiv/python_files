input_string = input("Enter the input word :").split(" ")
res = []
for i in input_string:
    if i not in res:
        res.append(i)
       
print(sorted(res))                       
