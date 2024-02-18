import math

def compute_confidence_interval(sample_size, mean, std_dev, confidence_level, z_score):
    margin_of_error = z_score * (std_dev / math.sqrt(sample_size))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound

sample_size = int(input())
mean = float(input())
std_dev = float(input())
confidence_level = float(input())
z_score = float(input())

lower_bound, upper_bound = compute_confidence_interval(sample_size, mean, std_dev, confidence_level, z_score)

print(round(lower_bound, 2))
print(round(upper_bound, 2))
