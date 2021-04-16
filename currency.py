from table import get_voltage
from table import TABLE


def get_cur(message):

    df_modified = TABLE.set_index('name_key')
    df_modified_number_key = TABLE.set_index('number_key')
    df_modified_name_currency = TABLE.set_index('name_currency')

    try:
        return str(df_modified.loc[message, 'rate']) + ' рублей'
    except KeyError:
        try:
            return str(df_modified_number_key.loc[message, 'rate']) + ' рублей'
        except KeyError:
            try:
                return str(df_modified_name_currency.loc[message, 'rate']) + ' рублей'
            except KeyError:
                return "Нет такой валюты"
