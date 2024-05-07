#scraping stock prices
import requests
from bs4 import BeautifulSoup
def data(symbol1, symbol2):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    url = f'https://stocks.zerodha.com/{symbol1}/{symbol2}'

    r = requests.get(url, headers = header)
    soup = BeautifulSoup(r.text, 'html.parser')
    stockinfo = {
    'price' : soup.find('div', {'class' : 'jsx-2945882850 quote-box-root with-children'}).findAll('span')[0].text, 
    'change' : soup.find('div', {'class' : 'jsx-2945882850 quote-box-root with-children'}).findAll('span')[1].text,
    } 
    # the above program finds the div functions and uses indexing to find the contents in the 'span' attribute
    return stockinfo
symbol1 = input("Enter the either INDICES OR STOCKS: ")
symbol2 = input("Enter the preferred index or stock: ")
print(f"Stock data: {data(symbol1, symbol2)}")
'''
     price = soup.find('span', {'class' : 'jsx-2945882850 current-price text-dark text-24'}).text
     change = soup.find('span', {'class' : 'jsx-2945882850 change absolute-value text-14 font-medium down'}).text
     changepercent = soup.find('span', {'class' : 'jsx-2945882850 change percentage-value text-14 down'}).text
'''
    # you can use the above lines to find the data as well but instead you can use the div function of the overall class as it is the common term between all the stock information. the above code has variables such as colour(green or red) with different stocks.
