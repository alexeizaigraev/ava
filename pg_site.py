# -*- coding: utf-8 -*-
from module.modules import *
import os
import shutil
from colorama import Fore, Style, init
from papa_pg import *

def mk_regimes():
    return file_to_dict_one(COMON_DATA_PATH, 4)


init()
dir_in = IN_DATA_PATH
dir_out = OUT_DATA_PATH
fname_out = 'OutSite.csv'
fname_out_php = 'page-departments.php'


text1 = '''<?php
get_header();
?> 
<div class="container">
    <div class="row">
      <h1 class="title-normal"><strong>Відділення</strong></h1>
       <h5>Керівник відділень - начальник відділень Кульчицький Андрій Олегович, тел. +380 (44) 300 00 01 (137)</h5>
        <div class="form-group" style="margin-top:10px;">
            <input type="text" class="search-depart form-control" placeholder="Пошук">
        </div>
        <span class="counter"></span>
        <table class="table table-hover table-bordered results">
          <thead>
            <tr>
              <th class="col-md-1"><div style="text-align: center;">Найменування відокремленного підрозділу та ПНФП</div></th>
              <th class="col-md-4"><div style="text-align: center;">Адреса</div></th>
              <th><div style="text-align: center;">Дата та номер рішення про створення</div></th>
              <th class="col-md-1"><div style="text-align: center;">ЄДРПОУ</div></th>
              <th class="col-md-2"><div style="text-align: center;">Режим роботи</div></th>
              <th class="col-md-2"><div style="text-align: center;">Платежі приймаються в Платіжній системі</div></th>
              <th class="col-md-2"><div style="text-align: center;">Платежі виплачуються  в Платіжній системі</div></th>
            </tr>
            <tr class="warning no-result">
              <td colspan="7"><i class="fa fa-warning"></i> No result</td>
            </tr>
          </thead>
          <tbody>
'''

text2 = '''          </tbody>
        </table>
        <div class="gap-20"></div>
        <ul class="list-arrow">
            <li><a href="<?php echo $www?>/departments.pdf" target="_blank">Список усіх відділень</a></li>
        </ul>
        <div class="gap-20"></div>
    </div>
    
</div>

<?php
get_footer();
?> '''
        

regimes = mk_regimes()
natasha = set(mk_natasha())

site_old = file_to_text(OUT_DATA_PATH + 'OutSite.csv')
access = get_site_data()
    
header = ['Найменування відокремленного підрозділу та ПНФП',
        'Адреса',
        'Дата та номер рішення про створення',
        'ЄДРПОУ',
        'Режим роботи',
        'Платежі приймаються в Платіжній системі',
        'Платежі виплачуються  в Платіжній системі',]
    
out_text_php = ''
out_text_clear = ';'.join(header) + "\n"

for access_line in access:
    if len(access_line) < 4:
        continue
      
    regim_insert = 'не працює'
    ag_sign = access_line[0][0:3]
                  
    if ag_sign in regimes and access_line[0] in natasha:
        regim_insert = regimes[ag_sign]
    elif '1' == access_line[0]:
        regim_insert = 'ПН-ПТ 09:00-18:00'
          
    if access_line[1]:
        out_text_php += f'<tr><td>ВІДДІЛЕННЯ №{access_line[0]}</td><td>{access_line[2]}</td><td>{access_line[3]}</td><td>{access_line[1]}</td><td>{regim_insert}</td><td>ВПС ЕЛЕКТРУМ, ВПС FLASHPAY</td><td>ВПС ЕЛЕКТРУМ</td></tr>\n'
        out_text_clear += f'ВІДДІЛЕННЯ №{access_line[0]};{access_line[2]};{access_line[3]};{access_line[1]};{regim_insert};ВПС ЕЛЕКТРУМ, ВПС FLASHPAY;ВПС ЕЛЕКТРУМ\n'
    else:
        out_text_php += f'<tr><td>ПНФП ВІДДІЛЕННЯ №{access_line[0]}</td><td>{access_line[2]}</td><td>{access_line[3]}</td><td>{access_line[1]}</td><td>{regim_insert}</td><td>ВПС ЕЛЕКТРУМ, ВПС FLASHPAY</td><td>ВПС ЕЛЕКТРУМ</td></tr>\n'
        out_text_clear += f'ПНФП ВІДДІЛЕННЯ №{access_line[0]};{access_line[2]};{access_line[3]};{access_line[1]};{regim_insert};ВПС ЕЛЕКТРУМ, ВПС FLASHPAY;ВПС ЕЛЕКТРУМ\n'

full_out_fname = OUT_DATA_PATH + fname_out
text_to_file(out_text_clear, full_out_fname)
    
out_text_php = text1 + out_text_php + text2
full_out_fname_php = OUT_DATA_PATH + fname_out_php
text_to_file(out_text_php, full_out_fname_php)
    
if site_old == out_text_clear:
    p_green('\n\n\tno change\n')
