from PyQt6.QtWidgets import QDialog

from ui.ui_account_editor import Ui_DlgAccountEditor
from expensestracker.database import Database, Accounts


class DlgAccountEditor(QDialog, Ui_DlgAccountEditor):
    def __init__(self, account_id=None):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.cmb_filetype.addItems(['No Import', 'CSV', 'Excel'])
        self.cmb_encoding.addItems(['UTF-8', ])
        self.cmb_field_delimiter.addItems(['Comma (,)', 'Semicolon (;)', 'Tab'])
        self.cmb_quotechar.addItems(['"', 'None'])
        self.cmb_account_type.addItems(['Normal', 'Savings', 'Credit Card'])
        self.cmb_currency.addItems(['EUR', 'USD', 'RON'])
        self.cmb_date_format.addItems(['DD.MM.YYYY', 'YYYY-MM-DD', 'MM/DD/YYYY'])
        self.cmb_number_format.addItems(['1.234,56', '1,234.56'])

        if account_id:
            self.account = self.db.get_account_by_id(account_id)
            self.txt_account_name.setText(self.account.name)
            self.txt_account_iban.setText(self.account.iban)
            self.cmb_account_type.setCurrentText(self.account.type)
            self.cmb_currency.setCurrentText(self.account.currency)
            self.spn_balance.setValue(self.account.balance)
            self.chk_include_overall_balance.setChecked(self.account.include_in_sum)
            self.cmb_filetype.setCurrentText(self.account.filetype)
            if self.account.filetype == 'CSV' or self.account.filetype == 'Excel':
                self.spn_col_name.setValue(self.account.col_name)
                self.spn_col_date.setValue(self.account.col_date)
                self.spn_col_iban.setValue(self.account.col_iban)
                self.spn_col_purpose.setValue(self.account.col_purpose)
                self.spn_col_amount.setValue(self.account.col_amount)
                self.spn_first_data_row.setValue(self.account.first_data_row)
                self.cmb_date_format.setCurrentText(self.account.dateformat)
                self.cmb_number_format.setCurrentText(self.account.numberformat)
            if self.account.filetype == 'CSV':
                self.cmb_field_delimiter.setCurrentText(self.account.delimiter)
                self.cmb_quotechar.setCurrentText(self.account.quotechar)
                self.cmb_encoding.setCurrentText(self.account.encoding)
        else:
            self.account = None

        self.btn_save.clicked.connect(self.save)
        self.btn_cancel.clicked.connect(self.hide)

        self.cmb_filetype.currentTextChanged.connect(self.filetype_changed)
        self.cmb_filetype.currentTextChanged.connect(self.check_entries)
        self.txt_account_name.textChanged.connect(self.check_entries)
        self.cmb_filetype.currentTextChanged.connect(self.check_entries)

        self.filetype_changed()
        self.check_entries()

    def filetype_changed(self):
        """ Sets the fields that are only required for CSV files to disabled if filetype is not CSV. """
        if self.cmb_filetype.currentText() == 'No Import':
            self.cmb_field_delimiter.setEnabled(False)
            self.cmb_quotechar.setEnabled(False)
            self.cmb_encoding.setEnabled(False)
            self.spn_first_data_row.setEnabled(False)
            self.cmb_date_format.setEnabled(False)
            self.cmb_number_format.setEnabled(False)
            self.spn_col_name.setEnabled(False)
            self.spn_col_date.setEnabled(False)
            self.spn_col_iban.setEnabled(False)
            self.spn_col_purpose.setEnabled(False)
            self.spn_col_amount.setEnabled(False)
        elif self.cmb_filetype.currentText() == 'Excel':
            self.cmb_field_delimiter.setEnabled(False)
            self.cmb_quotechar.setEnabled(False)
            self.cmb_encoding.setEnabled(False)
            self.spn_first_data_row.setEnabled(True)
            self.cmb_date_format.setEnabled(True)
            self.cmb_number_format.setEnabled(True)
            self.spn_col_name.setEnabled(True)
            self.spn_col_date.setEnabled(True)
            self.spn_col_iban.setEnabled(True)
            self.spn_col_purpose.setEnabled(True)
            self.spn_col_amount.setEnabled(True)
        elif self.cmb_filetype.currentText() == 'CSV':
            self.cmb_field_delimiter.setEnabled(True)
            self.cmb_quotechar.setEnabled(True)
            self.cmb_encoding.setEnabled(True)
            self.spn_first_data_row.setEnabled(True)
            self.cmb_date_format.setEnabled(True)
            self.cmb_number_format.setEnabled(True)
            self.spn_col_name.setEnabled(True)
            self.spn_col_date.setEnabled(True)
            self.spn_col_iban.setEnabled(True)
            self.spn_col_purpose.setEnabled(True)
            self.spn_col_amount.setEnabled(True)

    def check_entries(self):
        """ Checks if the entries made by the user are sufficient for saving the new/edited account. Enabled/disables the Save button accordingly. """
        entries_are_sufficient = True
        # Check the fields that are always mandatory
        if not self.txt_account_name.text() or not self.cmb_filetype.currentText():
            entries_are_sufficient = False

        if entries_are_sufficient:
            self.btn_save.setEnabled(True)
        else:
            self.btn_save.setEnabled(False)

    def save(self):
        """ Saves the new or edited account. """
        # Create a new account object in case we are saving a new account here
        if not self.account:
            self.account = Accounts()
        self.account.name = self.txt_account_name.text()
        self.account.iban = self.txt_account_iban.text()
        self.account.currency = self.cmb_currency.currentText()
        self.account.balance = self.spn_balance.value()
        self.account.type = self.cmb_account_type.currentText()
        self.account.include_in_sum = self.chk_include_overall_balance.isChecked()
        self.account.filetype = self.cmb_filetype.currentText()
        if self.cmb_filetype.currentText() == 'CSV' or self.cmb_filetype.currentText() == 'Excel':
            self.account.first_data_row = int(self.spn_first_data_row.text())
            self.account.dateformat = self.cmb_date_format.currentText()
            self.account.numberformat = self.cmb_number_format.currentText()
            self.account.col_date = int(self.spn_col_date.text())
            self.account.col_name = int(self.spn_col_name.text())
            self.account.col_purpose = int(self.spn_col_purpose.text())
            self.account.col_iban = int(self.spn_col_iban.text())
            self.account.col_amount = int(self.spn_col_amount.text())
        if self.cmb_filetype.currentText() == 'CSV':
            self.account.encoding = self.cmb_encoding.currentText()
            self.account.delimiter = self.cmb_field_delimiter.currentText()
            self.account.quotechar = self.cmb_quotechar.currentText()

        if not self.account.id:
            account_id = self.db.upsert_account(self.account)
            self.db.add_default_category_for_account(account_id)
        else:
            _ = self.db.upsert_account(self.account)
        self.hide()
