# -*- coding: utf-8 -*-
import scrapy
from ..items import JobcollectorItem


class MonsterSpider(scrapy.Spider):
    name = 'monster'
    allowed_domains = ['monster.com']
    start_urls = ['http://monster.com/']

    def parse(self, response):
        items = JobcollectorItem()

        position = response.css('').extract()
        company = response.css('').extract()
        location = response.css('').extract()

        items['position'] = position
        items['company'] = company
        items['location'] = location

        yield items
