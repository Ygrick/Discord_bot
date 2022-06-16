# from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn
import numpy
import requests
import pandas as pd
import datetime
from getRcode import getRcode
from get_period import get_period


def get_prediction(curr):
    today = datetime.datetime.today()
    tomorrow = (today + datetime.timedelta(days=1))
    df = get_period('01.01.2019', today, getRcode(curr))  # с 2016 по текущее с Rcode нужным
    new_row = {'date': [tomorrow], 'rate': [0]}
    new_df = pd.DataFrame(new_row)
    df = pd.concat([df, new_df])

    # разбиение даты на года\месяцы\недели
    df["weekday"] = df["date"].dt.weekday
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    df.drop(['date'], axis=1, inplace=True)

    # курсы за последние 7 дней (скроллинг\шифтинг)
    past_days = 7
    for day in range(past_days):
        d = day + 1
        df[f"curs_back_{d}d"] = df["rate"].shift(d)
    df.dropna(inplace=True)

    # бинарность столбцов по значениям
    df = pd.get_dummies(df, columns=["year", "month", "weekday"])

    # нужно создать последннюю строчку(как раз которую будем прогнозировать)
    # а именно входные данные
    new_df = df[-1:]
    df.drop(df.tail(1).index, inplace=True)
    #     print(df)
    # разметка на тестовые и тренировочные данные
    x = df.drop('rate', axis=1)
    y = df['rate']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    # обучение
    model = LinearRegression()
    model.fit(X_train, y_train)

    # метрика
    prediction = model.predict(X_test)
    #     print(mean_absolute_error(y_test, prediction))
    #     print(max_error(y_test, prediction))

    # предсказание
    return model.predict(new_df.drop('rate', axis=1))[0]



