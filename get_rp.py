# -*- coding: utf-8 -*-
from module.modules import *
import os
import shutil
from papa_pg import get_otbor_deps
from colorama import Fore, Style, init

def ag_folders():
    outlist = []
    for folder in comon_data_dict(3).values():
        if folder != 'nodata':
            outlist.append(folder)
    return outlist

def col_key_pg(vec):
    os.system('cls')
    listkey = vec
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]

def get_all_fnames():
    out = []
    folders = os.listdir(GDRIVE_PATH + ag_folder)
    for folder in folders:
        try:
            work_dir = GDRIVE_PATH + ag_folder + '/' + folder
            fnames = os.listdir(work_dir)
            for fname in fnames:
                if '_RP_' not in fname:
                    continue
                
                for dep in otbor:
                    if dep in fname:
                        fname_full = work_dir + '/' + fname
                        out.append(fname_full)
                        #print(fname_full)
        except:
            pass
        
    return out


def short_name(name):
    return name.split('/')[-1]


init()
out_path = 'R:/DRM/Access/ЗАКРЫТИЕ/RP/'

old = os.listdir(out_path)
for fname in old:
    try:
        os.remove(out_path + fname)
    except:
        print('err remove', fname)

#otbor = file_to_arr('R:/DRM/Access/ЗАКРЫТИЕ/otbor.csv')
otbor = get_otbor_deps()

print('\nread otbor', 'R:/DRM/Access/ЗАКРЫТИЕ/otbor.csv', '\n')


ag_folder = col_key_pg(ag_folders())
print(f'\n{ag_folder}\n')

a = get_all_fnames()
for aa in a:
    old_name = aa
    new_name = out_path + short_name(aa)
    coper(old_name, new_name)

