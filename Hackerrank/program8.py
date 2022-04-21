from os import remove


n = int(input())
arr = map(int,input().split())
a = list(set(arr))
a.remove(max(a))
print(max(a))