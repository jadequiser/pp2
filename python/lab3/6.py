a = [int(s) for s in input().split()]
max=-1e10
index=-1
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        index=i
print(max, index)