import statistics
_ = input()
data = list(map(int, input().split()))
# Finding Mean
print(statistics.mean(data))
 
# Finding Median
print(statistics.median(data))
 
# Finding Single Mode
print(min(statistics.multimode(data)))
