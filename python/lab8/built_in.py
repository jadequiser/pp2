import math
import time
# 1
def mltp(numbers):
    otv = math.prod(numbers)
    return otv
list=[2, 3, 4, 5]
res1=mltp(list)
print(res1)

# 2
def cnt(line):
    cntU=0
    cntL=0
    for i in range(0, len(line)):
        if line[i].isupper():
            cntU+=1
        if line[i].islower():
            cntL+=1
    return cntU,cntL

inputt='AbcRda'
res2=cnt(inputt)
print(res2)

# 3
def pal(s):
    t=''.join(reversed(s))
    if t==s:
        return True
    else:
        return False
ans3=pal('abba')
print(ans3)

# 4
def sq_root(n,s):
    time.sleep(s/1000) 
    return math.sqrt(n)
n=float(input())
s=int(input())
ans4=sq_root(n,s)
print(f"Square root of {n} after {s} milliseconds is {ans4}")

# 5
def tuple_true(t):
    return all(t)
ex=(True, False, True)
ans5=tuple_true(ex)
print(ans5)






    


