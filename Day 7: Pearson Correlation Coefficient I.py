import math

n = int(input())
# map will return iterator not a list
x = list(map(float, input().split()))
y = list(map(float, input().split()))

mean_x = sum(x) / n
std_dev_x = math.sqrt(sum([(xi - mean_x) ** 2 for xi in x]) / n)
mean_y = sum(y) / n
std_dev_y = math.sqrt(sum([(yi - mean_y) ** 2 for yi in y]) / n)

sigma_pearson = 0
for xi, yi in zip(x, y):
    sigma_pearson += (xi - mean_x) * (yi - mean_y)

pearson_corr = sigma_pearson / (n * std_dev_x * std_dev_y)
print(round(pearson_corr, 3))
