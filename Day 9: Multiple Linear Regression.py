from sklearn import linear_model

# Initial data
x = []
y = []

# Taking input for additional data points
m, n = map(int, input().split())
for i in range(n):
    input_list = list(map(float, input().split()))
    x.append(input_list[:m])
    y.append(input_list[m])

# Fitting linear regression model
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

# Number of queries
q = int(input())

# Predicting values for feature sets and printing them
for i in range(q):
    input_feature_set = list(map(float, input().split()))
    prediction = lm.predict([input_feature_set])
    print(prediction[0])
