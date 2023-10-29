#1
def squares(n):
    squares=[]
    for i in range(1, n+1):
        squares.append(i*i)
    yield squares
sq=squares(5)
print(*next(sq))

#2
def even(n):
    even=[]
    for i in range(0, n+1):
        if i%2==0:
            even.append(i)
    yield even

ev=even(int(input()))
print(*next(ev))


#3
def thfr(n):
    thfr=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            thfr.append(i)
    yield thfr

thr=thfr(int(input()))
print(*next(thr))

#4
def sq(a,b):
    for i in range(a,b):
        yield i*i

gen = sq(3,12)
for i in range(12-3):
    print(next(gen))
    
#5
def down(n):
    for i in reversed(range(n)):
        yield i

d=down(7)
for i in range (7):
    print(next(d))