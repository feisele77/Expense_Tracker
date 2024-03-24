from PyQt6.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem, QMessageBox

from ui.ui_account_manager import Ui_dlg_account_manager
from ui import DlgAccountEditor
from expensestracker.database import Database


class DlgAccountManager(QDialog, Ui_dlg_account_manager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.accounts = self.db.get_all_accounts()

        self.btn_close.clicked.connect(self.hide)
        self.btn_add_account.clicked.connect(self.newAccount)
        self.btn_edit_account.clicked.connect(self.editAccount)
        self.btn_delete_account.clicked.connect(self.deleteAccount)

        self.tbl_accounts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_accounts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_accounts.setColumnHidden(0, True)
        self.tbl_accounts.setColumnWidth(1, 250)
        self.tbl_accounts.itemSelectionChanged.connect(self.account_selection_changed)
        self.populate_table()
        self.account_selection_changed()

    def populate_table(self):
        """ Loads the accounts from the database and populates the accounts table. """
        self.tbl_accounts.clearContents()
        self.accounts = self.db.get_all_accounts()
        self.tbl_accounts.setRowCount(len(self.accounts))
        for idx, row in enumerate(self.accounts):
            self.tbl_accounts.setItem(idx, 0, QTableWidgetItem(str(row.id)))
            self.tbl_accounts.setItem(idx, 1, QTableWidgetItem(row.name))
            self.tbl_accounts.setItem(idx, 2, QTableWidgetItem(row.type))

    def account_selection_changed(self):
        """ Deactivate edit and delete buttons if no account is selected. """
        if not self.tbl_accounts.selectedItems():
            self.btn_edit_account.setEnabled(False)
            self.btn_delete_account.setEnabled(False)
        else:
            self.btn_edit_account.setEnabled(True)
            self.btn_delete_account.setEnabled(True)

    def deleteAccount(self):
        """ Deletes the selected account from the database, together with all expenses, categories and planned expenses that might exist for the account. """
        confirmation = QMessageBox.question(self, 'Delete account?',
                                            'Do you really want to delete the selected account? All existing expenses and categories for this account are being deleted as well!')
        if confirmation == QMessageBox.StandardButton.Yes:
            account_id = int(self.tbl_accounts.item(self.tbl_accounts.selectedItems()[0].row(), 0).text())
            self.db.delete_account(account_id)
        self.populate_table()

    def newAccount(self):
        """ Opens the Account Editor to create a new account. """
        dlg = DlgAccountEditor.DlgAccountEditor(account_id=None)
        dlg.exec()
        self.populate_table()

    def editAccount(self):
        """ Opens the Account Editor to edit the selected account. """
        account_id = int(self.tbl_accounts.item(self.tbl_accounts.selectedItems()[0].row(), 0).text())
        dlg = DlgAccountEditor.DlgAccountEditor(account_id=account_id)
        dlg.exec()
        self.populate_table()
