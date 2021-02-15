import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from ..items import TirolItem

pattern = r'(\r)?(\n)?(\t)?(\xa0)?'

class SpiderSpider(scrapy.Spider):
    name = 'spider'

    start_urls = ['https://presse.rlb.info/page.cfm?vpath=rlb/pressemeldungen',
                  'https://presse.rlb.info/page.cfm?vpath=rlb/pressearchiv'
                  ]

    def parse(self, response):
            links = response.xpath('//div[@class="desc"]/a/@href').getall()
            yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(TirolItem())
        item.default_output_processor = TakeFirst()

        date = response.xpath('//span[@class="date"]//text()').get()
        title = response.xpath('//h1/text()').getall()
        title = re.sub(pattern, "", ''.join(title))
        content = response.xpath('//div[@class="artikel"]//text()').getall()
        content = ' '.join([text.strip() for text in content if text.strip()])
        content = re.sub(pattern, "", content)


        item.add_value('date', date)
        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)
        return item.load_item()