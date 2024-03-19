import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar
from typing import List, Type

from sqlalchemy import String, Float, Boolean, Integer, DateTime, ForeignKey, create_engine, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from expensestracker import cfg


DB_FILENAME = 'expenses.db'
data_dir = cfg.get_data_dir()
database_path = os.path.join(data_dir, DB_FILENAME)
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

engine = create_engine(f'sqlite:///{database_path}')


class Base(DeclarativeBase):
    pass


class Accounts(Base):
    """ Holds the data for all (bank) accounts, including the settings used for importing data. """
    __tablename__ = 'accounts'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    iban: Mapped[str] = mapped_column(String(32), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    type: Mapped[str] = mapped_column(String(15), nullable=True)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    filetype: Mapped[str] = mapped_column(String(10), nullable=False)
    delimiter: Mapped[str] = mapped_column(String(1), nullable=True)
    quotechar: Mapped[str] = mapped_column(String(1), nullable=True)
    first_data_row: Mapped[int] = mapped_column(Integer, nullable=True)
    encoding: Mapped[str] = mapped_column(String(10), nullable=True)
    col_date: Mapped[int] = mapped_column(Integer, nullable=True)
    col_name: Mapped[int] = mapped_column(Integer, nullable=True)
    col_purpose: Mapped[int] = mapped_column(Integer, nullable=True)
    col_iban: Mapped[int] = mapped_column(Integer, nullable=True)
    col_amount: Mapped[int] = mapped_column(Integer, nullable=True)
    dateformat: Mapped[str] = mapped_column(String(30), nullable=True)
    numberformat: Mapped[str] = mapped_column(String(10), nullable=True)
    include_in_sum: Mapped[bool] = mapped_column(Boolean)


class Expenses(Base):
    """ Represents an expense record with its associated data. Belongs to a given account. """
    __tablename__ = 'account_data'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    purpose: Mapped[str] = mapped_column(String(300), nullable=True)
    iban: Mapped[str] = mapped_column(String(32), nullable=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('expense_categories.id'), nullable=True)
    future: Mapped[bool] = mapped_column(Boolean, nullable=True)
    comment: Mapped[str] = mapped_column(String(200), nullable=True)
    planned_expense_id: Mapped[int] = mapped_column(Integer)


class ExpenseCategories(Base):
    __tablename__ = 'expense_categories'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    main_category: Mapped[str] = mapped_column(String(40))
    sub_category: Mapped[str] = mapped_column(String(40))


class CategoryMappings(Base):
    __tablename__ = 'category_mappings'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    account_field: Mapped[str] = mapped_column(String(20))
    field_value: Mapped[str] = mapped_column(String(40))
    category_id: Mapped[int] = mapped_column(ForeignKey('expense_categories.id'))


class PlannedExpenses(Base):
    __tablename__ = 'planned_expenses'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[float] = mapped_column(ForeignKey('expense_categories.id'), nullable=False)
    frequency: Mapped[int] = mapped_column(Integer)
    day: Mapped[int] = mapped_column(Integer)
    auto_delete: Mapped[bool] = mapped_column(Boolean)
    auto_decrement: Mapped[bool] = mapped_column(Boolean)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean)


Base.metadata.create_all(engine)


class Database:
    """ Class that handles all interactions - queries, inserts, updates, deletes - with the database. """
    def __init__(self):
        self.session = Session(engine)

    def disconnect(self):
        """ Closes the database session created upon object instantiation. """
        self.session.close()

    # Accounts
    def get_all_accounts(self) -> list[Type[Accounts]]:
        """ Returns the data of all accounts in the database. """
        return self.session.query(Accounts).all()

    def get_account_by_id(self, account_id):
        """ Returns all account data for the given id. """
        return self.session.query(Accounts).filter_by(id=account_id).first()

    def upsert_account(self, account: Accounts):
        """ Adds a new or updates an existing account to the database. """
        self.session.add(account)
        self.session.commit()

    def delete_account(self, account_id: int) -> None:
        """ Deletes the given account id from the database. """
        self.session.execute(delete(Accounts).where(Accounts.id == account_id))
        self.session.commit()

    # Expenses
    def get_expenses_for_account(self, account_id):
        """ Returns all expenses for the given account. """
        return self.session.query(Expenses, ExpenseCategories).join(ExpenseCategories, isouter=True).filter_by(
            account_id=account_id).order_by(Expenses.date).all()

    def get_expense_by_id(self, expense_id: int):
        """ Returns the expense details for a given id. """
        return self.session.query(Expenses).filter_by(id=expense_id).first()

    def upsert_expense(self, expense: Expenses) -> None:
        """ Adds a new or updates an existing expense record to the database. """
        try:
            self.session.add(expense)
            self.session.commit()
        except Exception as e:
            print(f'Error add/updating the expense record with id {expense.id} to the database: {e}')

    def insert_expenses(self, expenses: list) -> None:
        """ Inserts all expenses from a given list. """
        self.session.add_all(expenses)
        self.session.commit()

    def delete_expense(self, expense_id: int) -> None:
        """ Deletes the Expenses record with the given id from the db. """
        try:
            self.session.execute(delete(Expenses).where(Expenses.id == expense_id))
            self.session.commit()
        except BaseException as e:
            print(f'Could not delete expense with id {expense_id}: {e}')

    def update_amount_for_expense(self, expense_id: int, new_amount: float):
        """ Updates an existing expense with the given amount. """
        try:
            expense = self.session.query(Expenses).filter_by(id=expense_id).first()
            expense.amount = new_amount
            self.session.add(expense)
            self.session.commit()
        except Exception as e:
            print(f'Error trying to update the amount of expense record with id {expense_id}: {e}')

    def does_expense_record_already_exists(self, new_expense: Expenses) -> bool:
        """ Checks if an expense record with the same data as the given expense already exists in the database. """
        existing_expense = self.session.query(Expenses).filter_by(
            account_id=new_expense.account_id).filter_by(
            date=new_expense.date).filter_by(
            name=new_expense.name).filter_by(
            purpose=new_expense.purpose).filter_by(
            iban=new_expense.iban).filter_by(
            amount=new_expense.amount).all()
        if existing_expense:
            return True
        else:
            return False

    def get_expenses_for_pivot(self, account_id: int, start_date: datetime, end_date: datetime):
        """ Returns the necessary data for the pivot table view. """
        expenses = self.session.query(Expenses, ExpenseCategories).join(ExpenseCategories).filter_by(account_id=account_id).all()
        pivot_data = []
        for expense in expenses:
            if (expense.Expenses.date >= start_date) and (expense.Expenses.date <= end_date):
                expense_date = expense.Expenses.date.strftime('%Y-%m')
                amount = expense.Expenses.amount
                main_category = expense.ExpenseCategories.main_category
                sub_category = expense.ExpenseCategories.sub_category
                if not main_category:
                    main_category = 'Uncategorized'
                    sub_category = 'Uncategorized'
                entry = (expense_date, amount, main_category, sub_category)
                pivot_data.append(entry)
        return pivot_data

    def get_expenses_for_chart(self, account_id: int):
        """ Returns a list of (month of expense, expense amount) for the given account. """
        expenses = self.session.query(Expenses).filter_by(account_id=account_id)
        data = []
        for expense in expenses:
            record = (expense.date.strftime('%Y-%m'), expense.amount)
            data.append(record)
        return data

    def get_balances(self, account_id: int):
        """ Returns the current and month end balance for the given account and all accounts in a tuple of 4 values. """
        current_balance_all = 0
        current_balance_account = 0
        monthend_balance_all = 0
        monthend_balance_account = 0
        today = datetime.now()
        date_month_end = datetime(today.year, today.month, calendar.monthrange(today.year, today.month)[-1])
        accounts = self.get_all_accounts()
        for account in accounts:
            starting_balance = account.balance
            expenses = self.get_expenses_for_account(account.id)
            expense_amount_current = sum([row.Expenses.amount for row in expenses if (row.Expenses.date <= datetime.now()) and (not row.Expenses.future)])
            expense_amount_monthend = sum([row.Expenses.amount for row in expenses if row.Expenses.date <= date_month_end])
            current_balance_all = current_balance_all + starting_balance + expense_amount_current
            monthend_balance_all = monthend_balance_all + starting_balance + expense_amount_monthend
            if account.id == account_id:
                current_balance_account = starting_balance + expense_amount_current
                monthend_balance_account = starting_balance + expense_amount_monthend
        return round(current_balance_all, 2), round(current_balance_account, 2), round(monthend_balance_all, 2), round(monthend_balance_account, 2)

    # Categories
    def get_categories_for_account(self, account_id: int) -> List[Type[ExpenseCategories]] | None:
        """ Returns a list of all categories for the given account id. """
        return self.session.query(ExpenseCategories).filter_by(account_id=account_id).order_by(
                ExpenseCategories.main_category).all()

    def get_category_by_id(self, category_id: int) -> ExpenseCategories | None:
        """ Returns the expense category data for the given id. """
        return self.session.query(ExpenseCategories).filter_by(id=category_id).first()

    def upsert_category(self, new_category: ExpenseCategories) -> None:
        """ Adds a new or updates an exisitng Expense Category. """
        try:
            self.session.add(new_category)
            self.session.commit()
        except BaseException as e:
            print(f'Error adding or updating the expense category with id {new_category.id}: {e}')

    def delete_category(self, category_id: int):
        """ Deletes the expense category with the given id. """
        try:
            self.session.execute(delete(ExpenseCategories).where(ExpenseCategories.id == category_id))
            self.session.commit()
        except BaseException as e:
            print(f'Error deleting the expense category with id {category_id}: {e}')

    # Category Mappings
    def get_category_mappings_for_account(self, account_id: int) -> List:
        """ Returns a list of all category mappings for the given account. """
        return self.session.query(CategoryMappings, ExpenseCategories).join(ExpenseCategories).filter_by(
                account_id=account_id).all()

    def upsert_category_mapping(self, category_mapping: CategoryMappings) -> None:
        """ Adds a new category mapping or updates an existing one. """
        self.session.add(category_mapping)
        self.session.commit()

    def delete_category_mapping(self, mapping_id: int) -> None:
        """ Deletes the category mapping with the given ID. """
        self.session.execute(delete(CategoryMappings).where(CategoryMappings.id == mapping_id))
        self.session.commit()

    def get_category_mapping_by_id(self, mapping_id: int) -> CategoryMappings | None:
        """ Returns the category mapping for the given ID. """
        return self.session.query(CategoryMappings).filter_by(id=mapping_id).first()

    def get_mapped_category(self, expense, category_mappings):
        field_match = {'name': expense.name, 'iban': expense.iban, 'purpose': expense.purpose}
        mapped_category = None
        for category_mapping in category_mappings:
            expense_data = field_match[category_mapping.account_field]
            if expense_data.lower().find(category_mapping.field_value.lower()) > -1:
                mapped_category = category_mapping.category_id
                break
            if not mapped_category:
                mapped_category = -1
        return mapped_category

    def get_category_mapping_for_expense(self, expense: Expenses) -> int:
        """ Returns the expense category id matching the given expense. """
        category_mappings = self.session.query(CategoryMappings).filter_by(account_id=expense.account_id)
        mapped_category_id = self.get_mapped_category(expense, category_mappings)
        return mapped_category_id

    # Planned Expenses
    def get_planned_expenses_for_account(self, account_id: int):
        """ Returns a list of all planned expenses. """
        return self.session.query(PlannedExpenses, ExpenseCategories).join(ExpenseCategories).filter_by(account_id=account_id).all()

    def get_all_planned_expenses(self):
        """ Returns all entries for planned expenses. """
        return self.session.query(PlannedExpenses).filter_by(active=True)

    def get_planned_expense_for_id(self, planned_expense_id: int) -> PlannedExpenses | None:
        """ Returns the Planned Expense of the given id. """
        return self.session.query(PlannedExpenses).filter_by(id=planned_expense_id).first()

    def upsert_planned_expense(self, planned_expense):
        """ Adds a new or changes an existing planned expense records to the database. """
        self.session.add(planned_expense)
        self.session.commit()

    def delete_planned_expense(self, planned_expense_id: int) -> None:
        """ Deletes the given account id from the database. """
        self.session.execute(delete(PlannedExpenses).where(PlannedExpenses.id == planned_expense_id))
        self.session.commit()

    def does_planned_expense_exist(self, account_id: int, planned_expense_id: int, expense_date: datetime) -> bool:
        """ Returns True if a planned expense already exists for the given account, planned_expense_id and at the given date. """
        planned_expense = self.session.query(Expenses).filter_by(account_id=account_id).filter_by(
                planned_expense_id=planned_expense_id, date=expense_date).all()
        return bool(len(planned_expense))

    def get_matching_planned_expense(self, new_expense: Expenses):
        """ Checks if a planned expense exists that matches the new real expense new_expense.
        Matches if a planned expense exists in the same month, under the same category and with the same amount. """
        min_date = datetime(year=new_expense.date.year, month=new_expense.date.month, day=1)
        max_date = min_date + relativedelta(months=1) - relativedelta(days=1)
        matching_planned_expense = self.session.query(Expenses).filter_by(
            category_id=new_expense.category_id).filter_by(
            amount=new_expense.amount).filter(
            Expenses.date >= min_date).filter(
            Expenses.date <= max_date).filter(
            Expenses.planned_expense_id.is_not(None)
        ).first()
        return matching_planned_expense

    def get_matching_decrementing_planned_expense(self, new_expense: Expenses):
        """ Checks if a planned expense exists that matches the new real expense and is flagged as auto-decrementing.
        Matches if the planned expense exists in the same month and under the same category.auto_decrement must be True. """
        min_date = datetime(year=new_expense.date.year, month=new_expense.date.month, day=1)
        max_date = min_date + relativedelta(months=1) - relativedelta(days=1)
        with Session(engine) as session:
            matching_planned_expense = session.query(Expenses).filter_by(
                category_id=new_expense.category_id).filter(
                Expenses.date >= min_date).filter(
                Expenses.date <= max_date).filter(
                Expenses.planned_expense_id.is_not(None)).first()
            if matching_planned_expense:
                planned_expense = session.query(PlannedExpenses).filter_by(id=matching_planned_expense.planned_expense_id).filter_by(auto_decrement=True).first()
                if planned_expense:
                    return matching_planned_expense
                else:
                    return None
            else:
                return None
