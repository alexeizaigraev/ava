from module.modules import *
import os
import shutil

class Papa():
    def mk_fio(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0] + ' ' \
                + fio_split[1] + ' ' \
                + fio_split[1]
        return ' '.join(fio_split)

    def mk_fio_split(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0], fio_split[1], fio_split[1]
        return fio_split[0], fio_split[1], fio_split[2]

    def mk_initial_one_dot(self):
        return f'{self.firstname[0]}.'

    def mk_initial_two_dot(self):
        return f'{self.lastname[0]}.'

    def mk_dep(self):
        if '№' in self.work_vec[self.ColDepOne]:
            return self.work_vec[self.ColDepOne].split('№')[-1].strip()
        return self.work_vec[self.ColDepOne].strip()

    def mk_fio_white(self, fff):
        fs = fff.replace('  ', ' ').strip().split(' ')
        surn = fs[0]
        out = surn
        other = ''.join(fs[1:]).replace('.', '').replace(' ', '')
        for leter in other:
            if leter.isupper() and leter.isalpha():
                out += leter
        return out

    def dep_clear(self, deps):
        out = []
        d = deps.replace('[', '').replace(']', '').replace(' ', '').strip()
        if ',' not in d:
            out.append(d[:7])
        else:
            dd = d.split(',')
            for ddd in dd:
                out.append(ddd[:7])
        return out

    def mk_kass_all(self):
        a = []
        for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            try:
                fio_white = self.mk_fio_white(line[2] )
                v = [line[0], fio_white, line[3]]
                a.append(v)
            except:
                print(f'>> err kass_all: {line[self.ColFioTwo]}')
        return a
            



    def login_deep(self, nama, parDep):
        logins = [line[0] for line in self.kass_all
            if ( (parDep in line[2][1:4])
                and (nama in line[1]) ) ]
        
        if logins and ( 1 == len(logins) ):
            self.login_ok = True

        return logins


    def login(self):
        parDep = self.mk_dep()
        self.login_ok = False
        nama = self.mk_fio_white(self.mk_fio())

        logins = [line[0] for line in self.kass_all
            if ( (parDep in line[2])
                and (nama in line[1]) ) ]
        
        if logins:
            self.login_ok = True
            return logins

        return self.login_deep(nama, parDep[:3])

# ____________________________________________________

    def dep_clear(self, deps):
        out = []
        d = deps.replace('[', '').replace(']', '').replace(' ', '').strip()
        if ',' not in d:
            out.append(d[:7])
        else:
            dd = d.split(',')
            for ddd in dd:
                out.append(ddd[:7])
        return out

    def mk_kass_all_hash(self):
        out_hash = dict()
        #kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
        #kass[:] = [line for line in kass if len(line) > 4 and 'true' in line[1]]
        a = []
        #kass = file.open(IN_DATA_PATH + 'kass_all.csv')
        for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            if len(line) > 4 \
                and 'true' in line[1]:
                try:
                    fio_white = self.mk_fio_white(line[2] )
                    login = line[0]
                    deps = self.dep_clear(line[3])
                    for dep in deps:
                        key = fio_white + dep
                        if key not in out_hash:
                            out_hash[key] = []
                        out_hash[key].append(login)
                        

                    #v = [line[ColLoginTwo], fio_white, line[ColDepTwo]]
                    #a.append(v)
                except:
                    print(f'>> err kass_all: {line[2]}')
        return out_hash

    def login_hash_deep(self, parDep, fio):
        rez = []
        key = fio + parDep
        key_list = list(self.kass_all_hash.keys())
        count = 0
        for el in key_list:
            if key in el:
                count += 1
                if count > 1:
                    self.login_ok = False
                    return
                rez = self.kass_all_hash[el]
                self.login_ok = True
        
        return rez


    def login_hash(self):
        login = ''
        parDep = self.mk_dep()
        fio = self.mk_fio_white(self.mk_fio())
        self.login_ok = False
        key = fio + parDep
        try:
            login = self.kass_all_hash[key]
            self.login_ok = True
            return login
        except:
            pass
        if not self.kass_all:
            self.kass_all = self.mk_kass_all()
        return self.login()

        parDep = parDep[:3]
        return self.login()

