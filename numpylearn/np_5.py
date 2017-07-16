import numpy as np

A = np.arange(3, 15)
print(A)
print(A[3])

A2 = np.arange(3, 15).reshape((3, 4))
print(A2)
print(A2[2])
print(A2[1, :])
print(A2[:, 1])
print(A2[1, 1:3])

print("for 行遍历:")
for row in A2:
    print(row)
print("for 列遍历:")
for column in A2.T:
    print(column)
for item in A2.flat:
    print(item)
