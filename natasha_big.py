# -*- coding: utf-8 -*-
from module.modules import *
from papa import *
from papa_pg import *
from datetime import datetime, date

def count_comon(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha:
            count += 1
    return(count)

def count_edrpou(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha and line[1]:
            count += 1
    return(count)

def count_pnfp(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha and not line[1]:
            count += 1
    return(count)



natasha = set(mk_natasha())
access_data = get_natasha_data()

partner_dict = dict()
for line in access_data:
    partner_dict[ line[-1] ] = line[0][:4]

partner_list = sorted( partner_dict.keys() )
header = 'Партнёр;Отделения с ЕДРПОУ;ПНФП;Всего'
out_text = header + '\n'
#print('\n\n' + header)
summ_comon = 0
summ_edrpou = 0
summ_pnfp = 0
for partner in partner_list:
    if partner and partner != 'intime' and count_comon(partner) > 0:
        out_line = f'{partner};{count_edrpou(partner)};{count_pnfp(partner)};{count_comon(partner)}'
        #print(out_line)
        out_text += out_line + '\n'
        summ_comon += count_comon(partner)
        summ_edrpou += count_edrpou(partner)
        summ_pnfp += count_pnfp(partner)

print()
out_text += '\n'
#print(out_text)

#print('Всего с ЕДРПОУ', summ_edrpou)
out_text += f'Всего с ЕДРПОУ {summ_edrpou}\n'
#print('Всего ПНФП', summ_pnfp)
out_text += f'Всего ПНФП {summ_pnfp}\n'
#print('Всего', summ_comon)
out_text += f'Всего {summ_comon}\n'

p_green('\n\n' + out_text)

now = str(datetime.today())[:10]
ofname = DATA_PATH + f'Количество отделений/Отделения-{now}.csv'
p_yellow('\n\t save?\t\t yes [Enter] ->')
choise = input()
if not choise:
    text_to_file(out_text, ofname)
else:
    p_blue('\tDu-Du :)')
     
        
