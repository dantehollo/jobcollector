# -*- coding: utf-8 -*-
import scrapy
from ..items import JobcollectorItem


class ZiprecruiterSpider(scrapy.Spider):
    name = 'ziprecruiter'
    allowed_domains = ['ziprecruiter.com']
    start_urls = ['http://ziprecruiter.com/']

    def parse(self, response):
        items = JobcollectorItem()

        position = response.css('').extract()
        company = response.css('').extract()
        location = response.css('').extract()

        items['position'] = position
        items['company'] = company
        items['location'] = location

        yield items
