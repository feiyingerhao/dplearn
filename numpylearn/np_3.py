import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print(a, b)
print(c)

c = b ** 2
print(c)

c = 10 * np.sin(a)
print(c)
print(b < 3)

a2 = np.array([[1, 1], [0, 1]])
b2 = np.arange(4).reshape((2, 2))
print(a2)
print(b2)

# 逐个相乘
print(a2 * b2)
# 矩阵乘法
print(np.dot(a2, b2))
print(a2.dot(b2))

a3 = np.random.random((2, 4))
print(a3)
print(np.sum(a3), np.max(a3), np.min(a3))
print(np.sum(a3, axis=1),np.min(a3,axis=1))
