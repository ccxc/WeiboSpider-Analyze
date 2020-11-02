import pymongo
import pandas as pd
from collections import Counter

client = pymongo.MongoClient(host='localhost', port=27017)
db=client.weibo
collection=db.Tweets

'''
idSum=collection.find().count()
print(idSum)
i=0
l=[]
for j in collection.find({},{'comment_user_id':1,'_id':0}):
    #idCount[i]=collection.find_one().count()
    #print(collection.find_one({'comment_user_id':1}).count())
    l.append(str(j.values))
    #print(j)
result=Counter(l)
print(result)
d=sorted(result.items(),key=lambda x:x[1],reverse=True)
print(d)
'''
#datas=pd.DataFrame(list(collection.find()))
data=[]
for item in collection.find({},{"_id":1}):
    data.append(item['_id'])
print(data)
            
