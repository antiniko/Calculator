from datetime import datetime as dt
from guid import dict_log


def get_log(res, oper, value_b, value_a):
    dtime = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}; первое значение: {}; операция: {}; второе значение: {}; результат: {}\n'
                     .format(dtime, value_a, oper, value_b, res))