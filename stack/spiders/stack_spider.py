import scrapy
from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    """docstring for StackSpider"""
    name = "stack"
    allowed_domains = ["laicode.com"]
    start_urls = ["http://www.laicode.com/accounts/login/index.html",]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'haoruzhao201503', 'password': '19881109'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "didn't match" in response.body:
            self.logger.error("Login failed")
            return
        self.logger.error("Login succeed")
        yield scrapy.Request(url='http://www.laicode.com/',callback = self.parse_items, dont_filter=True)

    def parse_items(self,response):
        questions = Selector(response).xpath('//div[@id = "problemlist"]/div[2]/div[1]')
        self.logger.error("Login succeed2")
        print questions
        # for question in questions:
        #     self.logger.error("get")
        #     item = StackItem()
        #     item['title'] = question.xpath(
        #         'div[1]/div[2]/text()').extract()[0]
        #     item['url'] = question.xpath(
        #         'a/@href').extract()[0]
        #
        #     yield item
