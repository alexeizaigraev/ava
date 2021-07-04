from papa_pg import *
#from modules_base import *
import os

os.system('python runsharp.py')
#os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
init()
verb = True
#verb = False

insert_all_terms()
insert_all_deps()
insert_all_otbor()
#select_terms()
#select_deps()


