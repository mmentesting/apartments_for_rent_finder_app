import requests
from bs4 import BeautifulSoup

class ZillowData:
    def __init__(self):
        self.city_heading = ""
        self.addresses = []
        self.links = []
        self.prices = []

    def make_soup(self, url, head):
        response = requests.get(url=url, headers=head)
        # print(response)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        self.city_heading = soup.select_one("#grid-search-results h1").getText()
        rentals_elements = soup.select(".property-card-data a")
        self.addresses = [address.getText().split(" | ")[-1] for address in rentals_elements]
        for tag in rentals_elements:
            link = tag.get("href")
            if not link.startswith("http"):
                link = f"https://www.zillow.com{link}"
            self.links.append(link)
        price_elements = soup.select(".property-card-data span[data-test='property-card-price']")
        self.prices = [price.getText()[:6] for price in price_elements]
