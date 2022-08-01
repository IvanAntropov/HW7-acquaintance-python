
def simple_print(text: str):
    return print(text)

def input_values_for_digits(text1:str, text2:str,min: int,max: int) -> int:
    check = False
    while not check:
        try:
            number = input(f'{text1}')
            if min <= int(number) <= max:
                check = True
        except ValueError:
            print(f'{text2}')
    return number

def input_values_for_strings_with_check(text1:str, text2:str,listHelp:list) -> str:
    check = False
    while not check:
        number = input(f'{text1}')
        if number in listHelp:
            check = True
        else:
            print(f"{text2}")
    return number

def input_values_for_strings_for_names(text1:str) -> str:
    name = input(f'{text1}')
    return name

def input_values_for_escape(text = 'Для выхода пиши "escape": ', escape = 'escape') -> bool:
    string = input(text)
    if string == escape: return True
    else: return False
