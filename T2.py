import tushare as ts
import pandas as pd
df=pd.DataFrame(ts.get_today_all())
df1=df[['name','code']]
print(df1)