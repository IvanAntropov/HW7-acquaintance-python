from view import simple_print as sp
from view import input_values_for_digits as inputD

from move import import_data as imp
from move import export_data as exp
from move import show_data as shw

def start_programm():
    sp('Вас приветствует телефонный справочник!')
    choice = inputD('Выберите действие:\n1)Импортировать данные\n2)Экспортировать данные\n3)Показать данные справочника\nВвод: ','Error. Try again',1,3)
    match int(choice):
        case 1:
            imp.start_import()
        case 2:
            exp.start_export()
        case 3:
            shw.show_numbers()


