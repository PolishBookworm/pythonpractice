# Quote guessing game, scrapes quotes from http://quotes.toscrape.com/ and
# asks user to guess the author

from requests import get
from bs4 import BeautifulSoup
from random import choice
from pyfiglet import figlet_format
from termcolor import colored


def welcome_screen():
    """printing welcome screen"""
    print(colored(figlet_format("Quote Guessing Game"), choice(
        ("red", "green", "yellow", "blue", "magenta", "cyan", "white"))))
    print("(Quotes scraped from: http://quotes.toscrape.com)\n")

# def scrape_quotes():
#     quotes = []
#     for n in range(11):
#         response = get(f"http://quotes.toscrape.com/page/{n}")
#         soup = BeautifulSoup(response.text, "html.parser")
#         for quote in soup.select("div.quote"):
#             quotes.append(quote)
#     return quotes


def scrape_quotes(url="http://quotes.toscrape.com"):
    quotes = []
    page_url = ""
    while True:
        response = get(f"{url}{page_url}")
        soup = BeautifulSoup(response.text, "html.parser")
        for quote in soup.select("div.quote"):
            quotes.append(quote)

        next_link = soup.find(class_="next").a["href"]
        if not hasattr(next_link, 'a'):
            break
        page_url = next_link.a["href"]
        print(page_url)
    return quotes


def info(quotes):
    quote_info = []
    for quote in quotes:
        text = quote.find("span").get_text()
        author = quote.select("span small")[0].get_text()
        url = quote.select("span a")[0]["href"]
        # author birth info
        res = get(f"http://quotes.toscrape.com/{url}")
        bs = BeautifulSoup(res.text, "html.parser")
        date = bs.select("span.author-born-date")[0].get_text()
        place = bs.select("span.author-born-location")[0].get_text()
        # author bio sample
        bio = bs.select("div.author-description")[0].get_text()[:500].replace(
            author, "$$$").replace(author.split(" ")[1], "$$$")
        # saving info to tuple, appending to list
        info = (text, author, url, f"{date} {place}", bio)
        quote_info.append(info)
    return quote_info


def guess(quote, guesses, hint=""):
    """asks for user input, returns correctness of guess"""
    print("\n")
    print(quote[0])
    print(hint)
    guess = input(f"Who do you think said this? ({guesses} guesses left) ")
    return guess == quote[1]


def game_logic(quote_info):
    play_again = "y"
    while play_again == "y":
        quote = choice(quote_info)
        if not guess(quote, 4):
            print("Incorrect!")
            if not guess(quote, 3, f"The author was born on {quote[3]}"):
                print("Incorrect yet again!")
                if not guess(
                        quote,
                        2,
                        f"This is a fragment of the author's bio ($$$ = author's name) {quote[4]}"):
                    print("Incorrect once more!")
                    if not guess(
                            quote,
                            1,
                            f"The first letter of the author's first name is: {quote[1][0]}"):
                        print("Incorrect once more!")
                        print(f"The correct answer is... {quote[1]}")
                    else:
                        print("Correct!")
                else:
                    print("Correct!")
            else:
                print("Correct!")
        else:
            print("Correct!")
        play_again = input("Do you want to play again? (y/n) ")

    print("Thanks for playing!")


def main():
    welcome_screen()
    quotes = info(scrape_quotes())
    game_logic(quotes)


if __name__ == "__main__":
    main()
