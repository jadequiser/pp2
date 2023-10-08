words=set()

for i in range(int(input())):
    for j in input().split():
        words.add(j)

print(len(words))
