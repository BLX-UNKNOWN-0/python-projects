# BLX-UNKNOWN-0
# PROJECT 11 // WEB SCRAPER

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    print("\n--- Scraping quotes from the web ---")
    url = "http://quotes.toscrape.com"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for i, quote in enumerate(quotes, 1):
        text   = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"\n{i}. {text}")
        print(f"   — {author}")

def scrape_news():
    print("\n--- Scraping headlines ---")
    url = "https://news.ycombinator.com"
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("span", class_="titleline")

    for i, title in enumerate(titles[:10], 1):
        print(f"{i}. {title.text}")

def menu():
    print("...WEB SCRAPER...")

    while True:
        print("\n 1=Scrape Quotes  2=Scrape News  0=Quit")
        choice = input("Choose: ").strip()

        if   choice == "1": scrape_quotes()
        elif choice == "2": scrape_news()
        elif choice == "0": print("Bye!Have a good day"); break
        else: print("Invalid choice.")

menu()