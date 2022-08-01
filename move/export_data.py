from view import input_values_for_strings_for_names as inputN

from data import read_all_numbers as rA

def export_to_file():
    listOfNumbers = rA
    path = inputN('Укажи путь: ')
    string =''
    for i in range(len(listOfNumbers)):
        string+= str(listOfNumbers[i][0]) + ';' + str(listOfNumbers[i][1]) + ';\n'
    with open(path, 'a') as fa:
        fa.write(string)

# def export_somewere():

def start_export():
    export_to_file()

    # choice = inputD('Как?\n1)Конкретный путь\n2)Куда-нибудь еще\nВвод: ','Error. Try again',1,2)
    # match int(choice):
    #     case 1:
    #         a(manual_input())
    #     case 2:
    #         a(numbers_from_file())