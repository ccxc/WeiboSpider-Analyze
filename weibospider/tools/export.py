import pandas as pd
import pymongo

# 连接mongodb数据库
client = pymongo.MongoClient("localhost")
# 连接数据库
db = client["weibo"]
# 数据表
#collection = db["Comments"]
collection = db["Tweets"]
#collection = db["Relationships"]

# 将mongodb中的数据读出
data = pd.DataFrame(list(collection.find()))

# 保存为csv格式
#data.to_csv('comments.csv', encoding='utf-8')
# 保存为xls格式
#data.to_excel('/root/spider/WeiboSpider/weibospider/output/relationships.xls', encoding='utf-8')
#data.to_excel('/root/spider/WeiboSpider/weibospider/output/comments.xls', encoding='utf-8')
data.to_excel('/root/spider/WeiboSpider/weibospider/output/tweets.xls', encoding='utf-8')