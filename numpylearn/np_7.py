import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)
# 对列进行分割，分为两列
print(np.split(A, 2, axis=1))
# 进行不等量的分割
print(np.array_split(A, 2, axis=0))

print(np.vsplit(A, 3))
print(np.hsplit(A, 2))
