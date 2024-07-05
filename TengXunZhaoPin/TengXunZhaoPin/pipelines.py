# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TengxunzhaopinPipeline:
    def process_item(self, item, spider):
        return item


import psycopg2


class TengxunzhaopinItemToPG:

    def __init__(self):
        self.conn = psycopg2.connect(
            database="flask",
            user="postgres",
            password="123456",
            host="192.168.200.19",
            port="5432",
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = "INSERT INTO tengxunzhaopin (job_name, job_address, job_type, job_time, job_responsibility, job_requiremnet) VALUES (%s, %s, %s, %s, %s,%s)"
            self.cur.execute(
                sql,
                (
                    item["job_name"],
                    item["job_address"],
                    item["job_type"],
                    item["job_time"],
                    item["job_responsibility"],
                    item["job_requiremnet"],
                ),
            )
            self.conn.commit()
        except Exception as e:
            print(e)
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
