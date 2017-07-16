import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

# 丢弃有nan的行
print(df.dropna(axis=0, how='any'))  # how={'any','all'} 当这一行所有的数据都等于none的时候才会丢弃该数据

# 对nan里面的数据填0
print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull()) == True)

