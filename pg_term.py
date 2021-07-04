from module.modules import *
from module.modules_base import *
from papa_pg import *
import os
from colorama import Fore, Style, init

def def_agent():
    h = dict()
    h['shablon1'] = ''
    h['shablon2'] = ''
    h['soft'] = ''
    h['limit'] = ''
    a = file_to_arr(COMON_DATA_PATH)
    for vec in a:
        if ag_cod in vec[0]:
            h['shablon1'] = vec[ColDataShablon1]
            h['shablon2'] = vec[ColDataShablon2]
            h['soft'] = vec[ColDataSoft]
            h['limit'] = vec[ColDataLimit]
            break
    if 'shablon1' in h['shablon1']:
        sos('Незнакомый агент', ag_cod)
    return h


init()

data = get_terms_data()
line = ''
ag_cog = ''

ColDataShablon1 = 5
ColDataShablon2 = 6
ColDataSoft = 7
ColDataLimit = 8

ColTermTerm = 0
ColTermId = 1
ColTermSity = 2
ColTermRegion = 3
ColTermStreet = 4
ColTermHouse = 5
ColTermSerial = 6


fname_out = 'OutTerminals.csv'
out_text = ''

for line in data:
    terminal = line[0]
    idd = line[1]
    if not idd:
        idd = terminal
        
    sity = line[2]
    region = line[3]
    if not region:
        region = sity

    street_type = line[4]
    street = line[5]
    house = line[6]

    serial = line[7]
    if serial and '0' or 'O' in serial:
        serial = ''.join(line[7].split('0')[1:])
    if not serial:
        serial = line[8]
    if not serial:
        serial = '333'

    ag_cod = terminal[:3]

    out_line = ( terminal + ';'
        +idd + ';' +
        def_agent()['shablon1'] + ';' +
        sity + ', ' + region + ';' +
        street_type + ' ' + street + ', ' + house + ';' +
        def_agent()['shablon2'] + ';' +
        def_agent()['soft'] + ';' +
        def_agent()['limit'] + ';' +
        serial
    )
    

    out_text += out_line + "\n"
    #print(f'{Fore.BLUE} {out_line}')
    p_green(out_line)
full_out_fname = OUT_DATA_PATH + fname_out
text_to_file(out_text, full_out_fname)


"""
        idd + ';' +
        def_agent()['shablon1'] + ';' +
        sity + ', ' + region + ';' +
    street_type + ' ' + street + ', ' + house + ';' +
    def_agent()['shablon2'] + ';' +
    def_agent()['soft'] + ';' +
    def_agent()['limit'] + ';' +
    serial)
"""
    
