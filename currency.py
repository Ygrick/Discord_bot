from table import get_voltage


def get_cur(messege):
    df_modified = get_voltage().set_index('name_key')
    df_modified_number_key = get_voltage().set_index('number_key')
    df_modified_name_currency = get_voltage().set_index('name_currency')

    try:
        return str(df_modified.loc[messege, 'rate']) + ' рублей'
    except KeyError:
        try:
            return str(df_modified_number_key.loc[messege, 'rate']) + ' рублей'
        except KeyError:
            try:
                return str(df_modified_name_currency.loc[messege, 'rate']) + ' рублей'
            except KeyError:
                return "Нет такой валюты"
