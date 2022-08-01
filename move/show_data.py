from view import simple_print as sp

from data import read_all_numbers as rA


def all_numbers():
    string = rA()
    for i in range(len(string)):
        sp(string[i])

def show_numbers():
    all_numbers()