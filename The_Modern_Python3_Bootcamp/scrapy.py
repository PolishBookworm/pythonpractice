import scrapy

class BooksSpider(scrapy.Spider):
	name = "bookspider"
	start_urls = ["https://books.toscrape.com/"]

	def parse(self, response):
		for article in response.css("article.product_pod"):
			yield {
				"price": article.css("price_color::text")
				"title": None
			}