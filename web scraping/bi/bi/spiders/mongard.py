import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MongardSpider(CrawlSpider):
    name = "mongard"
    allowed_domains = ["www.mongard.ir"]
    start_urls = ["https://www.mongard.ir/courses/"]

    rules = [
        Rule(LinkExtractor(allow=r"/courses/"), callback="parse_item", follow=True),
    ]

    def parse_item(self, response):
        item = {}

        item['title']=response.css('.item-box-title > span:nth-child(2)::text').get()
        return item
