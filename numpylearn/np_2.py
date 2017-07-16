import numpy as np

a = np.array([2, 23, 4], dtype=np.float)
print(a.dtype)

a2 = np.array([[2, 23, 4], [2, 23, 4]], dtype=int)
print(a2)

a3 = np.zeros(shape=(3, 4))
print(a3)

a4 = np.ones(shape=(3, 4), dtype=int)
print(a4)

# 结果接近于0
a5 = np.empty(shape=(3, 4))
print(a5)

a6 = np.arange(10, 20, 2)
print(a6)

a7 = np.arange(12).reshape((3, 4))
print(a7)

# 生成线段
a8 = np.linspace(1, 10, 5)
print(a8)


