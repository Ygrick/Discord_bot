import requests
import pandas as pd
import re


import datetime, threading



def get_voltage():
    html = requests.get('https://www.alta.ru/currency/').text

    # нашли таблицы с валютами(основную и побочную), запарсили их
    # к себе, соединили и положили в переменную
    tables = pd.concat([pd.read_html(html)[7], pd.read_html(html)[6]],
                       ignore_index=True)

    # для простоты переименовываем столбцы на английские названия
    tables.columns = ['key', 'currency', 'rate']

    # разделяем ключи-цифры и ключи-имя валют (первый столбец)
    table_key = tables['key'].str.split(' ', expand=True)
    table_key.columns = ['number_key', 'name_key']

    # совмещаем разделённые столбцы с всей таблицей и удаляем столбец "повторюшку"
    tables = (pd.concat([table_key, tables], axis=1)).drop('key',
                                                           axis=1)

    # делаем табличку с наименованием валюты(где также лежит "цена за X ед." и её стоимостью (табл. 1)
    table_course = pd.concat([tables['currency'], tables['rate']],
                             axis=1)
    # взяли столбец с наименованием и разбили его на два(табл. 2):
    # столбец с именем и столбец "цена за Х ед."
    table_currency = table_course['currency']
    table_currency = table_currency.str.split('  ', expand=True)
    table_currency.columns = ['name_currency', 'multiplier']
    for n in range(149):
        table_currency['multiplier'][n] = int(''.join(re.findall('\d+',
                                                                 table_currency['multiplier'][n])))

    # объединили табл1 и табл2 удалив "повторюшку"
    table_course = (pd.concat([table_currency, table_course], axis=1)).drop('currency',
                                                                            axis=1)

    # в "цена валюты" сделали сумму за 1 ед. валюты

    table_course['rate'] /= table_course['multiplier']

    # убрали столбец "цена за Х ед." и сделали общую таблицу df
    table_course = table_course.drop('multiplier', axis=1)
    df = pd.concat([table_key, table_course], axis=1)
    return df



TABLE = get_voltage()

def update():

    TABLE = get_voltage()
    print('таблица обновлена', datetime.datetime.now())
    threading.Timer(30, update).start()


