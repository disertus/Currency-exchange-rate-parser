import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup


class CURRENCY:

    def __init__(self, url: str):
        self.open_url = urllib.request.urlopen(url).read()
        self.soup = BeautifulSoup(self.open_url, "html.parser")
        self.parsed_text = self.soup.get_text()

    def usd(self):
        value = re.findall(r"USD\d*\.\d*", self.parsed_text)
        return value

    def eur(self):
        value = re.findall(r"EUR\d*\.\d*", self.parsed_text)
        return value

    def rub(self):
        value = re.findall(r"RUB\d*\.\d*", self.parsed_text)
        return value

    def pln(self):
        value = re.findall(r"PLN\d*\.\d*", self.parsed_text)
        return value

    def currency(self, currency):
        count_currency = 0
        for i in currency:
            count_currency = count_currency + 1
            if count_currency == 1:
                print("\tПокупка: ", i, "\n")
            elif count_currency == 2:
                print("\tПродажа: ", i, "\n")


print( "-" * 50)

money = CURRENCY("https://finance.i.ua/", )
currency_usd = money.usd()
currency_eur = money.eur()
currency_rub = money.rub()
currency_pln = money.pln()

print(money.currency(currency_usd), money.currency(currency_eur),
      money.currency(currency_rub), money.currency(currency_pln))
