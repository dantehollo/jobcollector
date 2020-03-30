# -*- coding: utf-8 -*-
import scrapy
from ..items import JobcollectorItem
from ..AutoCrawler import searchIndeed


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    page_number = 2
    start_urls = [searchIndeed.current_page_url]

    def parse(self, response):
        items = JobcollectorItem()

        position = response.css('.jobtitle::text').extract()
        company = response.css('span.company::text').extract()
        location = response.css('.location::text').extract()

        # print(position[0])

        items['position'] = position
        items['company'] = company
        items['location'] = location

        # for key in items:
        #     for value in items[key]:
        #         prestripped = items[key][value]
        #         stripped = prestripped.strip()
        #         items[key][value] = stripped

        yield items
