from colorama import *
import os
import re

# Версия v0.2.1

# Чтобы узнать все функции программы впишите в консоле 'A+ -func'

init()

print('A+ запустилась\n')

all_codes = []
user = ''
errors = 0

# Функция которая очищает консоль

def clear_console():
    os.system('cls||clear')

# Функция где программа определяет что ввёл пользователь

def go_command():
    if user_set_func == 'A+ -info':
        program_version()

    elif user_set_func == 'A+ -code edit':
        st_print()

    elif user_set_func == 'A+ -print':
    	st_print()

    elif user_set_func == '-print':
    	st_print()

    elif user_set_func == 'A+ -func':
        all_func()

    elif user_set_func == 'A+ -clear console':
        clear_console()
        set_command()

    else:
        print(Fore.RED + '\nОшибка: команда "' + user_set_func + '"\nне существует\n')
        set_command()


user_set_func = ''
res_input = ''

# Функция где пользователь пишет функцию

def set_command():
    global user_set_func
    user_set_func = input(Fore.YELLOW)
    print()
    go_command()

# Функция которая показывает информацию о А+

def program_version():
    print(Fore.WHITE + 'A+ version: 0.2.1\nAuthor: Almaz\n')
    set_command()

# Функция где описаны все функции А+

def all_func():
    print(
        Fore.WHITE + 'Все функции A+:\n\nA+ -info: вся информация о A+\nA+ -print: функция которая выводит текст который вы написали\n"print:" : выводит текст который вы написали\nA+ -res() или program -res(): перезапускает функцию\nA+ -exit() или program -exit(): выходит из функции\nA+ -func: выводит все функции A+\nA+ -clear console: полностью очищает консоль\n')
    set_command()

# Функция редактора кода

def st_print():
    
    # Старт написанного пользователем кода
    
    def code_start():
        global all_codes
        global errors
        clear_console()
        numbers_codes = 0
        for i in range(len(all_codes)):
            print(all_codes[numbers_codes])
            numbers_codes += 1


        all_codes = []
        print(Fore.WHITE + '\n\nProgram finished error code[' + str(errors) + ']')
        errors = 0
        comand_input()
        
        # Функция 'ошибка кода'
        
    def error_comand():
        global error_name
        print(Fore.RED + 'Ошибка: команда "' + error_name + '"\nне существует')
        
        # Функция где пользователь вводит функции после конца кода
        
    def comand_input():
        global res_input
        res_input = input(Fore.YELLOW)
        code_res_o()
        
        # Функция которая проверяет функцию который ввёл пользователь
        
    def code_res_o():
        if res_input == 'program -res()':
            clear_console()
            st_print()
        elif res_input == 'A+ -res()':
            clear_console()
            st_print()
        elif res_input == 'program -exit()':
            set_command()
        elif res_input == 'A+ -exit()':
            clear_console()
            set_command()
        else:
            print(Fore.RED + '\nОшибка: команда "' + res_input + '"\nне существует')
            comand_input()

    clear_console()
    print('function print has started\n')
    
    # Функция где пользователь пишет код
    
    def code_se():
        global all_codes

        user = input(Fore.GREEN)
        if user[0:6] == 'print:' and len(user) > 6:
        		all_codes.append(user[6:-1] + user[-1])

        elif user == 'start()':
        	code_start()

        elif user[0:8] == 's.print:' and len(user) >7:
        	set_nums = input(Fore.WHITE)
        	set_tx = user
        	all_codes.append((set_tx[8:-1] + set_tx[-1]) * int(set_nums))
        elif user == 'exit()':
        	clear_console()
        	all_codes = []
        	set_command()

        else:
            errors += 1

        code_se()

    code_se()


set_command()