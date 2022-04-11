# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```

## Запуск
Создайте файл ``.env`` и добавьте в него дату основания компании
Запустите сайт командой `python3 main.py`
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

```python
COMPANY_FOUNDATION_YEAR=1920
```

## Изменения каталога
Каталог товаров хранится в файле ``wine3.xlsx``, вы можете изменить/добавить товары через него или использовать другой файл по шаблону ``wine3.xlsx``.

**Не изменяйте названия колонок и их количество!**

Для изменения пути к нему, добавьте переменную в файл ``.env`` и добавьте в него путь к файлу с каталогом (по дефолту файл с каталогом хранится ``images/wine3.xlsx``)
```python
CATALOG_PATH='catalog/wine3.xlsx'
```
Либо вы можете запустить код с параметром ``-c`` ``-catalog``:
```
python3 main.py -c new_directory/newfile.xlxs
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

## Лицензия

Код распространяется свободно согласно MIT License