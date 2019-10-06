import numpy as np
import distance_fn as d


a = np.array([1,2,3])
b = np.array([2,3,4])

print(d.hamming_dist(a,b))
print(d.manhattan_dist(a,b))
print(d.euclidean_dist(a,b))
print(d.minkowski_dist(a,b,3))
print(d.chebyshev_dist(a,b))
