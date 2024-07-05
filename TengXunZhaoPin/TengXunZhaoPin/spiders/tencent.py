import json
import scrapy
from urllib import parse
from .. import items
from datetime import datetime


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["careers.tencent.com", "tencent.wd1.myworkdayjobs.com"]
    # keyword = input("请输入你要搜索的关键字：")
    keyword = "python"
    keyword = parse.quote(keyword)
    total = 10
    timestamp = int(datetime.now().timestamp() * 1000)
    start_urls = [
        f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword={keyword}&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
    ]

    def parse(self, response):
        # 抓取所有的一级页面放入消息队列
        for i in range(1, self.total + 1):
            url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={self.timestamp}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword={TencentSpider.keyword}&pageIndex={i}&pageSize=10&language=zh-cn&area=cn"
            yield scrapy.Request(
                url=url, callback=self.parse_page, dont_filter=True
            )  # dont_filter=True 防止重复请求
        # &area=cn

    def parse_page(self, response):
        # 一级页面解析
        data = response.text

        one_html = json.loads(data)

        for item in one_html["Data"]["Posts"]:
            post_id = item["PostId"]
            tow_url = item["PostURL"]
            if "https://tencent.wd1.myworkdayjobs.com/" in tow_url:

                tow_url = tow_url.replace(
                    "https://tencent.wd1.myworkdayjobs.com/",
                    "https://tencent.wd1.myworkdayjobs.com/wday/cxs/tencent/",
                )

                yield scrapy.Request(url=tow_url, callback=self.get_job_info_v2)
            else:
                timestamp = int(datetime.now().timestamp() * 1000)
                tow_url = f"https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={timestamp}&postId={post_id}&language=zh-cn&area=cn"

                yield scrapy.Request(url=tow_url, callback=self.get_job_info_v1)

    def get_job_info_v1(self, response):

        if response.status == 200:
            data = response.text
            tow_html = json.loads(data)
            item = items.TengxunzhaopinItem()
            item["job_name"] = tow_html["Data"]["RecruitPostName"]
            item["job_address"] = tow_html["Data"]["LocationName"]
            item["job_type"] = tow_html["Data"]["CategoryName"]
            item["job_time"] = tow_html["Data"]["LastUpdateTime"]
            item["job_responsibility"] = tow_html["Data"]["Responsibility"]
            item["job_requiremnet"] = tow_html["Data"]["Requirement"]
            yield item
        else:
            print(f"请求失败: {response.url}")

    def get_job_info_v2(self, response):

        # 二级页面解析
        if response.status == 200:
            data = response.text

            tow_html = json.loads(data)

            item = items.TengxunzhaopinItem()
            item["job_name"] = tow_html["jobPostingInfo"]["title"]
            item["job_address"] = tow_html["jobPostingInfo"]["location"]
            item["job_type"] = tow_html["jobPostingInfo"]["timeType"]
            item["job_time"] = tow_html["jobPostingInfo"]["startDate"]
            res_req = tow_html["jobPostingInfo"]["jobDescription"].split("Requirements")
            item["job_responsibility"] = res_req[0]
            item["job_requiremnet"] = "Requirements" + res_req[1]

            yield item
        else:
            print(f"请求失败: {response.url}")
