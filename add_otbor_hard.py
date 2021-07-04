from module.modules import *
from module.modules_base import *
from colorama import Fore, Style, init
from papa_pg import *

init()
head = 'term;dep\n'
out = head

all_term = get_terminals_list()
print(all_term)
print('*')

print(f'{Fore.CYAN} Terminals:\n')
choise = input(' -> ')


terms = []
if ' ' in choise:
    terms = choise.split(' ')
else:
    terms[0] = choise

for term in terms:
    if term not in all_term:
        p_red(term)
    dep = term[:7]
    out += term + ';' + dep + '\n'

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')
mk_vsyo_zapros()

insert_all_otbor()


