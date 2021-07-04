# -*- coding: utf-8 -*-
from module.modules import *
import os
import shutil
from colorama import Fore, Style, init

def dir_in_walk():
    return file_to_arr(CONFIG_PATH + 'ConfigRaskladPath.txt')[0]

def dir_out_walk():
        return file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]
    
def show():
    a = os.listdir(dir_in_walk())
    for aa in a:
        p_blue(aa)
    if not a:
        p_cyan('\nnothing show\n')


def mk_agents():
    return file_to_dict_one(COMON_DATA_PATH, 3)

def mover():
    agents = mk_agents()
    a = os.listdir(dir_in_walk())
    if len(a) < 1:
            print(f'{Fore.RED}\n\tno files found\n')
    old_dir = dir_in_walk()
    for aa in a:
        fname = os.path.abspath(aa).split(os.sep)[-1]
        old_fname = os.path.join(old_dir, fname)
        folder = fname[:7]
        key = fname[:3]
        new_root = os.path.join(dir_out_walk(), agents[key])
        new_dir = os.path.join(new_root, folder)
        new_fname = os.path.join(new_dir, fname)
        backup_fname = 'R:/DRM/ЗАИГРАЕВ ОБМЕН АРХИВ/Архив/' + fname
        if not os.path.exists(new_dir):
            try:
                os.mkdir(new_dir)
                print(f'{Fore.BLUE}\tnew folder {new_dir}')
            except:
                print(f'{Fore.RED}>> err creat folder {new_dir}')
        try:
            shutil.copy(old_fname, backup_fname)
        except:
            pass
        
        try:
            shutil.move(old_fname, new_fname)
            print(f'{Fore.CYAN} Ok move {new_fname}')
        except:
                print(f'{Fore.RED}>> err move {new_fname}')
        
        
        
init()        
mover()

p_green('\n\n\nОстаток в rasklad:\n')
show()

