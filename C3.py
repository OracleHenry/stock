#coding:utf-8

import tushare as ts
import pandas as pd

df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
names=pd.DataFrame(ts.get_stock_basics())

goodlist=[]


for c in codes[100:199]:
        good = True
        df = pd.DataFrame(ts.get_hist_data(code=str(c), start='2017-06-07', end='2017-06-13')).fillna(-1)
        p_change = list(df['p_change'])

        for i in p_change:
            if i < 0:
                good = False
                continue
        if good:
            if str(c).startswith('002') or str(c).startswith('30'):
                continue
            else:
                goodlist.append(c)
        else:
            continue

#######################


names = names.reindex(goodlist)
for n in names['name']:
        if str(n).lower().startswith('n'):
            continue
        else:
            print(n)

