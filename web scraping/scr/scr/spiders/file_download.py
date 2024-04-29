import scrapy
from scr.items import ScrItem



class WikiSpider(scrapy.Spider):
    name = 'file_download'
    start_urls = ['https://www.technolife.ir/product/list/164_163_876/%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1-%D9%88-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DA%86-%D9%BE%DB%8C-hp',]
    def parse(self, response, **kwargs):
        item = ScrItem()
        image_urls = []
        for bike in response.css('div.flex'):
            img_url = bike.css('img::attr(src)').get()# if bike.css('img::attr(src)').get()  
            image_urls.append(img_url)
        item['file_urls']=image_urls
        yield item
	 
		
            
