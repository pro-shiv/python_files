N = int(input())
list = []
for i in range(N):
    operation = input()
    n = operation.split(" ")
    if n[0] == "append":
        list.append(int(n[1]))
    elif n[0] == "remove":
        list.remove(int(n[1]))
    elif n[0] == "insert":
        list.insert(int(n[1]), int(n[2]))
    elif n[0] == "sort":
        list.sort()
    elif n[0] == "reverse":
        list.reverse()
    elif n[0] == "pop":
        list.pop()
    elif n[0] == "print":
        print(list)
    
