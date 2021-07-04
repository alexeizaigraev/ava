
import os
import sys
#import tech
from module.modules import *
from colorama import Fore, Style, init

def mk_menu(kv):
    #os.system('cls')
    print()
    init()
    my_keys = list(kv.keys())
    num = 0
    p_green('\n' + '_' * 75 + '\n')
    for point in kv:
        num += 1
        if num < len(kv):
            p_cyan(f'\t{num} {point}')
        else:
            p_green(f'\t{num} {point}')

    choice = '99'
    while choice != '0':
        print(f'{Fore.GREEN}\n\n -> ', end='')
        choice = input()
        if '' == choice:
            menu_main()
        elif 0 < int(choice) < len(my_keys) + 1:
            comand = 'python ' + kv[my_keys[int(choice)-1]] + '.py'
            os.system('cls')
            os.system(comand)
            mk_menu(kv)
        elif '0' == choice:
            sys.exit()
        else:
            print(f'{Fore.RED} >> wrong choice!')


def menu_main():
    os.system('cls')
    print('\n\n')
    menu = ['1 People',
            '2 Some',
            '3 Monitors',
            '4 Kabinet',
            '5 Base',
            '6 Zakr',
            '7 PostgresQL',]
    for point in menu:
        #print(f'{Fore.YELLOW} {point}', end = '  ')
        if point == menu[-1]:
            p_yellow(f'\t{point}')
        else:
            p_cyan(f'\t{point}')
        
    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input()
        
        if "1"  == choise:
            os.system('cls')
            menu_people()

        if "2"  == choise:
            os.system('cls')
            menu_some()

        if "3"  == choise:
            os.system('cls')
            menu_monitor()

        if "4"  == choise:
            os.system('cls')
            menu_kabinet()

        if "5"  == choise:
            os.system('cls')
            menu_base()
            
        if "6"  == choise:
            os.system('cls')
            menu_zakr()
        
        if "7"  == choise:
            os.system('cls')
            menu_pg()

        elif '0' == choise:
            sys.exit()
        else:
            p_red('\n\twrong choise!')

def menu_people():
    h_people = {'Priem': 'priem',
                'Otpusk': 'otpusk',
                'Perevod': 'perevod',
                'PostAll': 'postall',}
    mk_menu(h_people)
    
def menu_some():
    h_some = {'site': 'pg_site',
                'term': 'pg_term',
                'summury': 'pg_summury',
                'NatashaBig': 'natasha_big',
                'Kvadratiki': 'kvadratiki',
                'NatashaBig': 'natasha_big',}
    mk_menu(h_some)
    os.system('cls')

def menu_monitor():
    h_monitor = {'Monitor': 'monitor',
                'Accback': 'accback',
                'Walker': 'walker',}
    mk_menu(h_monitor)

def menu_kabinet():
    h_kabinet = {'Knigi': 'knigi',
                 'Rro': 'rro',
                 'Pereezd': 'pereezd',
                 'Otmena': 'otmena',
                 'OtmenaKnigi': 'otmena_knigi',}
    os.system('cls')
    mk_menu(h_kabinet)

def menu_base():
    h_base = {'add_otbor': 'add_otbor',
            'add_vsyo_zapros': 'add_vsyo_zapros',}
    os.system('cls')
    mk_menu(h_base)


def menu_zakr():
    h = {'get_rp': 'get_rp',
        'Kvadratiki': 'kvadratiki',}
    os.system('cls')
    mk_menu(h)


def menu_pg():
    h = {'refresh_all': 'refresh_all',
        'otbor': 'add_otbor',
        'otbor_hard': 'add_otbor_hard',}
    os.system('cls')
    mk_menu(h)


init()
menu_main()
