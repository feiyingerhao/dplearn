import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
# 上下合并
C = np.vstack((A, B))
print(C.shape)
# 左右合并
D = np.hstack((A, B))
print(D)
# 对A的横向加了一个维度
print(A[np.newaxis, :])

A2 = np.array([1, 1, 1])[:, np.newaxis]
B2 = np.array([2, 2, 2])[:, np.newaxis]
print(np.hstack((A2, B2)))

E=np.concatenate((A2,B2,B2,A2),axis=1)
print(E)