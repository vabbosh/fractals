# importing necessary modules
import matplotlib.pyplot as plt
import numpy as np

# initializing the affine transform
t1 = np.array([[0.195, -0.488, 0.4431], [0.344, 0.443, 0.2452], [0.0, 0.0, 1.0]])
t2 = np.array([[0.462, 0.414, 0.2511], [-0.252, 0.361, 0.5692], [0.0, 0.0, 1.0]])
t3 = np.array([[-0.058, -0.07, 0.5976], [0.453, -0.111, 0.0969], [0.0, 0.0, 1.0]])
t4 = np.array([[-0.035, 0.07, 0.4884], [-0.469, -0.022, 0.5069], [0.0, 0.0, 1.0]])
t5 = np.array([[-0.637, 0.0, 0.8562], [0.0, 0.501, 0.2513], [0.0, 0.0, 1.0]])

delta = 0.01
P = np.array([max(delta, np.abs(np.linalg.det(t1))),
              max(delta, np.abs(np.linalg.det(t2))),
              max(delta, np.abs(np.linalg.det(t3))),
              max(delta, np.abs(np.linalg.det(t4))),
              max(delta, np.abs(np.linalg.det(t5)))])

P = P / P.sum()

frac_ops = [lambda p: np.dot(t1, p),
            lambda p: np.dot(t2, p),
            lambda p: np.dot(t3, p),
            lambda p: np.dot(t4, p),
            lambda p: np.dot(t5, p)]

# init points array
N = 300000
np_points = np.zeros((2,N))
np_points = np.row_stack((np_points, np.ones((1,N))))

# generate the points
for i in range(N-1):
    np_points.T[i+1] = np.random.choice(frac_ops, p=P)(np_points.T[i])

plt.figure(figsize=(15, 15))
plt.scatter(np_points[0,10:], np_points[1,10:], s=0.2, edgecolor='green')

plt.savefig("./numpy-a-tree.png")

plt.show()
