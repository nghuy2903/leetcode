import cvxpy as cp
import numpy as np

# Dữ liệu
X = np.array([
    [5.7, 0.4, 1.5, 0.4],
    [5.4, 3.9, 1.3, 0.4],
    [-5.9, -3.0, -4.2, -1.5],
    [-6.0, -2.2, -4.0, -1.0]
])
y = np.array([1, 1, -1, -1])

# Biến tối ưu
w = cp.Variable(4)
b = cp.Variable()

# Hàm mục tiêu
objective = cp.Minimize(0.5 * cp.sum_squares(w))

# Ràng buộc
constraints = [y[i] * (X[i] @ w + b) >= 1 for i in range(4)]

# Bài toán
prob = cp.Problem(objective, constraints)
prob.solve()

print("w =", w.value)
print("b =", b.value)
