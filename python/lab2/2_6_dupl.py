n=int(input())
m=int(input())
k=int(input())
if n==m and n==k:
    print(3)
elif n==m and m!=k:
    print(2)
elif n==k and n!=m:
    print (2)
elif m==k and m!=n:
    print (2)
else:
    print (0)
