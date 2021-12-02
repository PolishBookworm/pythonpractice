# Printing text from https://wolnelektury.pl/katalog/lektura/fraszki-ksiegi-wtore-na-lipe-gosciu-siadz-pod-mym-lisciem-a-.html
# & the next page (using requests & BeautifulSoup)

from requests import get
from bs4 import BeautifulSoup

url = "https://wolnelektury.pl/katalog/lektura/fraszki-ksiegi-wtore-na-lipe-gosciu-siadz-pod-mym-lisciem-a-.html"
r = get(url)
soup = BeautifulSoup(r.text, features="lxml")

print(soup.select("span.author")[0].get_text())
print(soup.select("span.title")[0].get_text())
for verse in soup.find_all("div", {"class": "verse"}):
	print(verse.get_text())

next_page_url = "https://wolnelektury.pl/" + soup.find("a")["href"]
r2 = get(next_page_url)
soup2 = BeautifulSoup(r2.text, features="lxml")

print(next_page_url)
# print(soup2.select("span.author")[0].get_text())
# print(soup2.select("span.title")[0].get_text())
# for verse in soup2.find_all("div", {"class": "verse"}):
# 	print(verse.get_text())