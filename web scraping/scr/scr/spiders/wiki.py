import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags
# from ..items import ScrItem

# class WikiSpider(scrapy.Spider):
#     name = "wiki"
#     start_urls = ["https://www.scrapethissite.com/pages/simple/"]

#     def parse(self, response):
        # items = ScrItem()

        # for country in response.css('div.country'):
        #     name = remove_tags(country.css('h3.country-name').get()).strip()
        #     capital = country.css('span.country-capital::text').get()
        #     population = country.css('span.country-population::text').get()
        #     yield  {
        #         'name':name,'capital':capital,'population':population,
        #     }
            ## l = ItemLoader(item=ScrItem(),selector=country)
            ## l.add_css('name','h3.country-name')
            ## l.add_css('capital','span.country-capital::text')
            ## l.add_css('population','span.country-population::text')
            ## yield l.load_item()

# class WikiSpider(scrapy.Spider):
#     name = "wiki"
#     start_urls = ["https://www.bike-discount.de/en/bike"]
#     def parse(self, response):
#         for bike in response.css('a'):
#             # name=bike.css('a.product--title').get()
#             # status = remove_tags(bike.css('div.custom-btn-course-status ,span').get()).strip()
            
#             yield {'name':bike}
#             print('-------------')

#=============================================================
class WikiSpider(scrapy.Spider):
    name = "wiki_mid"
    start_urls = ["https://fa.wikipedia.org/wiki/%D8%B4%DA%A9%DB%8C%D8%B1%D8%A7"]
    def parse(self, response):
      
        pass           

            