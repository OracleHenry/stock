import tushare as ts
import pandas as pd

df=pd.DataFrame(ts.get_stock_basics())
codes=df.index
print(len(codes))
print(ts.get_hist_data('600848'))