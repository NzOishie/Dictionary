# -*- coding: utf-8 -*-
import scrapy


class WordsSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['english-bangla.com']
    start_urls = ['http://english-bangla.com/browse/index/a']

    def parse(self, response):
        urls = response.css('div.a-z > a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_a_z)

    def parse_a_z(self, response):
        words = response.css('div#cat_page>ul>li>a::attr(href)').extract()
        for w in words:
            yield scrapy.Request(url=w, callback=self.parse_details)
        next_page_url = response.css('div.pagination>a::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse_a_z)

    def parse_details(self, response):
        yield {
            'word': response.css('span.word::text').extract_first(),
            'meaning': response.css('span.format1::text').extract_first().replace(u'\xa0', u' ').strip()
        }