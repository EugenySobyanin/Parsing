import scrapy

from yatube_parsing.items import YatubeParsingItem


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    allowed_domains = ["158.160.177.221"]
    start_urls = ["http://158.160.177.221/"]

    def parse(self, response):
        for post in response.css('div.card-body'):
            data = {
                'author': post.css('strong::text').get(),
                'text': ''.join(
                    t.strip() for t in post.css('p::text').getall()
                ).strip(),
                'date': post.css('small.text-muted::text').get(),
            }
            yield YatubeParsingItem(data)
        # Ссылка на следующую страницу с использованием Xpath селектора
        next_page = response.xpath("//a[contains(., 'Следующая')]/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)