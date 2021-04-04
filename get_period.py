import requests
import pandas as pd
from getRcode import getRcode
from matplotlib import pyplot as plt


# на вход с какого по какое число и Rcode валюты
# (example: get_period('01.03.2021', '01.04.2021', 'R01235'))
# на выходе dataFrame курса валюты
# (example: dataFrame "курс доллара за март")
def get_period(fromDate, toDate, Rcode):
    html = requests.get(f'https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ={Rcode}&UniDbQuery.From={fromDate}&UniDbQuery.To={toDate}').text
    table = ((pd.concat(pd.read_html(html), ignore_index = True)).drop(index=[0,1])).reset_index(drop=True)
    table.columns = ['date', 'multiplier', 'rate']
    table['rate'], table['multiplier'] = pd.to_numeric(table['rate'],downcast = "float"), pd.to_numeric(table['multiplier'])
    table['date'] = pd.to_datetime(table['date'],format="%d.%m.%Y")
    for n in range(table.shape[0]):
        table['rate'][n] /= table['multiplier'][n]*10000
    table = table.drop('multiplier', axis=1)
    table = table.iloc[::-1].reset_index(drop=True)
    return table

def get_image(curr, fromDate, toDate):
    # curr = curr[0].upper() + curr[1:].lower()
    Rcode = getRcode(curr)
    # return Rcode
    print(fromDate, toDate, Rcode)
    df = get_period(fromDate, toDate, Rcode)
    # import numpy as np


    x = df.date
    y = df.rate

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.xaxis_date()  # interpret the x-axis values as dates
    fig.autofmt_xdate()  # make space for and rotate the x-axis tick labels
    plt.fill(x, y, '#00a1e4', alpha=0.3)
    # plt.figure(figsize=(20, 20))
    # plt.show()

    fig.savefig('graf.jpg')
    return 'graf.jpg'