import sys
import warnings
from datetime import datetime
from dateutil.relativedelta import relativedelta

from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QFileDialog, QTableWidgetItem, QTabWidget
from PyQt6.QtCore import QSize, Qt
import pandas
import numpy
import qdarkstyle

from ui import ui_mainwin, DlgAccountManager, DlgCategoryManager, DlgCategoryMapping, DlgPlannedExpenses, DlgAbout
from expensestracker import importer, cfg, mpl
from expensestracker.database import Database, Expenses

__version__ = 'v20240318'
warnings.simplefilter(action='ignore', category=FutureWarning)


class MainWin(QMainWindow, ui_mainwin.Ui_mainwin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Additional UI setup
        self.resize(QSize(int(cfg.get_value('mainwin', 'width')), int(cfg.get_value('mainwin', 'height'))))
        self.spn_amount.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.dat_expense_date.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tabwidget.setTabPosition(QTabWidget.TabPosition.West)

        column_widths = [20, 80, 250, 400, 170, 80, 150, 150, 250]
        for idx, width in enumerate(column_widths):
            self.tbl_expenses.setColumnWidth(idx, width)
        # Hide the id and future columns
        self.tbl_expenses.setColumnHidden(0, True)
        self.tbl_expenses.setColumnHidden(9, True)
        self.tbl_expenses.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_expenses.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_pivot.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_pivot.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_pivot.setAlternatingRowColors(True)

        # Set date range for pivot to current year
        self.dat_pivot_datefrom.setDate(datetime(datetime.now().year, 1, 1))
        self.dat_pivot_dateto.setDate(datetime(datetime.now().year, 12, 31))

        self.chart_canvas = mpl.MPLCanvas(self, width=10, height=7, dpi=100)
        self.chart_layout.addChildWidget(self.chart_canvas)

        # Variable initialisation
        self.db = Database()
        self.accounts = self.db.get_all_accounts()
        self.current_account_id = self.get_current_account_id()
        self.expenses = None
        self.expense_categories = None
        self.expense_categories_mapping = []
        self.current_expense = None
        self.current_account = None
        self.current_index = None

        for account in self.accounts:
            self.cmb_accounts.addItem(account.name)

        # Signals & Slots
        self.tbl_expenses.itemSelectionChanged.connect(self.expense_selection_changed)
        self.actionQuit.triggered.connect(self.quit)
        self.actionAccount_Manager.triggered.connect(self.open_accountmanager)
        self.actionCategory_Manager.triggered.connect(self.open_categorymanager)
        self.actionImport_expenses.triggered.connect(self.import_expenses)
        self.actionCategory_Mappings.triggered.connect(self.open_categorymapping)
        self.actionPlanned_Expenses.triggered.connect(self.open_plannedexpenses)
        self.actionAbout.triggered.connect(self.about_dlg)
        self.cmb_accounts.currentIndexChanged.connect(self.account_selection_changed)
        self.btn_del_record.clicked.connect(self.delete_selected_record)
        self.chk_pivot_show_sub_categories.stateChanged.connect(self.populate_pivot)
        self.btn_new_record.clicked.connect(self.new_record)
        self.btn_save_record.clicked.connect(self.save_record)
        self.btn_pivot_apply.clicked.connect(self.account_selection_changed)

        self.process_planned_expenses()

        self.account_selection_changed()

        self.draw_charts()

    def account_selection_changed(self):
        """ Trigged when the user changes the account selection on the main screen. """
        self.current_account_id = self.get_current_account_id()
        self.current_account = self.db.get_account_by_id(self.current_account_id)
        self.populate_expense_table()
        self.populate_pivot()
        current_balance_all, current_balance_account, monthend_balance_all, monthend_balance_account = self.db.get_balances(self.current_account_id)
        self.txt_current_balance.setText(f'{current_balance_account} €')
        self.txt_month_end_balance.setText(f'{monthend_balance_account} €')
        self.txt_current_balance_all.setText(f'{current_balance_all} €')
        self.txt_month_end_balance_all.setText(f'{monthend_balance_all} €')
        self.update_categories()

    def update_categories(self):
        """ Updates the available expense categories in the expense edit combobox. """
        self.expense_categories = self.db.get_categories_for_account(self.current_account_id)
        self.cmb_category.clear()
        self.expense_categories_mapping = dict()
        for idx, category in enumerate(self.expense_categories):
            self.cmb_category.addItem(' - '.join((category.main_category, category.sub_category)), userData=category.id)
            self.expense_categories_mapping[category.id] = idx

    def expense_selection_changed(self):
        """ Triggered when the user changes the selected row on the list of expenses. Writes the values of the selected
        entry to the edit fields on the screen. """
        try:
            self.enable_edit_fields(True)
            expense_id = int(self.tbl_expenses.item(self.tbl_expenses.selectedItems()[0].row(), 0).text())
            self.current_expense = self.db.get_expense_by_id(expense_id)
            self.dat_expense_date.setDate(self.current_expense.date)
            self.txt_name.setText(self.current_expense.name)
            self.txt_purpose.setPlainText(str(self.current_expense.purpose))
            self.txt_iban.setText(str(self.current_expense.iban))
            self.spn_amount.setValue(self.current_expense.amount)
            self.txt_comment.setPlainText(str(self.current_expense.comment))
            self.chk_future.setChecked(self.current_expense.future)
            self.cmb_category.setCurrentIndex(self.expense_categories_mapping[self.current_expense.category_id])
            self.btn_save_record.setEnabled(True)
            self.btn_del_record.setEnabled(True)
        except BaseException as e:
            print(f'Error loading record for editing: {e}')

    def enable_edit_fields(self, set_to_enabled: bool):
        """ Enable the fields for editing or creating a new expense record."""
        self.txt_name.setEnabled(set_to_enabled)
        self.txt_iban.setEnabled(set_to_enabled)
        self.txt_purpose.setEnabled(set_to_enabled)
        self.txt_comment.setEnabled(set_to_enabled)
        self.spn_amount.setEnabled(set_to_enabled)
        self.dat_expense_date.setEnabled(set_to_enabled)
        self.chk_future.setEnabled(set_to_enabled)
        self.cmb_category.setEnabled(set_to_enabled)

    def new_record(self):
        """ Initialize the edit fields for creation of new expense record. """
        self.enable_edit_fields(True)
        self.tbl_expenses.clearSelection()
        self.txt_name.clear()
        self.txt_iban.clear()
        self.txt_purpose.clear()
        self.txt_comment.clear()
        self.spn_amount.setValue(0)
        self.dat_expense_date.setDate(datetime.now())
        self.chk_future.setChecked(False)
        self.current_expense = None

    def save_record(self):
        """ Saves the edited or newly created expense record. """
        if self.current_expense:
            self.current_index = self.save_edited_record()
        else:
            self.save_new_record()
        self.account_selection_changed()
        self.new_record()

    def save_new_record(self):
        """ Save a new record to the database. """
        expense = Expenses()
        expense.account_id = self.current_account_id
        expense.name = self.txt_name.text()
        expense.iban = self.txt_iban.text()
        expense.purpose = self.txt_purpose.toPlainText()
        expense.comment = self.txt_comment.toPlainText()
        expense.amount = self.spn_amount.value()
        expense.date = self.dat_expense_date.date().toPyDate()
        expense.category_id = self.cmb_category.itemData(self.cmb_category.currentIndex())
        expense.future = self.chk_future.isChecked()
        self.db.upsert_expense(expense)

    def save_edited_record(self):
        """ Save the changes to an edited record to the database. """
        expense = self.current_expense
        expense.name = self.txt_name.text()
        expense.iban = self.txt_iban.text()
        expense.purpose = self.txt_purpose.toPlainText()
        expense.comment = self.txt_comment.toPlainText()
        expense.amount = self.spn_amount.value()
        expense.date = self.dat_expense_date.date().toPyDate()
        expense.category_id = self.cmb_category.itemData(self.cmb_category.currentIndex())
        expense.future = self.chk_future.isChecked()
        current_idx = self.tbl_expenses.currentIndex()
        self.db.upsert_expense(expense)
        return current_idx

    def delete_selected_record(self):
        expense_id = self.current_expense.id
        self.db.delete_expense(expense_id)
        self.account_selection_changed()

    def get_current_account_id(self):
        """ Returns the account id of the account that is currently selected on the main screen. """
        return self.accounts[self.cmb_accounts.currentIndex()].id

    def scroll_to_current_date(self):
        """ Scrolls the expense table to the first item that is of a later date than today, or to the last item. """
        today = datetime.today()
        item = None
        for row_idx in range(self.tbl_expenses.rowCount()):
            exp_date = datetime.strptime(self.tbl_expenses.item(row_idx, 1).text(), '%Y-%m-%d')
            if exp_date > today:
                item = self.tbl_expenses.item(row_idx, 1)
                break
        if item:
            self.tbl_expenses.scrollToItem(item)
        else:
            self.tbl_expenses.scrollToBottom()

    def import_get_importdata(self):
        """ Opens the open file dialog for import of expense files, reads the data and returns it. """
        # import_def = database.get_importdef(self.get_current_account_id())
        import_def = self.db.get_account_by_id(self.get_current_account_id())
        import_data = None
        if import_def.filetype == 'CSV':
            filename = QFileDialog.getOpenFileName(self, 'Select the expenses file to import...', '.', '*.csv')
            if filename[0]:
                imp = importer.ImporterCSV(filename[0], import_def)
                import_data = imp.parse_data()
        elif import_def.filetype == 'Excel':
            filename = QFileDialog.getOpenFileName(self, 'Select the expenses file to import...', '.', '*.xlsx')
            if filename[0]:
                imp = importer.ImporterExcel(filename[0], import_def)
                import_data = imp.parse_data()
        return import_data

    def import_expenses(self):
        """ Imports the expenses from the user opened file. Applies the following logic:
        - Adds the category id according to the category mapping rules, otherwise applies the standard 'Uncategorized' category
        - Only imports the new expense if it is not a duplicate of an already existing one.
        - Checks if a planned expense exists that matches the imported expense, and deletes the planned expense.
        - Checks if a planned expense with auto-decrement exists that matches the imported expense and decrements the amount or deletes the planned expense if the amount is depleted.
        """
        # TODO: Change order here - duplication check should come second (after categorization), and the other logic should only run if no duplicate is detected
        import_data = self.import_get_importdata()
        imported_expenses = 0
        skipped_duplicates = 0
        deleted_planned_expenses = 0
        if import_data:
            expenses_data_import = []
            for entry in import_data:
                new_expense_entry = Expenses(
                    account_id=entry['account_id'], date=entry['date'],
                    name=entry['name'], purpose=entry['purpose'],
                    iban=entry['iban'], amount=entry['amount'],
                    comment='', category_id=-1, future=False
                )
                # Get category according to the defined category mapping
                category_id = self.db.get_category_mapping_for_expense(new_expense_entry)
                if category_id:
                    new_expense_entry.category_id = category_id
                # Check if a planned expense matches this new expense, and if it does, delete it.
                matching_planned_expense = self.db.get_matching_planned_expense(new_expense_entry)
                if matching_planned_expense:
                    self.db.delete_expense(matching_planned_expense.id)
                    deleted_planned_expenses = deleted_planned_expenses + 1
                # Check if a planned expense with auto decrement exists, and if does, decrement the amount by the
                # amount of the new expense, or delete the planned expense if the amount reaches 0 or below.
                matching_planned_decrementing_expense = self.db.get_matching_decrementing_planned_expense(new_expense_entry)
                if matching_planned_decrementing_expense:
                    new_amount = matching_planned_decrementing_expense.amount - new_expense_entry.amount
                    if new_amount >= 0:
                        self.db.delete_expense(matching_planned_decrementing_expense.id)
                    else:
                        self.db.update_amount_for_expense(matching_planned_decrementing_expense.id, new_amount)
                if not self.db.does_expense_record_already_exists(new_expense_entry):
                    expenses_data_import.append(new_expense_entry)
                    imported_expenses = imported_expenses + 1
                else:
                    skipped_duplicates = skipped_duplicates + 1
                self.db.insert_expenses(expenses_data_import)
        self.account_selection_changed()
        self.statusbar.showMessage(f'{imported_expenses} new expenses were imported, {skipped_duplicates} duplicates were skipped, {deleted_planned_expenses} planned expense were replaced...')

    def populate_expense_table(self):
        """ Populates the expenses table with the data for the given account id.
        Scrolls to the given index if given, otherwise scrolls to the last entry. """
        self.tbl_expenses.clearContents()
        self.expenses = self.db.get_expenses_for_account(self.get_current_account_id())
        self.tbl_expenses.setRowCount(len(self.expenses))
        planned_expense_color = QColor(20, 68, 105)
        for idx, row in enumerate(self.expenses):
            self.tbl_expenses.setItem(idx, 0, QTableWidgetItem(str(row.Expenses.id)))
            self.tbl_expenses.setItem(idx, 1, QTableWidgetItem(row.Expenses.date.strftime("%Y-%m-%d")))
            self.tbl_expenses.setItem(idx, 2, QTableWidgetItem(row.Expenses.name))
            self.tbl_expenses.setItem(idx, 3, QTableWidgetItem(row.Expenses.purpose))
            self.tbl_expenses.setItem(idx, 4, QTableWidgetItem(row.Expenses.iban))
            self.tbl_expenses.setItem(idx, 5, QTableWidgetItem(f"{row.Expenses.amount} €"))
            self.tbl_expenses.setItem(idx, 6, QTableWidgetItem(row.ExpenseCategories.main_category))
            self.tbl_expenses.setItem(idx, 7, QTableWidgetItem(row.ExpenseCategories.sub_category))
            self.tbl_expenses.setItem(idx, 8, QTableWidgetItem(f'{row.Expenses.comment}'))
            self.tbl_expenses.setItem(idx, 9, QTableWidgetItem(str(row.Expenses.future)))
            # Set a different background colour for planned future expenses
            if row.Expenses.future:
                for col in range(self.tbl_expenses.columnCount()):
                    self.tbl_expenses.item(idx, col).setBackground(planned_expense_color)
        if self.current_index:
            self.tbl_expenses.scrollTo(self.current_index)
        else:
            self.scroll_to_current_date()

    def populate_pivot(self):
        """ Populates the pivot table with the data from the selected account id, within the
        limits of the given start and end date. Displays the main+sub categories or only the main categories
        depending on the setting in the UI. """
        start_date = self.dat_pivot_datefrom.dateTime()
        end_date = self.dat_pivot_dateto.dateTime()
        self.tbl_pivot.clear()
        pivotdata = self.db.get_expenses_for_pivot(self.get_current_account_id(), start_date, end_date)
        if pivotdata:
            df = pandas.DataFrame.from_records(pivotdata, columns=['Month', 'Amount', 'Main Category', 'Sub Category'])
            if self.chk_pivot_show_sub_categories.isChecked():
                pivot = df.pivot_table(values=['Amount'], index=['Main Category', 'Sub Category'], columns=['Month'],
                                       aggfunc=numpy.sum, margins=True, fill_value=0)
            else:
                pivot = df.pivot_table(values=['Amount'], index=['Main Category'], columns=['Month'],
                                       aggfunc=numpy.sum, margins=True, fill_value=0)
            pivot_records = pivot.to_records()
            # Collect the column headers for the pivot table
            data_columns = pivot.columns.to_list()
            columns = ['Main Category']
            if self.chk_pivot_show_sub_categories.isChecked():
                columns.append('Sub Category')
            for data_column in data_columns:
                columns.append(data_column[1])
            self.tbl_pivot.setColumnCount(len(columns))
            self.tbl_pivot.setHorizontalHeaderLabels(columns)
            # Hide the sum column
            self.tbl_pivot.setRowCount(len(pivot_records))
            for idx_row, row in enumerate(pivot_records):
                for idx_col, col in enumerate(row):
                    if (self.chk_pivot_show_sub_categories.isChecked() and idx_col > 1) or (not self.chk_pivot_show_sub_categories.isChecked() and idx_col > 0):
                        text = f'{row[idx_col]:.02f} €'
                    else:
                        text = f'{row[idx_col]}'
                    item = QTableWidgetItem(text)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    self.tbl_pivot.setItem(idx_row, idx_col, item)

    def get_earliest_new_planned_expense_date(self, start_date_expense: datetime, day_of_month: int):
        """ Returns the earliest next date for the next entry of a planned expense.
        If the overall start date for the planned expense (as per the configuration) is in the future, the first day of the planned expense is that overall start date
        (using the day_of_month instead of the day of the start date. Otherwise the next date is either in this month (if day_of_month is still in the future or today)
        or in the next month from today. """
        today = datetime.today()
        if start_date_expense > today:
            next_planned_expense_date = datetime(start_date_expense.year, start_date_expense.month, day_of_month)
        else:
            if datetime(start_date_expense.year, start_date_expense.month, day_of_month) >= today:
                next_planned_expense_date = datetime(today.year, today.month, day_of_month)
            else:
                next_planned_expense_date = datetime(today.year, today.month, day_of_month) + relativedelta(months=1)
        return next_planned_expense_date

    def process_planned_expenses(self):
        """ Creates entries for planned expenses where they are missing. """
        added_planned_expenses = 0
        planned_expenses = self.db.get_all_planned_expenses()
        for planned_expense in planned_expenses:
            next_planned_expense_date = self.get_earliest_new_planned_expense_date(planned_expense.start_date, planned_expense.day, )
            for num_planned_months in range(int(cfg.get_value('general', 'planned_expenses_months'))):
                planned_expense_date = next_planned_expense_date + relativedelta(months=num_planned_months)
                expense_exists = self.db.does_planned_expense_exist(account_id=planned_expense.account_id, planned_expense_id=planned_expense.id, expense_date=planned_expense_date)
                if not expense_exists:
                    planned_expense_entry = Expenses(
                        account_id=planned_expense.account_id,
                        date=planned_expense_date,
                        name=planned_expense.name,
                        purpose='',
                        iban='',
                        amount=planned_expense.amount,
                        category_id=planned_expense.category_id,
                        future=True,
                        comment='',
                        planned_expense_id=planned_expense.id
                    )
                    self.db.upsert_expense(planned_expense_entry)
                    added_planned_expenses = added_planned_expenses + 1
        self.account_selection_changed()
        if added_planned_expenses:
            self.statusbar.showMessage(f'Added {added_planned_expenses} new planned expenses...')

    def draw_charts(self):
        data = self.db.get_expenses_for_chart(1)
        df = pandas.DataFrame.from_records(data, columns=['Month', 'Amount'])
        pivot = df.pivot_table(values=['Amount'], columns=['Month'], aggfunc=numpy.sum)
        self.chart_canvas.axes.plot(pivot)

    def open_accountmanager(self):
        dlg = DlgAccountManager.DlgAccountManager()
        dlg.exec()

    def open_categorymanager(self):
        dlg = DlgCategoryManager.DlgCategoryManager()
        dlg.exec()

    def open_categorymapping(self):
        dlg = DlgCategoryMapping.DlgCategoryMapping()
        dlg.exec()

    def open_plannedexpenses(self):
        dlg = DlgPlannedExpenses.DlgPlannedExpenses()
        dlg.exec()

    def about_dlg(self):
        dlg = DlgAbout.DlgAbout(__version__)
        dlg.exec()

    def quit(self):
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6'))
    app_icon = QIcon()
    app_icon.addFile(r'res\app.ico', QSize(64, 64))
    app.setWindowIcon(app_icon)
    win = MainWin()
    win.show()
    app.exec()
