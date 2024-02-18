import math

mean, std_dev = map(float, input().split())

grade_1 = float(input())

def normal_cdf(x, mean, std_dev):
    return (1 + math.erf((x - mean) / (std_dev * math.sqrt(2)))) / 2

question_1 = 1 - normal_cdf(grade_1, mean, std_dev)

print(round(question_1 * 100, 2))

grade_2 = float(input())

question_2 = 1 - normal_cdf(grade_2, mean, std_dev)

print(round(question_2 * 100, 2))

question_3 = normal_cdf(grade_2, mean, std_dev)

print(round(question_3 * 100, 2))
