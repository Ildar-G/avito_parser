import requests
from bs4 import BeautifulSoup
import csv

#TODO
'''
1. Определить количество страниц
2. Список url
3. Собрать данные
'''

url = 'https://www.avito.ru/sankt-peterburg?p=2&q=htc'
#https://www.avito.ru/sankt-peterburg/bytovaya_elektronika?p=1&q=htc
#https://www.avito.ru/sankt-peterburg/noutbuki?p=3&q=%D1%83%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D0%B1%D1%83%D0%BA


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    #test_pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1]

    total_pages = pages.split('=')[1].split('&')[0]

    #print(pages)
    #print(total_pages)

    return int(total_pages)
    #print(test_pages)


def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('data_8.csv', 'a') as f:
        writer = csv.writer(f, delimiter = ';')

        writer.writerow((data['title'],
                        data['url'],
                        data['price'],
                        data['metro']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    #print(ads)
    #print(type(ads))
    for ad in ads:

        #title price metro
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
            #print(title)
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
            #print(url)
        except:
            url = ''

        try:
            price_text = ad.find('div', class_='description').find(class_='price').text.strip()
            price = price_text.replace('₽',  '')


        except:
            price = ''

        try:
            metro = ad.find('div', class_='data').find_all('p')[-1].text
            #print(metro)
        except:
            metro = ''

        data = {'title':title,
                'url':url,
                'price':price,
                'metro':metro}
        #print(data)
        write_csv(data)






def main():
    url = 'https://www.avito.ru/sankt-peterburg/noutbuki?p=3&q=%D1%83%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D0%B1%D1%83%D0%BA'

    base_url = 'https://www.avito.ru/sankt-peterburg/noutbuki?'
    page_part = 'p='
    query_part = '&q=%D1%83%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D0%B1%D1%83%D0%BA'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)
        #print(data)



if __name__ == '__main__':
    main()

