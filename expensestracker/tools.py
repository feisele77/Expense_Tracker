from datetime import datetime
import os
import shutil
import babel.numbers


DATA_DIR = 'ExpenseTrackerTest'


def get_data_dir():
    return os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), f'AppData\\Roaming\\{DATA_DIR}')


def create_app_folders():
    """ Checks if the folders for the app exists in the user directory, and creates them if not. """
    data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    archive_dir = os.path.join(data_dir, 'archive')
    if not os.path.exists(archive_dir):
        os.mkdir(archive_dir)


def clean_amount(amount_str: str) -> str:
    """ Removes any characters from the amount string that are not part of a number. """
    number_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', ',', '.']
    cleaned_chars = [n for n in amount_str if str(n) in number_chars]
    return ''.join(cleaned_chars)


def convert_amount(amount_str: str, number_format) -> float:
    """ Takes an amount string representing a numeric value and returns it as a float. """
    cleaned_amount = clean_amount(amount_str)
    if number_format == '1.234,56':
        return float(babel.numbers.parse_decimal(cleaned_amount, locale='de'))
    else:
        return float(cleaned_amount)


def convert_date(date_str: str, date_format: str) -> datetime:
    """ Takes a date string and a date format string, returns a datetime object. """
    date_formats = {
        'DD.MM.YYYY': '%d.%m.%Y',
        'YYYY-MM-DD': '%Y-%m-%d',
        'MM/DD/YYYY': '%m/%d/%Y'
    }
    return datetime.strptime(date_str, date_formats[date_format])


def make_db_backup():
    """ Makes a copy of the database with the current timestamp. """
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    database = os.path.join(get_data_dir(), 'expenses.db')
    database_copy = os.path.join(get_data_dir(), f'expenses_{timestamp}.db')
    if os.path.exists(database):
        shutil.copy(database, database_copy)


def archive_import_file(filepath: str):
    """ Save a copy of the imported expense file with a timestamp. """
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = ''.join((timestamp, '_', os.path.basename(filepath)))
    targetpath = os.path.join(get_data_dir(), 'archive', filename)
    shutil.copy(filepath, targetpath)
