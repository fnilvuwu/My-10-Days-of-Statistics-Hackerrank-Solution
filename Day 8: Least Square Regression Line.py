n = 5
x = []
y = []

for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

sigma_x = sum(x)
mean_x = sigma_x/n
sigma_y = sum(y)
mean_y = sigma_y/n

sigma_square_x = sum([xi**2 for xi in x])
sigma_x_times_y = sum([xi*yi for xi, yi in zip(x, y)])

b = (n * sigma_x_times_y - sigma_x * sigma_y) / (n * sigma_square_x - sigma_x ** 2)

a = mean_y - b * mean_x

x_question = 80
y = a + b * x_question

print(round(y, 3)) 