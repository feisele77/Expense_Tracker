from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView
from PyQt6.QtCore import QSize

from ui.ui_category_manager import Ui_dlg_category_manager
from expensestracker.database import Database
from ui import DlgCategoryEdit


class DlgCategoryManager(QDialog, Ui_dlg_category_manager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(QSize(600, 350))

        self.db = Database()
        self.accounts = self.db.get_all_accounts()
        self.current_account = None
        self.categories = None
        self.selected_category_id = None

        for account in self.accounts:
            self.cmb_accounts.addItem(account.name, userData=account.id)

        self.btn_edit.setEnabled(False)
        self.btn_delete.setEnabled(False)

        self.tbl_categories.setColumnHidden(0, True)
        self.tbl_categories.setColumnWidth(1, 200)
        self.tbl_categories.setColumnWidth(2, 200)
        self.tbl_categories.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_categories.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.btn_close.clicked.connect(self.close)
        self.btn_new.clicked.connect(self.new_category)
        self.btn_delete.clicked.connect(self.delete_category)
        self.btn_edit.clicked.connect(self.edit_category)
        self.cmb_accounts.currentIndexChanged.connect(self.account_selection_changed)
        self.tbl_categories.itemSelectionChanged.connect(self.category_selection_changed)

        self.account_selection_changed()

    def new_category(self):
        dlg = DlgCategoryEdit.DlgCategoryEdit(category_id=None, account_id=self.current_account.id)
        dlg.exec()
        self.account_selection_changed()

    def edit_category(self):
        category_id = int(self.tbl_categories.item(self.tbl_categories.selectedItems()[0].row(), 0).text())
        dlg = DlgCategoryEdit.DlgCategoryEdit(category_id=category_id, account_id=self.current_account.id)
        dlg.exec()
        self.account_selection_changed()

    def delete_category(self):
        category_id = int(self.tbl_categories.item(self.tbl_categories.selectedItems()[0].row(), 0).text())
        self.db.delete_category(category_id)
        self.account_selection_changed()

    def account_selection_changed(self):
        idx = self.cmb_accounts.currentIndex()
        self.current_account = self.accounts[idx]
        self.categories = self.db.get_categories_for_account(self.current_account.id)
        self.tbl_categories.clearContents()
        self.tbl_categories.setRowCount(len(self.categories))
        for idx, category in enumerate(self.categories):
            self.tbl_categories.setItem(idx, 0, QTableWidgetItem(str(category.id)))
            self.tbl_categories.setItem(idx, 1, QTableWidgetItem(category.main_category))
            self.tbl_categories.setItem(idx, 2, QTableWidgetItem(category.sub_category))

    def category_selection_changed(self):
        """ Deactivate edit and delete buttons if no categorx is selected. """
        if not self.tbl_categories.selectedItems():
            self.btn_edit.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.selected_category_id = None
        else:
            self.btn_edit.setEnabled(True)
            self.btn_delete.setEnabled(True)

    def close(self):
        self.hide()
