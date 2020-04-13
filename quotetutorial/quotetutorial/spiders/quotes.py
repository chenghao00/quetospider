# -*- coding: utf-8 -*-
import scrapy
from quotetutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    # 唯一的名字进行标识
    name = 'quotes'
    # 限制与开头的链接
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    # 进行解析的操作,response即使请求成功之后得到的response
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            # ::text --> 提取其中的文本信息  算是scrapy语法
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        # 获取下一页的url
        next = response.css('.pager .next a::attr(href)').extract_first()
        # 连接成新的url
        url = response.urljoin(next)
        # callback 对应的是：请求这个url参数之后 由谁处理
        # 用递归调用 实现了循环翻页
        yield scrapy.Request(url=url, callback=self.parse)
