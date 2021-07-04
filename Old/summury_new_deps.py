from modules import *
from modules_base import *

my_key = 'partner'

head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Область;Район в обл.;Індекс;Тип населеного пункту;Населений пункт;Район в місті;Тип вулиці;Адреса;Номер будинку;Дата признчення керівника;модель РРО;Заводський № РРО;2\n'
out_text = head
hh = file_to_hash(IN_DATA_PATH + 'vsyo_zapros.csv', 1)

partner = col_key(hh, my_key)
print(f'\n\n\t{partner}\n\n')

my_deps = []
count = 0
for key in hh:
    try:
        line = hh[key]
        if partner in line[my_key]:
            dep = line['Терминалы.department']
            if dep in my_deps or '1700999' in dep:
                continue
            my_deps.append(dep)
            count += 1
            out_line = (str(count) + ';' 
                        + line['Терминалы.department']  + ';'
                        + line['region'] + ';'
                        + line['district_region'] + ';'
                        + line['post_index'] + ';'
                        + line['city_type'] + ';'
                        + line['city'] + ';'
                        + line['district_city'] + ';'
                        + line['street_type'] + ';'
                        + line['street'] + ';'
                        + line['hous'] + ';'
                        + '' + ';'
                        + '' + ';'
                        + '' + ';'
                        + line['address'])
            out_text += out_line + '\n'
            out_line = (str(count) + ';' + line.keys() + "123")
    except:
        pass

text_to_file(out_text, OUT_DATA_PATH + 'hr_new_deps.csv')

