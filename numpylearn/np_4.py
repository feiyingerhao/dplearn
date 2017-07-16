import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A)
# 最小值和最大值的索引
print(np.argmin(A))
print(np.argmax(A))

print(np.mean(A))
print(A.mean())
print(np.average(A))
# 中位数
print(np.median(A))
# 逐步累加 累差
print(np.cumsum(A))
print(np.diff(A))
# 输出非零数的行数和列数
print(np.nonzero(A))
# 排序 逐行排序
print(np.sort(A))
# 矩阵的转置
print(np.transpose(A))
print(A.T)
# A里面所有小于5的数等于5，大于9的数等于9，中间的数保持不变
print(np.clip(A, 5, 9))
