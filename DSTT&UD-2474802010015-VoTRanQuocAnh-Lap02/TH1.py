import numpy as np

# Problem 1
A1 = np.array([[-1, 1],
               [2, 3]])
b1 = np.array([-2, 6])
x1 = np.linalg.solve(A1, b1)
print("Problem 1 - Point of intersection:", x1)

# Problem 2
A2 = np.array([[1, -1, 0],
               [2, -1, -1],
               [1, 1, 1]])
b2 = np.array([2, 3, 6])
x2 = np.linalg.solve(A2, b2)
print("Problem 2 - Point of intersection:", x2)

# Problem 3
A3 = np.array([[1, 1, 1],
               [4, 2, 1],
               [9, 3, 1]])
b3 = np.array([4, 3, 4])
x3 = np.linalg.solve(A3, b3)
print("Problem 3 - Polynomial coefficients [a, b, c]:", x3)

# Problem 4
A4 = np.array([[1, 0, 1],
               [1, -2, -1],
               [-2, 2, 1]])
b4 = np.array([1, -3, 0])
x4 = np.linalg.solve(A4, b4)
print("Problem 4 - Coefficients [a, b, c]:", x4)
