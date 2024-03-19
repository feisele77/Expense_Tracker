from PyQt6.QtWidgets import QDialog

from ui.ui_planned_expenses_edit import Ui_dlg_planned_expenses_edit
from expensestracker.database import Database, PlannedExpenses


class DlgPlannedExpensesEdit(QDialog, Ui_dlg_planned_expenses_edit):
    def __init__(self, account_id, planned_expense_id):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.account_id = account_id

        # Populate the categories combobox
        self.categories = self.db.get_categories_for_account(self.account_id)
        for category in self.categories:
            self.cmb_category.addItem(f'{category.main_category} - {category.sub_category}', userData=category.id)

        if planned_expense_id:
            self.planned_expense = self.db.get_planned_expense_for_id(planned_expense_id)
            self.txt_name.setText(self.planned_expense.name)
            self.cmb_category.setCurrentIndex(self.cmb_category.findData(self.planned_expense.category_id))
            self.spn_amount.setValue(self.planned_expense.amount)
            self.spn_frequency.setValue(self.planned_expense.frequency)
            self.spn_day.setValue(self.planned_expense.day)
            self.dat_startdate.setDate(self.planned_expense.start_date)
            self.chk_autodelete.setChecked(self.planned_expense.auto_delete)
            self.chk_autodecrement.setChecked(self.planned_expense.auto_decrement)
            self.chk_active.setChecked(self.planned_expense.active)
        else:
            self.planned_expense = None

        # self.btn_save.setEnabled(False)

        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)

    def save(self):
        if self.planned_expense:
            self.planned_expense.name = self.txt_name.text()
            self.planned_expense.amount = self.spn_amount.value()
            self.planned_expense.frequency = self.spn_frequency.value()
            self.planned_expense.day = self.spn_day.value()
            self.planned_expense.start_date = self.dat_startdate.date().toPyDate()
            self.planned_expense.auto_delete = self.chk_autodelete.isChecked()
            self.planned_expense.auto_decrement = self.chk_autodecrement.isChecked()
            self.planned_expense.category_id = self.cmb_category.currentData()
            self.planned_expense.active = self.chk_active.isChecked()
        else:
            self.planned_expense = PlannedExpenses(
                account_id=self.account_id,
                name=self.txt_name.text(),
                amount=self.spn_amount.value(),
                frequency=self.spn_frequency.value(),
                day=self.spn_day.value(),
                start_date=self.dat_startdate.date().toPyDate(),
                auto_delete=self.chk_autodelete.isChecked(),
                auto_decrement=self.chk_autodecrement.isChecked(),
                category_id=self.cmb_category.currentData(),
                active=self.chk_active.isChecked()
            )
        self.db.upsert_planned_expense(self.planned_expense)
        self.db.disconnect()
        self.hide()

    def cancel(self):
        self.db.disconnect()
        self.hide()
