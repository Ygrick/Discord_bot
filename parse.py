def get_voltage():
    from pandas import read_html as pdrd
    from pandas import concat as pdcn
    from re import findall as refa
    from requests import get as rqget

    #####################################################
    # Я конечно не эксперт, но этот код явно "НЕ ОЧЕНЬ" #
    #####################################################
    #          (Это Игорь писал, я тут ни при чем!)

    html = rqget('https://www.alta.ru/currency/').text

    tables = pdrd(html)[7]

    tables.columns = ['key', 'currency', 'rate']

    table_key = tables['key'].str.split(' ', expand=True)
    table_key.columns = ['number_key', 'name_key']

    tables = (pdcn([table_key, tables], axis=1)).drop('key',
                                                           axis=1)

    table_course = pdcn([tables['currency'], tables['rate']],
                             axis=1)

    table_currency = table_course['currency']
    table_currency = table_currency.str.split('  ', expand=True)
    table_currency.columns = ['name_currency', 'multiplier']
    for n in range(115):
        table_currency['multiplier'][n] = int(''.join(refa('\d+', table_currency['multiplier'][
            n])))

    table_course = (pdcn([table_currency, table_course], axis=1)).drop('currency',
                                                                            axis=1)

    for n in range(115):
        table_course['rate'][n] /= table_course['multiplier'][n]

    table_course = table_course.drop('multiplier', axis=1)
    df1 = pdcn([table_key, table_course], axis=1)

    # html = rqget('https://www.alta.ru/currency/').text

    tables = pdrd(html)[7]

    tables.columns = ['key', 'currency', 'rate']

    table_key = tables['key'].str.split(' ', expand=True)  #
    table_key.columns = ['number_key', 'name_key']

    tables = (pdcn([table_key, tables], axis=1)).drop('key',
                                                           axis=1)

    table_course = pdcn([tables['currency'], tables['rate']],
                             axis=1)

    table_currency = table_course['currency']
    table_currency = table_currency.str.split('  ', expand=True)
    table_currency.columns = ['name_currency', 'multiplier']
    for n in range(33):
        table_currency['multiplier'][n] = int(''.join(refa('\d+', table_currency['multiplier'][
            n])))

    table_course = (pdcn([table_currency, table_course], axis=1)).drop('currency',
                                                                            axis=1)

    for n in range(33):
        table_course['rate'][n] /= table_course['multiplier'][n]

    table_course = table_course.drop('multiplier', axis=1)
    df2 = pdcn([table_key, table_course], axis=1)
    df3 = pdcn([df1, df2], axis=0)
    return df3