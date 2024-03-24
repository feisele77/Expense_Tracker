import configparser as cp
import os

from expensestracker import tools

CFG_FILE = 'ExpenseTracker.cfg'


class Config:
    def __init__(self):
        self.cfg = cp.ConfigParser()
        if not os.path.exists(os.path.join(tools.get_data_dir(), CFG_FILE)):
            self.create_initial_cfg()
        self.cfg.read(os.path.join(tools.get_data_dir(), CFG_FILE))

    def get_value(self, section: str, attribute: str):
        return self.cfg.get(section, attribute)

    def set_value(self, section: str, attribute: str, value: str):
        self.cfg.set(section, attribute, value)

    def create_initial_cfg(self):
        self.cfg['general'] = {'planned_expenses_months': '2',
                               'archive_imported_files': '1',
                               'duplicates_check': '1'
                               }
        self.cfg['mainwin'] = {'width': '1800',
                               'height': '1000',
                               'x': '1',
                               'y': '1'
                               }
        self.cfg['expense_table'] = {'col_date': '80',
                                     'col_name': '250',
                                     'col_purpose': '400',
                                     'col_iban': '170',
                                     'col_amount': '80',
                                     'col_main_category': '150',
                                     'col_sub_category': '150',
                                     'col_comment': '250'
                                     }
        with open(os.path.join(tools.get_data_dir(), CFG_FILE), 'w') as cfgfile:
            self.cfg.write(cfgfile)

    def save_config(self):
        with open(os.path.join(tools.get_data_dir(), CFG_FILE), 'w') as cfgfile:
            self.cfg.write(cfgfile)
