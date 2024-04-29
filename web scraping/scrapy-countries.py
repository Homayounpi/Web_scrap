import scrapy
from scrapy.crawler import CrawlerProcess


class TekSpider(scrapy.Spider):
    name = 'Tek'

    def start_request(self):
        yield scrapy.Request('https://www.mongard.ir/courses/')

    def parse(self,response,**kwargs):
        for d in response.css('div.col-lg-12'):
            name = d.css('a.d-block::text').get()
            yield {'name':name}


Process = CrawlerProcess(settings={
    'FEEDS':{
        '/Users/Homayoun/Desktop/web scraping/mongard.json':{'format':'json','encoding':'utf8'},
        '/Users/Homayoun/Desktop/web scraping/mongard.csv':{'format':'csv'},
    }
})

Process.crawl(TekSpider)
Process.start()