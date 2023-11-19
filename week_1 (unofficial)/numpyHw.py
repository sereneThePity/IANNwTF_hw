import numpy as np

# 1. Create a 5x5 NumPy array filled with normally distributed (i.e. µ = 0,σ = 1)
mean = 0
std = 1
dimension = 5
normalArray = np.random.normal(loc=mean, scale=std, size=(dimension,dimension))

# 2. If the value of an entry is greater than 0.09, replace it with its square. Else, replace it with 42.

for i in range(dimension):
    for j in range(dimension):
        if normalArray[i,j]>0.09:
            normalArray[i,j] = normalArray[i,j]**2
        else:
            normalArray[i,j] = 42

# 3. Use slicing to print just the fourth column of your array.

print(normalArray[:,3])        