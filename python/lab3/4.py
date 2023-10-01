a = [int(s) for s in input().split()]

for i in range(1,len(a)):
    if a[i-1]>0 and a[i]>0:
        print (a[i-1], a[i])
        break
    elif a[i-1]<0 and a[i]<0:
        print (a[i-1], a[i])
        break