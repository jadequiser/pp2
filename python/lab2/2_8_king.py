x1=int (input())
y1=int (input())
x2=int (input())
y2=int (input())

if x1+1==x2:
    if y1-1==y2 or y1==y2 or y1+1==y2:
        print ("YES")
    else:
        print ("NO")
elif x1-1==x2:
    if y1-1==y2 or y1==y2 or y1+1==y2:
        print ("YES")
    else:
        print ("NO")
elif x1==x2:
    if y1-1==y2 or y1+1==y2:
        print ("YES")
    else:
        print ("NO")
else:
    print ("NO")