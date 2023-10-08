n,m=[int(x) for x in input().split()]
anya=set()
borya=set()

for i in range(n):
    anya.add(input())

for i in range(m):
    borya.add(input())

print(len(anya.intersection(borya)))
print(*sorted(anya&borya, key=int))
print(len(anya.difference(borya)))
print(*sorted(anya.difference(borya),key=int))
print(len(borya.difference(anya)))
print(*sorted(borya.difference(anya)))






