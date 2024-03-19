from PyQt6.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem

from ui.ui_planned_expenses import Ui_dlg_planned_expenses
from expensestracker.database import Database
from ui.DlgPlannedExpensesEdit import DlgPlannedExpensesEdit


class DlgPlannedExpenses(QDialog, Ui_dlg_planned_expenses):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.accounts = self.db.get_all_accounts()
        self.current_account = None
        self.categories = None
        self.planned_expenses = None

        for account in self.accounts:
            self.cmb_accounts.addItem(account.name, userData=account.id)

        self.tbl_planned_expenses.setColumnHidden(0, True)
        self.tbl_planned_expenses.setColumnWidth(1, 200)
        self.tbl_planned_expenses.setColumnWidth(2, 200)
        self.tbl_planned_expenses.setColumnWidth(3, 200)
        self.tbl_planned_expenses.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_planned_expenses.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.cmb_accounts.currentIndexChanged.connect(self.account_selection_changed)
        # self.tbl_planned_expenses.itemSelectionChanged.connect(self.planned_expense_selection_changed)
        self.btn_close.clicked.connect(self.close)
        self.btn_new.clicked.connect(self.new_planned_expense)
        self.btn_delete.clicked.connect(self.delete_planned_expense)
        self.btn_edit.clicked.connect(self.edit_planned_expense)

        self.account_selection_changed()

    def account_selection_changed(self):
        idx = self.cmb_accounts.currentIndex()
        self.current_account = self.accounts[idx]
        self.planned_expenses = self.db.get_planned_expenses_for_account(account_id=self.current_account.id)
        self.tbl_planned_expenses.clearContents()
        self.tbl_planned_expenses.setRowCount(len(self.planned_expenses))
        for idx, planned_expense in enumerate(self.planned_expenses):
            self.tbl_planned_expenses.setItem(idx, 0, QTableWidgetItem(str(planned_expense.PlannedExpenses.id)))
            self.tbl_planned_expenses.setItem(idx, 1, QTableWidgetItem(planned_expense.PlannedExpenses.name))
            self.tbl_planned_expenses.setItem(idx, 2, QTableWidgetItem(planned_expense.ExpenseCategories.main_category))
            self.tbl_planned_expenses.setItem(idx, 3, QTableWidgetItem(planned_expense.ExpenseCategories.sub_category))

    def new_planned_expense(self):
        dlg = DlgPlannedExpensesEdit(self.current_account.id, None)
        dlg.exec()
        self.account_selection_changed()

    def edit_planned_expense(self):
        if self.tbl_planned_expenses.selectedItems():
            planned_expense_id = int(self.tbl_planned_expenses.item(self.tbl_planned_expenses.selectedItems()[0].row(), 0).text())
            dlg = DlgPlannedExpensesEdit(self.current_account.id, planned_expense_id)
            dlg.exec()
            self.account_selection_changed()

    def delete_planned_expense(self):
        if self.tbl_planned_expenses.selectedItems():
            planned_expense_id = int(self.tbl_planned_expenses.item(self.tbl_planned_expenses.selectedItems()[0].row(), 0).text())
            self.db.delete_planned_expense(planned_expense_id)
            self.account_selection_changed()
