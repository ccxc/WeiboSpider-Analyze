# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'SSOLoginState=1602472533; ALF=1605064533; SCF=AiX6oZiMho4ywuhjhIyQvn9ppujqk7HPMGETCH5xgj9aBjlVbkZG318JV9gGCx7iPfWJ9FNQH786a1iwnRF5g-4.; SUB=_2A25yh7oFDeRhGeNN4lAR-S7JyjmIHXVRi8ZNrDV6PUNbktANLWbMkW1NSZGgqXTzWkB_obzacEgCrpTJtCzdN8PL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhA1gZY.JU97n8Ldc3_IOuW5JpX5KMhUgL.Fo-01Kz71K5feK-2dJLoIp-LxK-LB-BLBKqLxKqL1-eLB-9bdNBt; SUHB=03oVzB1Eiq1H2-; _T_WM=0fd69d2f7a3d90d0f6c8e72e7603516a'
}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
