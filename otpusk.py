from module.modules import *
from papa_class import *

class Otpusk(Papa):
    
    def status(self):
        return 'otpusk' if self.work_vec[2] else 'uvolnenie'

    def reversedate(self, par_line):
        return '-'.join(reversed(par_line.split('.')))

    def dates(self):
        # Отпуск
        if self.status() == 'otpusk':
            date_start_otpusk = self.reversedate(self.work_vec[1]) + ' ' + '00:00:01'
            date_finish_otpusk = self.reversedate(self.work_vec[2]) + ' ' + '23:59:59'

            date_active_start = '2020-02-02 00:00:01'
            date_active_finish = '2050-02-02 00:00:01'

            return date_start_otpusk + ';' \
                + date_finish_otpusk + ';' \
                + '' + ';' \
                + date_active_start + ';' \
                + date_active_finish
        else:
            date_start_otpusk = ''
            date_finish_otpusk = ''

            date_uvol = self.reversedate(self.work_vec[1]) + ' ' + '23:59:59'

            date_active_start = '2020-02-02 00:00:01'
            date_active_finish = date_uvol

            return date_start_otpusk + ';' \
                + date_finish_otpusk + ';' \
                + date_uvol + ';' \
                + date_active_start + ';' \
                + date_active_finish



    def otpusk_main(self):

        self.ColFioOne = 0
        self.ColDepOne = 3

        fname_out = 'OutOtpuskUvol.csv'
        out_text = ''
        out_text_unfind = ''

        #self.kass_all = self.mk_kass_all()
        self.kass_all = []
        self.kass_all_hash = self.mk_kass_all_hash()

        for line_str in open(IN_DATA_PATH + 'otpusk_uvol.csv', 'r', encoding="UTF-8"):
            self.work_vec = line_str.strip().split(';')
            self.surname, self.firstname, self.lastname = self.mk_fio_split()

            my_login = self.login_hash()
            
            if not self.login_ok:
                out_text_unfind += f'{self.work_vec[0]}\t{self.work_vec[3]}\t;{self.dates()}\n'
                continue        
            else:
                for unit in my_login:
                    out_text += f'{unit};{self.dates()}\n'

                
        full_out_fname = OUT_DATA_PATH + fname_out
        text_to_file(out_text_unfind + out_text, full_out_fname)

        if out_text_unfind:
            p_red('\tunfind\n')
        else:
            p_yellow('\twell\n')

u = Otpusk()
u.otpusk_main()