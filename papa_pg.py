from module.modules import *
from colorama import Fore, Style, init
import psycopg2

#conn = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")

def dbexec(execstr):
    print('# dbexec')
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr)
        con.commit()
        if verb:
            p_blue(execstr)
    except (Exception) as error:
        print ('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

def db_exec_vec(execstr, vec):
    print('# db_exec_vec')
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr, vec)
        con.commit()
        if verb:
            print(vec[0])
    except (Exception) as error:
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
 
            
def clear_table(table):
    execstr =  f'DELETE FROM {table}'
    dbexec(execstr)

def clear_otbor():
    clear_table('otbor')
def clear_dep():
    print('# clear_dep')
    clear_table('departments')
def clear_term():
    print('# clear_term')
    clear_table('terminals')

def insert_otbor(v):
    query = f""" INSERT INTO otbor (term, dep)
                              VALUES ({v[0]}, {v[1]});"""
    dbexec(query)

def insert_one_dep(v):
    print('# insert_one_dep')
    q = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    db_exec_vec(q, v)
    
def insert_one_term(v):
    print('# insert_one_term')
    q = '''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
    db_exec_vec(q, v)    


def insert_all_deps():
    print('# insert_all_deps')
    clear_dep()
    q_err = 0
    query = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')

        data = file_to_arr(IN_DATA_PATH + 'departments.csv')
        if 'department' in data[0][0]:
            data = data[1:]
        size_line = len(data[0])

        for vec in data:
            if vec[0] and len(vec) == size_line:
                cur.execute(query, vec)
            else:
                q_err += 1
                print(f'>> {vec[0]} {len(vec)=}')                    
            #con.commit()
            if verb:
                print(vec[0])                
        con.commit()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('end\n')
    else:
        print('end', 'errors:', q_err, '\n')

def insert_all_terms():
    print('# insert_all_terms')
    clear_term()
    q_err = 0
    query = '''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')

        data = file_to_arr(IN_DATA_PATH + 'terminals.csv')
        if 'department' in data[0][0]:
            data = data[1:]
        
        size_line = len(data[0])
        
        for vec in data:
            if vec[1] and len(vec) == size_line:
                cur.execute(query, vec)
            else:
                q_err += 1
                print(f'>> {vec[1]} {len(vec)=}')                    
            #con.commit()
            if verb:
                print(vec[1])                
        con.commit()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('end\n')
    else:
        print('end', 'errors:', q_err, '\n')


def insert_all_otbor():
    print('# insert_all_otbor')
    clear_otbor()
    q_err = 0

    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')

        data = file_to_arr(IN_DATA_PATH + 'otbor.csv')
        if 'term' in data[0][0]:
            data = data[1:]
        size_line = len(data[0])
        
        for vec in data:
            if vec[0] and vec[1] and len(vec) == size_line:
                query = f""" INSERT INTO otbor (term, dep)
VALUES ({vec[0]}, {vec[1]});"""
                cur.execute(query)
                print('->', vec[0])
            else:
                q_err += 1
                print(f'>> {vec[1]} {len(vec)=}')                    
            #con.commit()
            if verb:
                print(vec[1])                
        con.commit()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('end\n')
    else:
        print('end', 'errors:', q_err, '\n')



def select_deps():
    print('# select_deps')
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute("SELECT *  FROM departments")
        rows = cur.fetchall()
        arr_to_file(rows, IN_DATA_PATH + 'pg_departments.csv')      

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    p_green('end\n')
        
def select_terms():
    print('# select_terms')
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute("SELECT *  FROM terminals")
        rows = cur.fetchall()
        arr_to_file(rows, IN_DATA_PATH + 'pg_terminals.csv')      

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    p_green('end\n')

def get_terms_data():
    print('# get_terms_data')
    query = '''SELECT otbor.term, departments.id_terminal, departments.city,departments.region, 
departments.street_type, departments.street, departments.hous, 
terminals.serial_number, terminals.fiscal_number
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows

def get_summury_data():
    print('get_summury_data')
    u = "'1700999'"
    query = f'''SELECT department, region, district_region, post_index, city_type, city, district_city, street_type, street, hous, address, koatu, partner
FROM departments
WHERE department != {u}
ORDER BY department;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows


def get_site_data():
    print('# get_site_data')
    u1 = "'1700999'"
    u2 = "'ТЕСТ'"
    u3 = "'EPS-МІСТ'"
    u4 = "'Меркурій'"
    u5 = "''"
    u6 = "'Ситиком'"
    u7 = "'1980001'"
    u8 = "'1980001'"
    query = f'''SELECT department, edrpou, address, register  FROM departments
WHERE department != {u1}
AND department != {u2}
AND partner != {u3}
AND partner != {u4}
AND partner != {u5}
AND partner != {u6}
AND partner != {u7}
AND partner != {u8}
ORDER BY department'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    return rows
    p_green('end\n')

def get_natasha_data():
    print('# get_natasha_data')
    query = f'''SELECT department, edrpou, partner FROM departments
ORDER BY partner'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    return rows
    print(rows)
    p_green('end\n')


def get_terminals_list():
    print('# get_terminals_list')
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    p_green('end\n')
    return out_list


def get_otbor_deps():
    print('# get_terminals_list')
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    p_green('end\n')
    return out_list



def col_key_pg(hh, key_col_num = -1):
    os.system('cls')
    print('\n\n')
    s = set()
    for line in hh:
        try:
            key = line[key_col_num]
            s.add(key)
        except:
            #('>> no key', key)
            pass
    
    listkey = list(s)
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]

def get_kabinet_knigi_data():
    print('# get_kabinet_knigi_data')
    query = '''SELECT terminals.fiscal_number, terminals.model, terminals.serial_number,
terminals.soft, terminals.rne_rro, terminals.department,
departments.address, departments.koatu, departments.tax_id,
terminals.oro_number, terminals.oro_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows


def get_kabinet_rro_data():
    print('# get_kabinet_knigi_data')
    query = '''SELECT terminals.department,
departments.post_index, departments.region, departments.district_region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.oro_serial, terminals.ticket_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows


def get_kabinet_pereezd_data():
    print('# get_kabinet_knigi_data')
    query = '''SELECT terminals.department,
departments.post_index, departments.region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.fiscal_number, terminals.oro_serial, terminals.ticket_serial,
terminals.to_rro,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows

def get_kabinet_otmena_data():
    print('# get_kabinet_knigi_data')
    query = '''SELECT terminals.ticket_number, terminals.serial_number,
terminals.model, terminals.soft, terminals.rne_rro, 
departments.address, departments.koatu, departments.tax_id,
terminals.fiscal_number, departments.department
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    p_green('end\n')
    return rows





verb = False

 
'''
insert_all_otbor()    
init()
#verb = True
verb = False

select_terms()
#select_deps()
#insert_all_terms()
#insert_all_deps()



#clear_term()
#insert_otbor(['11', '12'])

'''
