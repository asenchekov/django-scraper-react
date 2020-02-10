# Full Stack Developer task


## Make a Django application with PostgreSQL database for scraping data.
### The application should scrape the information for all of the products from https://detence.bg
### The data should be visualized in web interface in a table which should have the following columns:

### Website url | Name of product | Price | SKU | Description of the product

## Requirements:
1. The table should have a sorting options on all of the columns.
2. Python 3
3. Django 2.2
4. React.Js
5. SQLite 3


## Usage:

Install dependencies

```
$ pipenv install
$ pipenv shell
$ cd scraper_react
```

Migrate the database
```
$ python manage.py migrate
```

Start scraper
```
$ python manage.py scraper
```

Start server
```
$ python manage.py runserver
```
