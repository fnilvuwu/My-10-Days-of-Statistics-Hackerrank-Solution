import math

x_mean = float(input())
prob_x = int(input())

result = x_mean ** prob_x * math.e ** -x_mean / math.factorial(prob_x)
print(round(result, 3))
