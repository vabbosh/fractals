# importing necessary modules
import matplotlib.pyplot as plt
import numpy as np

# initializing the affine transform
stem = np.array([[0, 0, 0], [0, 0.16, 0], [0, 0, 1]])
small_leaflet = np.array([[0.85, 0.04, 0], [-0.04, 0.85, 1.6], [0, 0, 1]])
large_L_leaflet = np.array([[0.2, -0.26, 0], [0.23, 0.22, 1.6], [0, 0, 1]])
large_R_leaflet = np.array([[-0.15, 0.28, 0], [0.26, 0.24, 0.44], [0, 0, 1]])

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

x = []
y = []

# setting first element to 0
x.append(0)
y.append(0)

current = 0

for i in range(1, 500000):

    # generates a random integer between 1 and 100
    newPoint = np.random.choice(frac_ops, p=P)([x[current], y[current], 1])
    x.append(newPoint[0])
    y.append(newPoint[1])

    current = current + 1

plt.figure(figsize=(10, 20))
plt.scatter(x[100:], y[100:], s=0.2, edgecolor='green')

plt.savefig("./numpy-fern.png")

plt.show()

