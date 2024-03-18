from PyQt6.QtWidgets import QDialog

from ui.ui_dlg_category_mapping_edit import Ui_dlg_category_mappings
from expensestracker.database import Database, CategoryMappings


class DlgCategoryMappingEdit(QDialog, Ui_dlg_category_mappings):
    def __init__(self, account_id: int,  mapping_id):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        # Add the available options for the fieldnames
        self.cmb_fieldname.addItem('name')
        self.cmb_fieldname.addItem('purpose')
        self.cmb_fieldname.addItem('iban')

        self.account_id = account_id

        # Populate the categories combobox
        self.categories = self.db.get_categories_for_account(self.account_id)
        for category in self.categories:
            self.cmb_categories.addItem(f'{category.main_category} - {category.sub_category}', userData=category.id)

        # Populate the fields with the values for the mapping for the given mapping_id (we are in edit mode), otherwise set category_mapping to None (add mode)
        if mapping_id:
            self.category_mapping = self.db.get_category_mapping_by_id(mapping_id)
            self.txt_matchedtext.setText(self.category_mapping.field_value)
            self.cmb_fieldname.setCurrentText(self.category_mapping.account_field)
            self.cmb_categories.setCurrentIndex(self.cmb_categories.findData(self.category_mapping.category_id))
        else:
            self.category_mapping = None

        self.btn_save.setEnabled(False)

        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)
        self.txt_matchedtext.textChanged.connect(self.text_changed)

        self.text_changed()

    def text_changed(self):
        """ Only have the save button enabled if the necessary fields have data. """
        if len(self.txt_matchedtext.text()) > 0:
            self.btn_save.setEnabled(True)
        else:
            self.btn_save.setEnabled(False)

    def save(self):
        """ Save new category mapping or save the changes made to the edited category. """
        if self.category_mapping:
            self.category_mapping.account_field = self.cmb_fieldname.currentText()
            self.category_mapping.field_value = self.txt_matchedtext.text()
            self.category_mapping.category_id = self.cmb_categories.currentData()
            self.db.upsert_category_mapping(self.category_mapping)
        else:
            new_category_mapping = CategoryMappings(
                account_id=self.account_id,
                account_field=self.cmb_fieldname.currentText().lower(),
                field_value=self.txt_matchedtext.text().lower(),
                category_id=self.cmb_categories.currentData()
            )
            self.db.upsert_category_mapping(new_category_mapping)
        self.hide()

    def cancel(self):
        """ Just close the dialog. """
        self.db.disconnect()
        self.hide()
