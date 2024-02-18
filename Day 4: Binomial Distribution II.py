import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

x, y = map(int, input().split())
b, p, n = 0, x/100, y
# No more than 2 rejects so x<=3
for i in range(0, 3):
    b += bi_dist(i, n, p)   
print("%.3f" %b)
    
b = 0
# At least 2 rejects so x>2
for i in range(2, n+1):
    b += bi_dist(i, n, p)   
print("%.3f" %b)
