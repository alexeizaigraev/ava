# -*- coding: utf-8 -*-
""" Набор модулей """
import os
import shutil
from pathlib import Path
import datetime
from colorama import Fore, Style, init

def sos(err, fact):
    """Сообщение об ошибке - запрос ввода - меню"""
    print('>> Err ', err, fact)
    input('## Press Any Key')
    input()
    os.system('python main.py')

def file_to_arr(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    for line in open(path, 'r', encoding="UTF-8"):
        if ";" in line:
            b.append(line.strip().split(";"))
        else:
            b.append(line.strip())
    return b

def file_to_vec(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    for line in open(path, 'r', encoding="UTF-8"):
        b.append(line.strip())
    return b

def file_to_dict_one(fname, num_col):
    h = dict()
    for line in open(fname, 'r', encoding="UTF-8"):
        split_line = line.strip().split(";")
        h[split_line[0]] = split_line[num_col]
    return h

def access_to_arr():
    b = []
    for line in open(IN_DATA_PATH + 'access.csv', 'r', encoding="UTF-8"):
        aa = line.strip().split(';')
        aa[0] = "ВІДДІЛЕННЯ №" + aa[0]
        b.append(aa)
    return b

def arr_to_text(arr):
    text = ''
    for v in arr:
        text += ';'.join(v) + "\n"
    return text

def file_to_text(fname):
    text = open(fname, 'r', encoding="UTF-8").read()
    return text

def text_to_file(b, fname):
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        p_magenta('clear ' + fname)
    else:
        p_blue(f'\n\t{fname}\n')

def text_add_file(b, fname):
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'a', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        p_magenta('clear ' + fname)
    else:
        p_blue(f'\n\t add to: {fname}\n')


def save_and_show(text, fname):
    text_to_file(text, fname)
    open_name = 'notepad.exe ' + fname
    os.system(open_name)


def arr_to_file(b, fname):
    """Записывает массив b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as out_object:
        for bb in b:
            out_object.write(";".join(bb) + "\n")
    p_blue(f'\n\t{fname}\n')
    
    
def text_to_file_cp1251(b, fname):
    """Записывает text b в файл с именем fname"""
    with open(fname, 'w', encoding="cp1251") as out_object:
        out_object.write(b)
    p_green(fname)

def now_date_kabinet():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}{m}{y}'

def now_date_log():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}.{m}.{y}'

def loger(kind):
    a = file_to_vec(IN_DATA_PATH + 'vsyo_zapros_vnesh_otbor.csv')[1:]
    text = ''
    for line in a:
        text += kind + ';' + now_date_log() + ';' + line + '\n'
    text_add_file(text, IN_DATA_PATH + 'loger.csv')

def mk_natasha():
    sign = 'Відділення № '
    b = []
    for line_str in open(IN_DATA_PATH + 'natasha.csv', 'r', encoding="UTF-8"):
        line = line_str.strip().split(';')
        for unit in line:
            if sign in unit:
                el = unit.replace(sign, '').strip()
                b.append(el)
    return b

def comon_data_dict(col_key_num):
    h = dict()
    for line in open(COMON_DATA_PATH, 'r', encoding="UTF-8"):
        vec = line.split(';')
        key = vec[0]
        dat = vec[col_key_num]
        h[key] = dat
    return h

def dir_kabinet(self):
        return file_to_arr(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]


def mover(old_name, new_name):
        
    try:
        shutil.move(old_name, new_name)
        p_blue(new_name)
    except:
        p_red('>> err', old_name)

def coper(old_name, new_name):
    try:
        shutil.copy(old_name, new_name)
        p_blue(new_name)
    except:
        p_red('>> err', old_name)


def p_red(text):
    init()
    print(Fore.RED + text)
def p_green(text):
    init()
    print(Fore.GREEN + text)
def p_yellow(text):
    init()
    print(Fore.YELLOW + text)
def p_cyan(text):
    init()
    print(Fore.CYAN + text)
def p_magenta(text):
    init()
    print(Fore.MAGENTA + text)
def p_blue(text):
    init()
    print(Fore.LIGHTBLUE_EX + text)


                      
    

DATA_PATH = file_to_arr('Config/ConfigDataPath.txt')[0]
IN_DATA_PATH = DATA_PATH + 'InData/'
OUT_DATA_PATH = DATA_PATH + 'OutData/'
CONFIG_PATH = DATA_PATH + 'Config/'
COMON_DATA_PATH = CONFIG_PATH + 'comon_data.csv'
CONFIG_DIR_PATH = DATA_PATH + 'ConfigDir/'
KABINET_DIR = file_to_arr(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]

GDRIVE_PATH = file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]