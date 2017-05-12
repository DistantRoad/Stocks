from sqlalchemy import create_engine
import tushare as ts

# 首先下载一个股票列表，并更新本地股票列表

# 对于每一支股票，如果相应股票文件不存在：
# 下载所有历史数据，并保存相应文件
# 否则，查看文件中最后一天数据日期，下载至今数据并追加保存到相应文件
print(ts.get_stock_basics())
