# -*- coding: utf-8 -*-
from module.modules import *
from papa import *
from datetime import datetime, date


names0 = {'1010' : 'delivery',
        '1060' : 'intime',
        '1100' : 'mandarin',
        '1330' : 'justin',
        '1410' : 'lukso',
        '1670' : 'parfums',
        '1700' : 'sat',
        '1890' : 'allo',
        '1990' : 'test'
        }

names = comon_data_dict(1)
        
fname_out = 'OutNatasha.csv'
out_text = ''
#data = set(file_to_arr(IN_DATA_PATH + 'natasha.csv'))
data = set(mk_natasha())
h = dict()
for line in data:
    key = line[:3]
    if key in h:
        h[key] += 1
    else:
        h[key] = 1
    
sum = 0
for key in sorted(list(h.keys())):
    sum += h[key]
    name = '_'
    if key in names:
        name = names[key]
            
    out_text += key + ';' + name + ';' + str(h[key]) + '\n'

out_text += '__________\n'
out_text += 'Всего: ' + str(sum)
        
full_out_fname = OUT_DATA_PATH + fname_out
text_to_file(out_text, full_out_fname)
p_green('\n\n' + out_text)

now = str(datetime.today())[:10]
ofname = DATA_PATH + f'Количество отделений/Отделения-{now}.csv'
p_yellow('\n\t save?\t\t yes [Enter] ->')
choise = input()
if not choise:
    text_to_file(out_text, ofname)
else:
    p_blue('\tDu-Du :)')
