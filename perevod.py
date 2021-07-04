from module.modules import *
from papa_class import *

class Perevod(Papa):

    def perevod_main(self):
        self.ColFioOne = 0
        self.ColDepOne = 1

        fname_out = 'OutPerevod.csv'
        out_text = ''
        out_text_unfind = ''

        #self.kass_all = self.mk_kass_all()
        self.kass_all = []
        self.kass_all_hash = self.mk_kass_all_hash()

        for line_str in open(IN_DATA_PATH + 'perevod.csv', 'r', encoding="UTF-8"):
            self.work_vec = line_str.strip().split(';')
            self.surname, self.firstname, self.lastname = self.mk_fio_split()
            
            my_login = self.login_hash()
            
            if not self.login_ok:
                out_text_unfind += f'{self.work_vec[0]};{self.work_vec[1]};{self.work_vec[2]}\n'
                continue
            else:
                for unit in my_login:
                    out_text += unit + ';' + self.work_vec[1] + ';' + self.work_vec[2] + "\n"

        full_out_fname = OUT_DATA_PATH + fname_out
        #text_to_file(out_text_unfind + out_text, full_out_fname)
        save_and_show(out_text_unfind + out_text, full_out_fname)

        if out_text_unfind:
            p_red('\tunfind\n')
        else:
            p_yellow('\twell\n')

u = Perevod()
u.perevod_main()
