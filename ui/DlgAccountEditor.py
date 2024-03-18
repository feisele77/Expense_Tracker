from PyQt6.QtWidgets import QDialog

from ui.ui_account_editor import Ui_DlgAccountEditor
from expensestracker import database
from expensestracker.database import Database


class DlgAccountEditor(QDialog, Ui_DlgAccountEditor):
    def __init__(self, account_id=None):
        super().__init__()
        self.setupUi(self)
        self.account_id = account_id
        self.db = Database()

        self.cmb_filetype.addItems(['', 'CSV', 'Excel', 'No Import'])
        self.cmb_encoding.addItems(['UTF-8', ])
        self.cmb_field_delimiter.addItems(['Comma (,)', 'Semicolon (;)', 'Tab'])
        self.cmb_quotechar.addItems(['"', 'None'])
        self.cmb_account_type.addItems(['Normal', 'Savings', 'Credit Card'])
        self.cmb_currency.addItems(['EUR', 'USD', 'RON'])
        self.cmb_date_format.addItems(['DD.MM.YYYY', 'YYYY-MM-DD', 'MM/DD/YYYY'])
        self.cmb_number_format.addItems(['1.234,56', '1,234.56'])

        self.cmb_filetype.setCurrentText('')

        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)
        self.cmb_filetype.currentTextChanged.connect(self.filetype_changed)

    def filetype_changed(self):
        """ Sets the fields that are only required for CSV files to disabled if filetype is not CSV. """
        if self.cmb_filetype.currentText() == 'Excel' or self.cmb_filetype.currentText() == '':
            self.cmb_field_delimiter.setEnabled(False)
            self.cmb_quotechar.setEnabled(False)
            self.cmb_encoding.setEnabled(False)
        elif self.cmb_filetype.currentText() == 'CSV':
            self.cmb_field_delimiter.setEnabled(True)
            self.cmb_quotechar.setEnabled(True)
            self.cmb_encoding.setEnabled(True)

    def check_entries(self):
        pass

    def save(self):
        self.check_entries()
        account = database.Accounts(
            name=self.txt_account_name.text(),
            iban=self.txt_account_iban.text(),
            currency=self.cmb_currency.currentText(),
            type=self.cmb_account_type.currentText(),
            balance=float(self.txt_account_balance.text()),
            first_data_row=int(self.spn_first_data_row.text()),
            encoding=self.cmb_encoding.currentText(),
            col_date=int(self.spn_col_date.text()),
            col_name=int(self.spn_col_name.text()),
            col_purpose=int(self.spn_col_purpose.text()),
            col_iban=int(self.spn_col_iban.text()),
            col_amount=int(self.spn_col_amount.text()),
            dateformat=self.cmb_date_format.currentText(),
            numberformat=self.cmb_number_format.currentText(),
            filetype=self.cmb_filetype.currentText(),
            delimiter=self.cmb_field_delimiter.currentText(),
            quotechar=self.cmb_quotechar.currentText()
        )
        self.db.upsert_account(account)
        self.hide()

    def cancel(self):
        self.hide()
