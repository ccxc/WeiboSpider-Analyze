import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db=client.weibo
col_comment=db.Comments
col_weibo=db.Tweets
coms1=db.Coms1 #[{'user_id':2052320590}]
coms2=db.Coms2 #[{'user_id':1721987202}]
coms3=db.Coms3 #[{'user_id':1825457341}]
'''
results1=col_comment.find({'weibo_id':'IuYJ2nfCP'})
'''
'''
results1=col_weibo.aggregate(
    [

        {
            '$lookup':{
                    'from': "col_comment", 
                    'localField': "_id",  
                    'foreignField': "weibo_id", 
                    'as': "join"  
            }
        },
        #{
         #   '$match':{
         #       'user_id':2052320590
         #   }
        #},
        {
            '$project':{
                'user_id':1,
                'weibo_id':1,
                '_id':0,
                'comment_user_id':1
            }
        },
        
        {
            '$out':"coms"
        }
    ]
)
'''

results2=coms3.aggregate(
    [
        {
            '$group':{
                '_id':'$comment_user_id',
                'count':{
                    '$sum':1
                }
            }
        },
        {
            '$sort':{
                'count':-1
            }
        },
        {
            '$limit':10
        },
        {
            '$project':{
                '评论用户ID':'$_id',
                '评论总数':'$count',
                '_id':0
            }
        }
    ]
)

#print(jsonb.dumps(list(results)))
#resultx=[r for r in results1]
#print(resultx)
#for result in resultx:
#    print(result)
for o in results2:
    print(o)
