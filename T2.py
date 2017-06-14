import tushare as ts
import pandas as pd
#print(ts.top_list('2017-06-13')[['name','pchange','reason']])
df = ts.day_boxoffice() 
print(df)