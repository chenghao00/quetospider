# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': None,
            'Accept-Language': 'en',
        }
    }

    def parse(self, response):
        pass
