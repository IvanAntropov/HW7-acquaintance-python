from view import input_values_for_strings_with_check as inputSC

def choice_format():
    return inputSC('Выберите расширение файла .txt .xls .word: ','Try again',['.txt','.xls','.word'])

def append_numbers(numbers: list):
    format_of_file = choice_format()
    string =''
    for i in range(len(numbers)):
        string+= str(numbers[i][0]) + ';' + str(numbers[i][1]) + ';\n'
    path = 'Phone_books/phone_book' + format_of_file 
    with open(path, 'a') as fa:
        fa.write(string)

def read_all_numbers():
    mainList = []
    for i in range(1,4):
        match i:
            case 1:
                format_of_file = '.txt'
            case 2:
                format_of_file = '.word'
            case 3:
                format_of_file = '.xls'
        path = 'Phone_books/phone_book' + format_of_file
        with open(path, 'r') as fa:
            numbers = fa.read().split(';')
            mainList.append(numbers)
    return mainList
