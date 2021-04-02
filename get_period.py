import requests
import pandas as pd


def get_period(fromDate, toDate, Rcode):
    html = requests.get(f'https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ={Rcode}&UniDbQuery.From={fromDate}&UniDbQuery.To={toDate}').text
    table = ((pd.concat(pd.read_html(html), ignore_index = True)).drop(index=[0,1])).reset_index(drop=True)
    table.columns = ['date', 'multiplier', 'rate']
    table['rate'], table['multiplier'] = pd.to_numeric(table['rate'],downcast = "float"), pd.to_numeric(table['multiplier'])
    table['date'] = pd.to_datetime(table['date'])
    for n in range(table.shape[0]):
        table['rate'][n] /= table['multiplier'][n]*10000
    table = table.drop('multiplier', axis=1)
    return table