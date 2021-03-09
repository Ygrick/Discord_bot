from parse import get_voltage


def get_cur(cur):
    if str(cur).isdigit():
        return get_cur_by_number(int(cur))
    else:
        return get_cur_by_letter(cur.upper())


def get_cur_by_letter(cur):
    df = get_voltage()
    ser = df[df['name_key']==cur].drop_duplicates()
    if ser is not None:
        val = list(ser['rate'])[0]
        name = list(ser['name_currency'])[0]
        return (f'{round(val,3)} р. за 1 {name}')
    else:
        return 'информация отсутствует'


def get_cur_by_number(cur):
    df = get_voltage()
    ser = df[df['number_key']==cur].drop_duplicates()
    if ser is not None:
        val = list(ser['rate'])[0]
        name = list(ser['name_currency'])[0]
        return (f'{round(val, 3)} р. за 1 {name}')
    else:
        return 'информация отсутствует'


def get_cur_by_keyword():
    pass
    # я уже жалею, что всё это затеял