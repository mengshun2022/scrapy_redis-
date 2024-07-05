from scrapy import cmdline

cmdline.execute("scrapy crawl tencent -s LOG_FILE=tencent.log".split())