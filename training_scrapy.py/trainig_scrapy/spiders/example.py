import scrapy

from trainig_scrapy.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/',]

    def parse(self, response):
        for quote in response.css('div.quote'):
            # Заменили return на yield.
            data = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('a.tag::text').getall(),
            }
            yield QuoteItem(data)
            

        # По CSS-селектору ищем ссылку на следующую страницу.
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # Если ссылка нашлась, загружаем страницу по ссылке
            # и вызываем метод parse() ещё раз.
            yield response.follow(next_page, callback=self.parse)
