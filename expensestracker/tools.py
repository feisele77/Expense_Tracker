from datetime import datetime
import babel.numbers


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

