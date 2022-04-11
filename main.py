import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
products = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values='None', keep_default_na=False).to_dict(orient='record')
products_grouped = collections.defaultdict(list)
for product in products:
    products_grouped[product['Категория']].append(product)

rendered_page = template.render(
    products_grouped=products_grouped.items(),
    company_age=datetime.datetime.now().year-1920
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
