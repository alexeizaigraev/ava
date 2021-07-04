# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from module.modules import *
#from papa import *
import papa
from colorama import Fore, Style, init

in_files = file_to_arr(CONFIG_DIR_PATH + 'PathBackUpAccessDirList.txt')

out_dir_list = file_to_arr(CONFIG_DIR_PATH + 'PathBackUpAccessOut.txt')
        
init()
for out_dir in out_dir_list:
    for in_dir in in_files:
        for old_fname in os.listdir(in_dir):
            if '.accdb' in old_fname:
                old_fname_full = in_dir + old_fname
                for out_dir in out_dir_list:
                    
                    new_fname_full = out_dir + old_fname
                    coper(old_fname_full, new_fname_full)
