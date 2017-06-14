#coding:utf-8

import tushare as ts
import pandas as pd

df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
names=pd.DataFrame(ts.get_stock_basics())

goodlist=[]


######################

ra=[]
for x in range(1,33):
    ra.append(((x-1)*100,x*100-1))

#######################

#for x1, y1 in ra:
    for c in codes[0:99]:
        good = True
        df = pd.DataFrame(ts.get_hist_data(code=str(c), start='2017-06-07', end='2017-06-14')).fillna(-1)
        p_change = list((df['p_change']))

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

