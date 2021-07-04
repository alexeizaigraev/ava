from module.modules import *
from random import randint
import os
import shutil
from colorama import Fore, Style, init


def mk_fio():
    fio_split = work_vec[ColFioOne].replace('  ', ' ' ).strip().split(' ')
    
    if len(fio_split) < 3:
        return fio_split[0] + ' ' \
            + fio_split[1] + ' ' \
            + fio_split[1]
    return ' '.join(fio_split)

def mk_surname():
    return mk_fio().split(' ')[0]

def mk_firstname():
    return mk_fio().split(' ')[1]

def mk_lastname():
    return mk_fio().split(' ')[2]

def mk_initial_one_dot():
    return mk_firstname()[0] + '.'

def mk_initial_two_dot():
    return mk_lastname()[0] + '.'

def mk_dep():
    if '№' in work_vec[ColDepOne]:
        return work_vec[ColDepOne].split('№')[-1].strip()
    return work_vec[ColDepOne].strip()

def mk_fio_white(fff):
    fs = fff.replace('  ', ' ').strip().split(' ')
    surn = fs[0]
    out = surn
    other = ''.join(fs[1:]).replace('.', '').replace(' ', '')
    for leter in other:
        if leter.isupper() and leter.isalpha():
            out += leter
    return out

def dep_clear(deps):
    out = []
    d = deps.replace('[', '').replace(']', '').replace(' ', '').strip()
    if ',' not in d:
        out.append(d[:7])
    else:
        dd = d.split(',')
        for ddd in dd:
            out.append(ddd[:7])
    return out

def mk_kass_all_hash():
    out_hash = dict()
    #kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
    #kass[:] = [line for line in kass if len(line) > 4 and 'true' in line[1]]
    a = []
    #kass = file.open(IN_DATA_PATH + 'kass_all.csv')
    for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
        line = line_str.split(';')
        if len(line) > 4 \
            and 'true' in line[1]:
            try:
                fio_white = mk_fio_white(line[2] )
                login = line[0]
                deps = dep_clear(line[3])
                for dep in deps:
                    key = fio_white + dep
                    if key not in out_hash:
                        out_hash[key] = []
                    out_hash[key].append(login)
                    

                #v = [line[ColLoginTwo], fio_white, line[ColDepTwo]]
                #a.append(v)
            except:
                print(f'>> err kass_all: {line[2]}')
    return out_hash



def mk_kass_all():
    a = []
    for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
        line = line_str.split(';')
        try:
            fio_white = mk_fio_white(line[2] )
            v = [line[0], fio_white, line[3]]
            a.append(v)
        except:
            print(f'>> err kass_all: {line[2]}')
    return a
          
def login_hash_deep():
    logins = []
    parDep = mk_dep()[:3]
    fio = mk_fio_white(mk_fio())
    login_ok = False
    key = fio + parDep
    key_list = list(kass_all_hash.keys())
    for el in key_list:
        if key in el:
            logins.append(kass_all_hash[el])
            login_ok = True
    if login_ok and ( 1 == len(logins) ):
        return logins[0]
    else:
        return ''

def login_hash():
    login = ''
    parDep = mk_dep()
    fio = mk_fio_white(mk_fio())
    login_ok = False
    key = fio + parDep
    try:
        login = kass_all_hash[key]
    except:
        pass
    if login:
        return login

    return login_hash_deep()




def login_deep(nama, parDep):
    logins = [line[0] for line in kass_all
        if ( (parDep in line[2][1:4])
            and (nama in line[1]) ) ]
    
    if logins and ( 1 == len(logins) ):
        login_ok = True

    return logins


def login():
    parDep = mk_dep()
    login_ok = False
    nama = mk_fio_white(mk_fio())

    logins = [line[0] for line in kass_all
        if ( (parDep in line[2])
            and (nama in line[1]) ) ]
    
    if logins:
        login_ok = True
        return logins

    return login_deep(nama, parDep[:3])


def dir_kabinet():
    return file_to_arr(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]

def text_to_file_cp1251(b, fname):
    """Записывает text b в файл с именем fname"""
    with open(fname, 'w', encoding="cp1251") as out_object:
        out_object.write(b)
    print(fname)

def mover(old_name, new_name):
    init()
    try:
        shutil.move(old_name, new_name)
        p_blue(new_name)
    except:
        p_red(old_name)

def coper(old_name, new_name):
    try:
        shutil.copy(old_name, new_name)
        p_blue(new_name)
    except:
        p_red(old_name)

