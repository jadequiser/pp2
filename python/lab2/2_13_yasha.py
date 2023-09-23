n=int (input())
m=int (input())
x=int (input())
y=int (input())

if n>m:
    temp = n
    n = m
    m = temp
    
if n-x>x:
    ans=x
elif n-x<x:
    ans=n-x
if m-y>y:
    ans2=y
elif m-y<y:
    ans2=m-y
    
if ans>ans2:
    print (ans2)
else:
    print (ans)



