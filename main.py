import datetime
import pandas
import collections

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
wines = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values='None', keep_default_na=False).to_dict(orient='record')
wine_catalog = collections.defaultdict(list)
for wine in wines:
    wine_catalog[wine['Категория']].append(wine)

rendered_page = template.render(
    wine_catalog=wine_catalog.items(),
    company_age=datetime.datetime.now().year-1920
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
