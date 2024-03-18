from PyQt6.QtWidgets import QDialog

from ui.ui_category_edit import Ui_dlg_category_edit
from expensestracker.database import Database, ExpenseCategories


class DlgCategoryEdit(QDialog, Ui_dlg_category_edit):
    def __init__(self, category_id: int | None, account_id: int):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.account_id = account_id
        self.categories = self.db.get_categories_for_account(account_id)
        self.main_categories = set()
        for category in self.categories:
            self.main_categories.add(category.main_category)
        for main_category in self.main_categories:
            self.cmb_maincategory.addItem(main_category)

        if category_id:
            self.category = self.db.get_category_by_id(category_id)
            self.txt_subcategory.setText(self.category.sub_category)
            self.cmb_maincategory.setCurrentText(self.category.main_category)
        else:
            self.category = None

        self.btn_save.setEnabled(False)

        self.btn_save.clicked.connect(self.save)
        self.btn_close.clicked.connect(self.cancel)
        self.txt_subcategory.textChanged.connect(self.texts_changed)
        self.cmb_maincategory.currentTextChanged.connect(self.texts_changed)

    def texts_changed(self):
        """ Enable Save button only if both main and sub category fields have values. """
        if self.txt_subcategory.text() and self.cmb_maincategory.currentText():
            self.btn_save.setEnabled(True)
        else:
            self.btn_save.setEnabled(False)

    def save(self):
        """ Save new category in database. """
        if self.category:
            self.category.main_category = self.cmb_maincategory.currentText()
            self.category.sub_category = self.txt_subcategory.text()
            self.db.upsert_category(self.category)
        else:
            new_category = ExpenseCategories(
                account_id=self.account_id,
                main_category=self.cmb_maincategory.currentText(),
                sub_category=self.txt_subcategory.text()
            )
            self.db.upsert_category(new_category)
        self.hide()

    def cancel(self):
        self.hide()
