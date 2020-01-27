from django.core.management.base import BaseCommand, CommandError
from backend.models import Item
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
  help = 'Run scraper to populate DB'
  
  def scrape_item(self, link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find('div', class_='product-description').find_all('p')
    desc = ''

    for para in p:
      if para.string:
        desc += para.string

    Item.objects.create(
      url = link,
      name = soup.find('h1', class_='h1').string,
      price = soup.find('div', class_='current-price').span['content'],
      sku = soup.find('h1', class_='h1').parent.div.div.contents[0].split(' ')[2],
      description = desc,
    )
  
  def handle(self, *args, **kwargs):
    print('Starting scraping products from http://detence.bg/')
    count = 0
    main = requests.get('https://detence.bg/')
    main_soup = BeautifulSoup(main.content, 'html.parser')
    category_list = main_soup.find('ul', class_='category-sub-menu').find_all('li')

    for index in range(len(category_list)):
      category = category_list[index].find('a')['href']
      current_page = 1

      while True:
        print('\nCURRENT PAGE {}'.format(current_page))
        print('PRODUCTS COUNT:')
        item_page = requests.get('{}?page={}'.format(category, current_page))
        soup = BeautifulSoup(item_page.content, 'html.parser')
        products = soup.find_all('a', class_='thumbnail product-thumbnail')

        if len(products):
          for index in range(len(products)):
            count += 1
            print('{}  '.format(count), end='\r')
            self.scrape_item(products[index]['href'])

          current_page += 1

        else:
          break
