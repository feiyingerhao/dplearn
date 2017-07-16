import numpy as np

# 浅拷贝
a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
print(b)

# 深拷贝
e = a.copy()
a[0] = 22
print(e)
