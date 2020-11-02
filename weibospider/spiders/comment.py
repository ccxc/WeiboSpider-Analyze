#!/usr/bin/env python
# encoding: utf-8

import re
from lxml import etree
from scrapy import Spider
from scrapy.http import Request
import time
from items import CommentItem
from spiders.utils import extract_comment_content, time_fix
from items import TweetItem
#from spiders.tweet import *
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db=client.weibo
collection=db.Tweets


class CommentSpider(Spider):
    name = "comment_spider"
    base_url = "https://weibo.cn"
    
    #a=TweetSpider(Spider)
    #a.start_requests(self)
    #a.parse(self, response)
    #a.parse_all_content(self, response)

    def start_requests(self):
        #tweet_ids = ['JodbssFDE', 'JnPQV4Lky', 'JnuGKhT4k','Jnkbzszua','JhHy6dYGS']
        #tweet_ids=[]
        #for tweet_node in TweetSpider.tweet_nodes:
        #    tweet_ids.append(tweet_node.tweet_item['_id'])  
        #weibo_ids=TweetSpider.tweet_ids
        #print(weibo_ids)

        tweet_ids=[]
        for item in collection.find({},{"_id":1}):
            tweet_ids.append(item['_id'])
        urls = [f"{self.base_url}/comment/hot/{tweet_id}?rl=1&page=1" for tweet_id in tweet_ids]
        for url in urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        if response.url.endswith('page=1'):
            all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
            if all_page:
                all_page = all_page.group(1)
                all_page = int(all_page)
                all_page = all_page if all_page <= 50 else 50
                for page_num in range(2, all_page + 1):
                    page_url = response.url.replace('page=1', 'page={}'.format(page_num))
                    yield Request(page_url, self.parse, dont_filter=True, meta=response.meta)
        tree_node = etree.HTML(response.body)
        comment_nodes = tree_node.xpath('//div[@class="c" and contains(@id,"C_")]')
        for comment_node in comment_nodes:
            comment_user_url = comment_node.xpath('.//a[contains(@href,"/u/")]/@href')
            if not comment_user_url:
                continue
            comment_item = CommentItem()
            comment_item['crawl_time'] = int(time.time())
            comment_item['weibo_id'] = response.url.split('/')[-1].split('?')[0]
            comment_item['comment_user_id'] = re.search(r'/u/(\d+)', comment_user_url[0]).group(1)
            #comment_item['content'] = extract_comment_content(etree.tostring(comment_node, encoding='unicode'))
            comment_item['_id'] = comment_node.xpath('./@id')[0]
            #created_at_info = comment_node.xpath('.//span[@class="ct"]/text()')[0]
            #like_num = comment_node.xpath('.//a[contains(text(),"赞[")]/text()')[-1]
            #comment_item['like_num'] = int(re.search('\d+', like_num).group())
            #comment_item['created_at'] = time_fix(created_at_info.split('\xa0')[0])
            yield comment_item
