# str1 = "yuzimou is a nice man"
# print(str1.center(40,"*"))

# import tushare
# data = tushare.get_hist_data('002230')  # 一次性获取全部日线数据
# data.to_excel('002230.xlsx')

# import tushare as ts
# pro = ts.pro_api()
# df = pro.daily(ts_code='002230.SZ', stat_daily='20200101',end_daily='20200429')
# df.to_csv("002230.csv")

import tushare
import pandas
df_hs300s = tushare.get_hs300s()
# DataFrame panda
print(df_hs300s['code'])

tickers = df_hs300s['code'].to_list()