a=[int(x) for x in input().split()]
elm=set()
for i in range(len(a)):
    if a[i] in elm:
        print("YES")
    else:
        print("NO")
        elm.add(a[i])