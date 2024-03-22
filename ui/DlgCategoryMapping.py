from PyQt6.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem, QMessageBox

from ui.ui_category_mapping import Ui_dlg_category_mappings
from ui.DlgCategoryMappingEdit import DlgCategoryMappingEdit
from expensestracker.database import Database


class DlgCategoryMapping(QDialog, Ui_dlg_category_mappings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.accounts = self.db.get_all_accounts()
        self.current_account = None
        self.categories = None
        self.category_mappings = None

        for account in self.accounts:
            self.cmb_accounts.addItem(account.name, userData=account.id)

        self.tbl_mappings.setColumnHidden(0, True)
        self.tbl_mappings.setColumnWidth(1, 80)
        self.tbl_mappings.setColumnWidth(2, 250)
        self.tbl_mappings.setColumnWidth(3, 220)
        self.tbl_mappings.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_mappings.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.cmb_accounts.currentIndexChanged.connect(self.account_selection_changed)
        self.btn_close.clicked.connect(self.close)
        self.btn_new.clicked.connect(self.new_category_mapping)
        self.btn_delete.clicked.connect(self.delete_category_mapping)
        self.btn_edit.clicked.connect(self.edit_category_mapping)

        self.account_selection_changed()

    def account_selection_changed(self):
        idx = self.cmb_accounts.currentIndex()
        self.current_account = self.accounts[idx]
        self.category_mappings = self.db.get_category_mappings_for_account(account_id=self.current_account.id)
        self.tbl_mappings.clearContents()
        self.tbl_mappings.setRowCount(len(self.category_mappings))
        for idx, category_mapping in enumerate(self.category_mappings):
            self.tbl_mappings.setItem(idx, 0, QTableWidgetItem(str(category_mapping.CategoryMappings.id)))
            self.tbl_mappings.setItem(idx, 1, QTableWidgetItem(category_mapping.CategoryMappings.account_field))
            self.tbl_mappings.setItem(idx, 2, QTableWidgetItem(category_mapping.CategoryMappings.field_value))
            self.tbl_mappings.setItem(idx, 3, QTableWidgetItem(category_mapping.ExpenseCategories.main_category))
            self.tbl_mappings.setItem(idx, 4, QTableWidgetItem(category_mapping.ExpenseCategories.sub_category))

    def delete_category_mapping(self):
        if self.tbl_mappings.selectedItems():
            confirmation = QMessageBox.question(self, 'Delete category mapping?', 'Do you really want to delete the selected category mapping?')
            if confirmation == QMessageBox.StandardButton.Yes:
                mapping_id = int(self.tbl_mappings.item(self.tbl_mappings.selectedItems()[0].row(), 0).text())
                self.db.delete_category_mapping(mapping_id)
            self.account_selection_changed()

    def new_category_mapping(self):
        dlg = DlgCategoryMappingEdit(self.current_account.id, None)
        dlg.exec()
        self.account_selection_changed()

    def edit_category_mapping(self):
        if self.tbl_mappings.selectedItems():
            mapping_id = int(self.tbl_mappings.item(self.tbl_mappings.selectedItems()[0].row(), 0).text())
            dlg = DlgCategoryMappingEdit(self.current_account.id, mapping_id)
            dlg.exec()
            self.account_selection_changed()

    def close(self):
        self.db.disconnect()
        self.hide()
