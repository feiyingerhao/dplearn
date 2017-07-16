import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df['A'])
print(df[0:2])
print(df['20130102':'20130104'])

# 对行列信息筛选
print(df.loc['20130102'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20130102', ['A', 'B']])

# select by position:iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5, 1:3])
# mixed selection ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 8])
