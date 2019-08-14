# importing necessary modules
import matplotlib.pyplot as plt
import numpy as np

# initializing the affine transform
stem = np.array([[0, 0, 0.5], [0, 0.16, 0], [0, 0, 1]])
small_leaflet = np.array([[0.849, 0.037, 0.075], [-0.037, 0.849, 0.183], [0, 0, 1]])
large_L_leaflet = np.array([[0.197, -0.226, 0.4], [0.226, 0.197, 0.049], [0, 0, 1]])
large_R_leaflet = np.array([[-0.15, 0.283, 0.575], [0.26, 0.237, -0.084], [0, 0, 1]])

delta = 0.01
P = np.array([max(delta, np.abs(np.linalg.det(stem))),
              max(delta, np.abs(np.linalg.det(small_leaflet))),
              max(delta, np.abs(np.linalg.det(large_L_leaflet))),
              max(delta, np.abs(np.linalg.det(large_R_leaflet)))])

P = P / P.sum()

frac_ops = [lambda p: np.dot(stem, p),
            lambda p: np.dot(small_leaflet, p),
            lambda p: np.dot(large_L_leaflet, p),
            lambda p: np.dot(large_R_leaflet, p)]

# init points array
N = 300000
np_points = np.zeros((2,N))
np_points = np.row_stack((np_points, np.ones((1,N))))

# generate the points
for i in range(N-1):
    np_points.T[i+1] = np.random.choice(frac_ops, p=P)(np_points.T[i])

# Draw the fern
plt.figure(figsize=(8, 15))
plt.scatter(np_points[0,10:], np_points[1,10:], s=0.2, edgecolor='green')

plt.savefig("./numpy-fern.png")

plt.show()

