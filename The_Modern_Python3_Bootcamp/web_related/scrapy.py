import scrapy

class BookSpider(scrapy.Spider):
    name = "bookspider"
    starturls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for article in response.css("article.product_pod"):
            yield {
                "price": article.css(".price_color::text")
            }
