#coding:utf-8
import xlrd
import openpyxl
import xlwt
import tushare as ts
import pandas as pd
import os,sys,string
df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
names=pd.DataFrame(ts.get_stock_basics())

goodlist=[]
goodlist1=[]

try:
    for c in codes[0:10]:
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
                        #goodlist1.append(str(''.join(' '.join(str(c)).split())))
                        

                else:
                    continue
except(Exception) as e:
    print(e)
else:
   res= (names.ix[goodlist])[['name','industry']]
   #res['code']=goodlist1
   #res.to_csv('d:\\Temp\\stock.csv',encoding="utf_8_sig")
   res.to_excel('d:\\Temp\\stock1.xls',sheet_name='fuck')
    
   





