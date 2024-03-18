import csv
import openpyxl
from expensestracker import tools


class ImporterCSV:
    def __init__(self, filename, import_def):
        self.filename = filename
        self.import_def = import_def
        self.delimiter = {'Semicolon (;)': ';', 'Comma (,)': ',', 'Tab': '\t'}
        self.quotechar = {'"': '"', 'None': None}

    def parse_data(self) -> list:
        data = []
        with open(self.filename, newline='', encoding=self.import_def.encoding) as infile:
            csvreader = csv.reader(infile, delimiter=self.delimiter[self.import_def.delimiter], quotechar=self.quotechar[self.import_def.quotechar])
            for idx, row in enumerate(csvreader):
                if idx > 0:
                    entry = dict()
                    entry['account_id'] = self.import_def.id
                    if self.import_def.col_date:
                        entry['date'] = tools.convert_date(row[self.import_def.col_date-1], self.import_def.dateformat)
                    if self.import_def.col_name:
                        entry['name'] = row[self.import_def.col_name-1]
                    if self.import_def.col_purpose:
                        entry['purpose'] = row[self.import_def.col_purpose-1]
                    if self.import_def.col_iban:
                        entry['iban'] = row[self.import_def.col_iban-1]
                    if self.import_def.col_amount:
                        entry['amount'] = tools.convert_amount(row[self.import_def.col_amount-1], self.import_def.numberformat)
                    data.append(entry)
        return data


class ImporterExcel:
    def __init__(self, filename, import_def):
        self.filename = filename
        self.import_def = import_def

    def parse_data(self):
        wb = openpyxl.load_workbook(self.filename)
        ws = wb.active
        data = []
        for row in ws.iter_rows(min_row=self.import_def.first_data_row, max_row=10000, min_col=1, max_col=50):
            if row[1].value:
                entry = dict()
                entry['account_id'] = self.import_def.id
                if self.import_def.col_date:
                    entry['date'] = tools.convert_date(row[self.import_def.col_date-1].value, self.import_def.dateformat)
                if self.import_def.col_name:
                    entry['name'] = row[self.import_def.col_name-1].value
                else:
                    entry['name'] = None
                if self.import_def.col_purpose:
                    entry['purpose'] = row[self.import_def.col_purpose-1].value
                else:
                    entry['purpose'] = None
                if self.import_def.col_iban:
                    entry['iban'] = row[self.import_def.col_iban-1].value
                else:
                    entry['iban'] = None
                if self.import_def.col_amount:
                    entry['amount'] = tools.convert_amount(row[self.import_def.col_amount-1].value, self.import_def.numberformat)
                data.append(entry)
            else:
                break
        wb.close()
        return data
