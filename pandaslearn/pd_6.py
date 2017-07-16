import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# join
df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df4)
print(df5)
# 如果没有的话，使用Nan填充
res2 = pd.concat([df4, df5], join='outer', ignore_index=True)
# 合并的时候只保留相同的
res3 = pd.concat([df4, df5], join='inner', ignore_index=True)
print(res3)

# join_axes=[df4.index] 因为序号有冲突
res4 = pd.concat([df4, df5], axis=1, join_axes=[df4.index])
print(res4)
# 一行一行添加
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res5 = df1.append(s1, ignore_index=True)
print(s1)
print(res5)

res6=df1.append(df2,ignore_index=True)
print(res6)