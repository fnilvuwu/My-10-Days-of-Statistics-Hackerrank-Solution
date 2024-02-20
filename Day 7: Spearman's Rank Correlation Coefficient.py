n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
rx = sorted(list(dict.fromkeys(X)))
ry = sorted(list(dict.fromkeys(Y)))
rx = [rx.index(i) + 1 for i in X]
ry = [ry.index(i) + 1 for i in Y]
di = [rx[i] - ry[i] for i in range(n)]

rxy = 1 - (6 * sum([i ** 2 for i in di])) / (n * (n ** 2 - 1))
print(round(rxy, 3))



