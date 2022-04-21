marksheet = []
scorelist = []
n = int(input())
for i in range(n):
        name = input()
        score = float(input())
        record = [name , score]
        marksheet.append(record)
        scorelist.append(score)
marksheet.sort()
secondlowest = sorted(set(scorelist))[1]
for i , j in marksheet:
        if j == secondlowest:
                print(i)