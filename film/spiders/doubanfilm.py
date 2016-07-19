# -*- coding=utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy import selector
from film.items import FilmItem


class doubanfilm(Spider):
    name = "doubanfilm"
    allowed_domains = ["movie.douban.com"]
    start_url = ['http://www.baidu.com']

    def parse(self, response):
        sel = selector(response)


        movie_name = sel.xpath('/div[@class="pl2"]/a/text()').extract()
        movie_star = sel.xpath('/div[@class="allstar45"]/span[@class=rating_nums]/text()').extract()
        movie_url = sel.xpath('/div[@class="pl2"]/a/@href').extract()

        item = FilmItem()
        item['movie_name'] = (n.encode('utf-8') for n in movie_name)
        item['movie_star'] = (n for n in movie_star)
        item['movie_url'] = (n for n in movie_url)
        yield item

        print movie_url,movie_star,movie_name