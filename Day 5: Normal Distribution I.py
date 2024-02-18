import math

mean, std_dev = map(float, input().split())

x = float(input())

def normal_cdf(x, mean, std_dev):
    return (1 + math.erf((x - mean) / (std_dev * math.sqrt(2)))) / 2

question_1 = normal_cdf(x, mean, std_dev)

print(round(question_1, 3))

a, b = map(float, input().split())

question_2 = normal_cdf(b, mean, std_dev) - normal_cdf(a, mean, std_dev) 

print(round(question_2, 3))
