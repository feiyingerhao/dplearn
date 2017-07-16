import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)

# 合并后只有一个key
res = pd.merge(left, right, on='key')
# print(res)

# 多个进行合并的时候，只有当key完全相同的时候才会进行合并 默认how=inner，outer，left，inner
# 然后没有的数据是用NaN来代替
left2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})
right2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})
# print(left2)
# print(right2)
res2 = pd.merge(left2, right2, on=['key1', 'key2'], how='inner')
# print(res2)

# indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_left': [2, 2, 2]})
# print(df1)
# print(df2)
res3 = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# print(res3)
res4 = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
# print(res4)

# index merge
left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
right3 = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
# print(left3)
# print(right3)
res5 = pd.merge(left3, right3, left_index=True, right_index=True, how='outer')
res6 = pd.merge(left3, right3, left_index=True, right_index=True, how='inner')
# print(res5)
# print(res6)

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res7 = pd.merge(boys, girls, on='k', suffixes=['_boys', '_girl'], how='inner')
res8 = pd.merge(boys, girls, on='k', suffixes=['_boys', '_girl'], how='outer')
print(res7)
print(res8)
