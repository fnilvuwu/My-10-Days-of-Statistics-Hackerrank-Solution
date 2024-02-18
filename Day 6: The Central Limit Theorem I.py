import math

max_weight = float(input())
n = int(input())
mean = float(input())
std_dev = float(input())

total_mean = n * mean
total_std_dev = math.sqrt(n) * std_dev

def normal_cdf(x, mean, std_dev):
    return (1 + math.erf((x - mean) / (std_dev * math.sqrt(2)))) / 2

result = normal_cdf(max_weight, total_mean, total_std_dev)

print(round(result, 4))
