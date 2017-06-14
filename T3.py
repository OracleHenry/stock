#coding:utf-8

import tushare as ts
import pandas as pd

df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
names=pd.DataFrame(ts.get_stock_basics())

print(names)
    
        




