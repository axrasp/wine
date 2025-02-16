import argparse
import collections
import datetime
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    load_dotenv()
    catalog_path = os.getenv('CATALOG_PATH')
    foundation_year = int(os.getenv('COMPANY_FOUNDATION_YEAR'))

    parser = argparse.ArgumentParser(
        description='Сайт магазина авторского вина "Новое русское вино"'
    )
    parser.add_argument('-c', '--catalog', default='catalog/catalog.xlsx', help='Укажите путь к каталогу (вместе с названием файла)')
    args = parser.parse_args()
    if args.catalog:
        catalog_path = args.catalog

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    products = pandas.read_excel(catalog_path, sheet_name='Лист1', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values='None', keep_default_na=False).to_dict(orient='record')
    grouped_products = collections.defaultdict(list)
    for product in products:
        grouped_products[product['Категория']].append(product)

    rendered_page = template.render(
        products_grouped=grouped_products.items(),
        company_age=datetime.datetime.now().year-foundation_year
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
