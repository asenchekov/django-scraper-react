from django.core.management.base import BaseCommand, CommandError
from backend.models import Item
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
  help = 'Run scraper to populate DB'
  
  def handle(self, *args, **kwargs):
    print('Starting scraping products from http://detence.bg/')
    count = 0
    main = requests.get('https://detence.bg/')
    main_soup = BeautifulSoup(main.content, 'html.parser')
    html = main_soup.find('ul', class_='category-sub-menu').find_all('li')

    for index in range(len(html)):
      category = html[index].find('a')['href']
      current_page = 1

      while True:
        print('\nCURRENT PAGE {}'.format(current_page))
        print('PRODUCTS COUNT:')
        page = requests.get('{}?page={}'.format(category, current_page))
        soup = BeautifulSoup(page.content, 'html.parser')
        products = soup.find_all('a', class_='thumbnail product-thumbnail')

        if len(products):
          for index in range(len(products)):
            count += 1
            # print('{}  '.format(count), end='\r')
            print(products[index]['href'])
            page = requests.get(products[index]['href'])
            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.find('h1', class_='h1').string)
            # print(soup.find('h1', class_='h1').parent.div.div.contents[0].split(' ')[2])
            # print(soup.find('div', class_='current-price').span['content'])
            p = soup.find('div', class_='product-description').find_all('p')
            desc = ''

            for para in p:
              if para.string:
                desc += para.string
            # print(desc)

            Item.objects.create(
              url = products[index]['href'],
              name = soup.find('h1', class_='h1').string,
              price = soup.find('div', class_='current-price').span['content'],
              sku = soup.find('h1', class_='h1').parent.div.div.contents[0].split(' ')[2],
              description = desc,
            )
          current_page += 1
        else:
          break
