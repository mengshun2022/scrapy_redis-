# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunzhaopinItem(scrapy.Item):
    job_name: str = scrapy.Field()
    job_address: str = scrapy.Field()
    job_type: str = scrapy.Field()
    job_time: str = scrapy.Field()
    job_responsibility: str = scrapy.Field()
    job_requiremnet: str = scrapy.Field()


