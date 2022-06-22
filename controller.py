import view
import guid
import logger
import keyboard


def button_click():
    print ('для выхода из калькулятора нажмите: Esc','для продолжения вычеслений, Enter', sep='\n')
    if keyboard.read_key() == "esc":
        print ('конец')
        return 0
    while input() != '':
        print ('лучше нажать enter')
    # if keyboard.read_key() == "enter":
    value_a = view.get_value()
    oper = view.get_operator()
    value_b = view.get_value()
    func = guid.dict_ar[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)
    operation = guid.dict_log[oper]
    logger.get_log(result, operation, value_b, value_a)
    button_click() 
