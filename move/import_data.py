from view import input_values_for_digits as inputD
from view import input_values_for_strings_for_names as inputN
from view import input_values_for_escape as esc

from data import append_numbers as a

def manual_input():
    check = False
    mainList = []
    while not check:
        listInput = []
        name = inputN('Введите имя: ')
        phone_number = inputD('Введите телефон без "+":','Error. Try again',79000000000,89999999999)
        listInput.append(name)
        listInput.append(phone_number)
        mainList.append(listInput)
        check = esc()
    return mainList

def start_import():
    a(manual_input())
