a = [int(s) for s in input().split()]

for i in range(len(a)):
    if a[i]>a[i-1] and i!=0:
        print(a[i])