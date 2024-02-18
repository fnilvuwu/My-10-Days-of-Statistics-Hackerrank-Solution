import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

x, y = map(float, input().split())
# n = 6 cause 6 children
b, p, n = 0, x/(x+y), 6
# 3 boys and 6 children so range(3, 7)
for i in range(3,7):
    b += bi_dist(i, n, p)   
print("%.3f" %b)
