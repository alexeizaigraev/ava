from module.modules import *
from module.modules_base import *
from papa_pg import *

def niseStr(str):
    return str.replace("’", '').replace("'", '').replace(' ', '').replace('-', '').lower()

def strInBoth(str1, str2):
    str1 = niseStr(str1)
    str2 = niseStr(str2)
    if ( str1 in str2 ) or ( str2 in str1 ):
        return True
    return False

def mk_koatu2(workLine):
    sity = workLine[5]
    distrSity = workLine[6]
    koatu = workLine[11]
    adrFull = workLine[10]
    
    for line in koatuSpr:
        sprKoatu = line[1]
        sprPlace = line[2]
        
        if strInBoth(koatu, sprKoatu) \
        and ( strInBoth(sprPlace, sity) or ( strInBoth(sprPlace, distrSity) ) ):
            return line[0]
    return ''
"""    
def mk_koatu2(line):
    bigline = niseStr(''.join(line))
    for line in koatuSpr:
        if line[1] in bigline and niseStr(line[2]) in niseStr(bigline):
            return line[0]
    return ''
"""
my_key = 'partner'

koatuSpr = file_to_arr(IN_DATA_PATH + 'koatuall.csv')

head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Область;Район в обл.;Індекс;Тип населеного пункту;Населений пункт;Район в місті;Тип вулиці;Адреса;Номер будинку;Дата признчення керівника;модель РРО;Заводський № РРО;2;koatu1;koatu2\n'
out_text = head
data = get_summury_data()

partner = col_key_pg(data)
print(f'\n\n\t{partner}\n\n')

my_deps = []
count = 0
for line in data:
    
    try:
        if line[-1] == partner:
            dep = line[0]
            if dep in my_deps:
                continue
            my_deps.append(dep)
            count += 1
            out_line = (str(count) + ';' 
                        + line[0]  + ';'
                        + line[1] + ';'
                        + line[2] + ';'
                        + line[3] + ';'
                        + line[4] + ';'
                        + line[5] + ';'
                        + line[6] + ';'
                        + line[7] + ';'
                        + line[8] + ';'
                        + line[9] + ';'
                        + '' + ';'
                        + '' + ';'
                        + '' + ';'
                        + line[10] + ';'
                        + line[11] + ';'
                        + mk_koatu2(line) )
            out_text += out_line + '\n'
                        
    except:
        pass

text_to_file(out_text, OUT_DATA_PATH + 'hr_new_deps.csv')

