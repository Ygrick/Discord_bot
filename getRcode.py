import pandas as pd


# На вход имя валюты (example: 'Japanese Yen')
# На выходе Rcode валюты (example: 'R01820')
def getRcode(message):
    df = pd.read_csv('file1.csv', delimiter=',')
    df.drop('Unnamed: 0', axis=1)
    dfName = df.set_index('Name')
    dfEngName = df.set_index('EngName')
    try:
        return str(dfName.loc[message, 'Rcode'])[:6]
    except KeyError:
        try:
            return str(dfEngName.loc[message, 'Rcode'])[:6]
        except KeyError:
            return "Нет такой валюты"
