import configparser as cp
import os

CFG_FILE = 'ExpenseTracker.cfg'


def get_data_dir():
    return os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), r'AppData\Roaming\ExpenseTracker')


def create_initial_cfg():
    cfg = cp.ConfigParser()
    cfg['general'] = {'planned_expenses_months': '2'}
    cfg['mainwin'] = {'width': '1800',
                      'height': '1000',
                      'x': '50',
                      'y': '50'}
    cfg['expense_table'] = {'col_Name': '120',
                            'col_IBAN': '100'}
    with open(os.path.join(get_data_dir(), CFG_FILE), 'w') as cfgfile:
        cfg.write(cfgfile)


def get_value(section: str, attribute: str):
    cfg = cp.ConfigParser()
    cfg.read(os.path.join(get_data_dir(), CFG_FILE))
    return cfg.get(section, attribute)


if not os.path.exists(os.path.join(get_data_dir(), CFG_FILE)):
    create_initial_cfg()
