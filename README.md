# scrapy_redis
腾讯招聘职位爬虫
分布式爬虫
普通爬虫-》分布式爬虫
# 分布式爬虫
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # 使用scrapy_redis调度器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 使用scrapy_redis去重过滤器
REDIS_HOST = "192.168.200.19"  # redis地址
REDIS_PORT = 6379  # redis端口
# 开启redis管道
ITEM_PIPELINES = {
    "scrapy_redis.pipelines.RedisPipeline": 200,  # 存入redis数据库
    "TengXunZhaoPin.pipelines.TengxunzhaopinPipeline": 300, 
    "TengXunZhaoPin.pipelines.TengxunzhaopinItemToPG": 400,  # 存入postgresql数据库
}

# 增量爬虫
SCHEDULER_PERSIST = True  # 不清除指纹 保留历史任务
