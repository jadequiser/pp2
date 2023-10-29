import math
# 1
def d_to_r(d):
    radian=d*(math.pi)/180
    return radian

radian=float(d_to_r(180))
print(radian)

# 2
def trapezoid(h,a,b):
    return (a+b)*h/2
h=float(input())
a=float(input())
b=float(input())
tr=trapezoid(h,a,b)
print(tr)

# 3
num_of_sides=float(input())
length=float(input())
area=(num_of_sides*pow(length,2))/(4*math.tan(math.pi/num_of_sides))
print(area)
# 4
def parallelogram(b,l):
    return b*l
b=int(input())
l=int(input())
par=parallelogram(b,l)
print(float(par))