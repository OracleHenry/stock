#coding:utf-8

import tushare as ts
import pandas as pd

df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
names=pd.DataFrame(ts.get_stock_basics())

goodlist=[]

try:
    for c in codes:
        good = True
        df = pd.DataFrame(ts.get_hist_data(code=str(c), start='2017-06-13', end='2017-06-14')).dropna()
        if not df.empty:
            p_change = list(df['p_change'].fillna(0))
            if p_change:
                for i in p_change:
                    if i:
                        if i <= 0:
                            good = False
                            break
                if good:
                    if str(c).startswith('002') or str(c).startswith('30'):
                        continue
                    else:
                        #print(c)
                        goodlist.append(c)

                else:
                    continue
except(Exception) as e:
    print(e)
else:
    print((names.ix[goodlist])[['name','industry']])
   





