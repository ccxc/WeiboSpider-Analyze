# WeiboSpider-Analyze
Analyze relationship network with comment times and so on among tweets themselves. Modified from https://github.com/nghuyong/WeiboSpider/

## Step1
You should set up and learn how to crawl data from weibo.cn in https://github.com/nghuyong/WeiboSpider/tree/simple
## Step2
Learn how to use MongoDB, especially aggregate pipeline and lookup functions. Combine them with pymongo library and write with python.
## Step3
Print them if you need to use Excel through mongoexport library.
## Tips
1. When compiling WeiboSpider, you should confirm your python version and unify all system's version, otherwise the spider cannot be started.
2. If MongoDB cannot return any results with pymongo but do in MongoDB terminal, you should try to use "_id" enrty in String mode.
3. Contact me with Issues and I am glad to help you if you have any problems.
