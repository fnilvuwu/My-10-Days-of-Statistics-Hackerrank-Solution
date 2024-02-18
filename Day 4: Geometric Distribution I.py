def geo_dist(n, p):
    b = ((1-p)**(n-1))*(p)
    return(b)

print(round(geo_dist(5, 1/3), 3))
