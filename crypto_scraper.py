# Importing all the required modules
from bs4 import BeautifulSoup
import requests
import openpyxl

# Creating a new excel file
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Crypto Currencies'
sheet.append(['Rankings', 'Name', 'Shortform', 'Price', '24H Change', '24H Volume', 'MarketCap'])

# To overcome the anti-bot detection of crypto.com website
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

try:
    url = "https://crypto.com/price"

    def scrape_crypto_names(page_url):
        source = requests.get(page_url, headers=HEADERS)
        source.raise_for_status()  # Raise an error if there is an issue with the URL
        soup = BeautifulSoup(source.text, 'html.parser')

        cryptos = soup.find('tbody', class_='css-0').find_all('tr', class_="css-1cxc880")

        for i in cryptos:
            # Scraping all the required data
            ranking = i.find('td', class_="css-w6jew4").text
            name = i.find('td', class_="css-1sem0fc").find('div', class_="css-87yt5a").p.text
            shortform = i.find('td', class_="css-1sem0fc").find('div', class_="css-87yt5a").span.text
            price = i.find('td', class_="css-1m7ejhk").find('div', class_="css-16q9pr7").find("p",
                                                                                            class_="chakra-text css-5a8n3t").text
            Volume24hr = (i.find_all('td', class_="css-15lyn3l"))[0].text
            MarketCap = (i.find_all('td', class_="css-15lyn3l"))[1].text
            pricechange = i.find('td', class_="css-vtw5vj").text
            sheet.append([ranking, name, shortform, price, pricechange, Volume24hr, MarketCap])
        return sheet

    def scrape_all_crypto_names(url, page_numbers=3):
        for i in range(1, page_numbers + 1):
            base_url = url + f"?page={i}"
            extendednames = scrape_crypto_names(base_url)
        return True

    scrape_all_crypto_names(url, 3)  # Change the number according to your necessity and convenience

except Exception as e:
    print(e)

excel.save("TopCryptos.xlsx")
