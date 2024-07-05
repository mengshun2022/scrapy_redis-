# Scrapy settings for TengXunZhaoPin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "TengXunZhaoPin"

SPIDER_MODULES = ["TengXunZhaoPin.spiders"]
NEWSPIDER_MODULE = "TengXunZhaoPin.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "TengXunZhaoPin (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "TengXunZhaoPin.middlewares.TengxunzhaopinSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "TengXunZhaoPin.middlewares.TengxunzhaopinDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     "TengXunZhaoPin.pipelines.TengxunzhaopinPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 分布式爬虫
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # 使用scrapy_redis调度器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 使用scrapy_redis去重过滤器
REDIS_HOST = "192.168.200.19"  # redis地址
REDIS_PORT = 6379  # redis端口
# REDIS_PARAMS = {
#     "password": "123456",  # redis密码
#     "db": 0,  # redis数据库
# }
# 爬虫中间件
# DOWNLOADER_MIDDLEWARES = {
#     "scrapy_redis.downloadermiddlewares.RedisMiddleware": 543,
#     "scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware": 800,
# }
# 调度器中间件
# SPIDER_MIDDLEWARES = {
#     "scrapy_redis.spidermiddlewares.RedisSpiderMiddleware": 543,
# }
# 开启redis管道
ITEM_PIPELINES = {
    "scrapy_redis.pipelines.RedisPipeline": 200,  # 存入redis数据库
    "TengXunZhaoPin.pipelines.TengxunzhaopinPipeline": 300, 
    "TengXunZhaoPin.pipelines.TengxunzhaopinItemToPG": 400,  # 存入postgresql数据库
}

# 增量爬虫
SCHEDULER_PERSIST = True  # 不清除指纹 保留历史任务

# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"  # 优先级队列
# SCHEDULER_IDLE_BEFORE_CLOSE = 10  # 关闭爬虫前空闲时间
# SCHEDULER_DUPEFILTER_KEY = "%(spider)s:dupefilter"  # 去重键
# SCHEDULER_MEMORY_QUEUE_ENABLED = True  # 内存队列
