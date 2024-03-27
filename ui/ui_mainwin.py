# Form implementation generated from reading ui file '.\mainwin.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, QtCharts


class Ui_mainwin(object):
    def setupUi(self, mainwin):
        mainwin.setObjectName("mainwin")
        mainwin.resize(1486, 886)
        self.centralwidget = QtWidgets.QWidget(parent=mainwin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_accounts = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_accounts.setObjectName("lbl_accounts")
        self.horizontalLayout.addWidget(self.lbl_accounts)
        self.cmb_accounts = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cmb_accounts.setMinimumSize(QtCore.QSize(250, 0))
        self.cmb_accounts.setObjectName("cmb_accounts")
        self.horizontalLayout.addWidget(self.cmb_accounts)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_current_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_current_balance.setObjectName("lbl_current_balance")
        self.horizontalLayout.addWidget(self.lbl_current_balance)
        self.txt_current_balance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_current_balance.setMinimumSize(QtCore.QSize(40, 0))
        self.txt_current_balance.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_current_balance.setReadOnly(True)
        self.txt_current_balance.setObjectName("txt_current_balance")
        self.horizontalLayout.addWidget(self.txt_current_balance)
        self.lbl_month_end_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_month_end_balance.setObjectName("lbl_month_end_balance")
        self.horizontalLayout.addWidget(self.lbl_month_end_balance)
        self.txt_month_end_balance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_month_end_balance.setMinimumSize(QtCore.QSize(50, 0))
        self.txt_month_end_balance.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_month_end_balance.setReadOnly(True)
        self.txt_month_end_balance.setObjectName("txt_month_end_balance")
        self.horizontalLayout.addWidget(self.txt_month_end_balance)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.txt_current_balance_all = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_current_balance_all.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_current_balance_all.setReadOnly(True)
        self.txt_current_balance_all.setObjectName("txt_current_balance_all")
        self.horizontalLayout.addWidget(self.txt_current_balance_all)
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.txt_month_end_balance_all = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_month_end_balance_all.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_month_end_balance_all.setReadOnly(True)
        self.txt_month_end_balance_all.setObjectName("txt_month_end_balance_all")
        self.horizontalLayout.addWidget(self.txt_month_end_balance_all)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabwidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabwidget.setObjectName("tabwidget")
        self.tab_expensetable = QtWidgets.QWidget()
        self.tab_expensetable.setObjectName("tab_expensetable")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_expensetable)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tbl_expenses = QtWidgets.QTableWidget(parent=self.tab_expensetable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_expenses.sizePolicy().hasHeightForWidth())
        self.tbl_expenses.setSizePolicy(sizePolicy)
        self.tbl_expenses.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_expenses.setObjectName("tbl_expenses")
        self.tbl_expenses.setColumnCount(9)
        self.tbl_expenses.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_expenses.setHorizontalHeaderItem(8, item)
        self.tbl_expenses.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tbl_expenses)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(parent=self.tab_expensetable)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(80, 25))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.dat_expense_date = QtWidgets.QDateEdit(parent=self.frame)
        self.dat_expense_date.setEnabled(False)
        self.dat_expense_date.setMaximumSize(QtCore.QSize(100, 25))
        self.dat_expense_date.setObjectName("dat_expense_date")
        self.horizontalLayout_5.addWidget(self.dat_expense_date)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spn_amount = QtWidgets.QDoubleSpinBox(parent=self.frame)
        self.spn_amount.setEnabled(False)
        self.spn_amount.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spn_amount.setMinimum(-100000.0)
        self.spn_amount.setMaximum(100000.0)
        self.spn_amount.setObjectName("spn_amount")
        self.horizontalLayout_5.addWidget(self.spn_amount)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.txt_name = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_name.setEnabled(False)
        self.txt_name.setObjectName("txt_name")
        self.horizontalLayout_6.addWidget(self.txt_name)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(120, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.txt_iban = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_iban.setEnabled(False)
        self.txt_iban.setObjectName("txt_iban")
        self.horizontalLayout_7.addWidget(self.txt_iban)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.chk_future = QtWidgets.QCheckBox(parent=self.frame)
        self.chk_future.setEnabled(False)
        self.chk_future.setObjectName("chk_future")
        self.verticalLayout_8.addWidget(self.chk_future)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txt_comment = QtWidgets.QPlainTextEdit(parent=self.frame)
        self.txt_comment.setEnabled(False)
        self.txt_comment.setMinimumSize(QtCore.QSize(0, 70))
        self.txt_comment.setMaximumSize(QtCore.QSize(16777215, 70))
        self.txt_comment.setObjectName("txt_comment")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_comment)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txt_purpose = QtWidgets.QPlainTextEdit(parent=self.frame)
        self.txt_purpose.setEnabled(False)
        self.txt_purpose.setMinimumSize(QtCore.QSize(0, 70))
        self.txt_purpose.setMaximumSize(QtCore.QSize(16777215, 70))
        self.txt_purpose.setObjectName("txt_purpose")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_purpose)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.cmb_category = QtWidgets.QComboBox(parent=self.frame)
        self.cmb_category.setEnabled(False)
        self.cmb_category.setObjectName("cmb_category")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmb_category)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem3)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_new_record = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_record.setObjectName("btn_new_record")
        self.verticalLayout_4.addWidget(self.btn_new_record)
        self.btn_save_record = QtWidgets.QPushButton(parent=self.frame)
        self.btn_save_record.setEnabled(False)
        self.btn_save_record.setObjectName("btn_save_record")
        self.verticalLayout_4.addWidget(self.btn_save_record)
        self.btn_del_record = QtWidgets.QPushButton(parent=self.frame)
        self.btn_del_record.setEnabled(False)
        self.btn_del_record.setObjectName("btn_del_record")
        self.verticalLayout_4.addWidget(self.btn_del_record)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabwidget.addTab(self.tab_expensetable, "")
        self.tab_pivot = QtWidgets.QWidget()
        self.tab_pivot.setObjectName("tab_pivot")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_pivot)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_from_month = QtWidgets.QLabel(parent=self.tab_pivot)
        self.lbl_from_month.setObjectName("lbl_from_month")
        self.horizontalLayout_4.addWidget(self.lbl_from_month)
        self.dat_pivot_datefrom = QtWidgets.QDateEdit(parent=self.tab_pivot)
        self.dat_pivot_datefrom.setObjectName("dat_pivot_datefrom")
        self.horizontalLayout_4.addWidget(self.dat_pivot_datefrom)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_pivot)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.dat_pivot_dateto = QtWidgets.QDateEdit(parent=self.tab_pivot)
        self.dat_pivot_dateto.setObjectName("dat_pivot_dateto")
        self.horizontalLayout_4.addWidget(self.dat_pivot_dateto)
        self.btn_pivot_apply = QtWidgets.QPushButton(parent=self.tab_pivot)
        self.btn_pivot_apply.setObjectName("btn_pivot_apply")
        self.horizontalLayout_4.addWidget(self.btn_pivot_apply)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.chk_pivot_show_sub_categories = QtWidgets.QCheckBox(parent=self.tab_pivot)
        self.chk_pivot_show_sub_categories.setChecked(True)
        self.chk_pivot_show_sub_categories.setObjectName("chk_pivot_show_sub_categories")
        self.horizontalLayout_4.addWidget(self.chk_pivot_show_sub_categories)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tbl_pivot = QtWidgets.QTableWidget(parent=self.tab_pivot)
        self.tbl_pivot.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_pivot.setTabKeyNavigation(False)
        self.tbl_pivot.setProperty("showDropIndicator", False)
        self.tbl_pivot.setDragDropOverwriteMode(False)
        self.tbl_pivot.setAlternatingRowColors(True)
        self.tbl_pivot.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tbl_pivot.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tbl_pivot.setWordWrap(False)
        self.tbl_pivot.setCornerButtonEnabled(False)
        self.tbl_pivot.setObjectName("tbl_pivot")
        self.tbl_pivot.setColumnCount(0)
        self.tbl_pivot.setRowCount(0)
        self.tbl_pivot.horizontalHeader().setVisible(True)
        self.tbl_pivot.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tbl_pivot)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.tabwidget.addTab(self.tab_pivot, "")
        self.tab_charts = QtWidgets.QWidget()
        self.tab_charts.setObjectName("tab_charts")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_charts)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.chart_central_widget = QtWidgets.QWidget(parent=self.tab_charts)
        self.chart_central_widget.setObjectName("chart_central_widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.chart_central_widget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.chart_area = QtWidgets.QVBoxLayout()
        self.chart_area.setObjectName("chart_area")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(parent=self.chart_central_widget)
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.cmb_chart_type = QtWidgets.QComboBox(parent=self.chart_central_widget)
        self.cmb_chart_type.setMinimumSize(QtCore.QSize(500, 0))
        self.cmb_chart_type.setMaximumSize(QtCore.QSize(500, 16777215))
        self.cmb_chart_type.setObjectName("cmb_chart_type")
        self.horizontalLayout_8.addWidget(self.cmb_chart_type)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.chart_area.addLayout(self.horizontalLayout_8)
        self.chart_layout = QtWidgets.QVBoxLayout()
        self.chart_layout.setObjectName("chart_layout")
        self.chartview = QtCharts.QChartView(parent=self.chart_central_widget)
        self.chartview.setObjectName("chartview")
        self.chart_layout.addWidget(self.chartview)
        self.chart_area.addLayout(self.chart_layout)
        self.horizontalLayout_9.addLayout(self.chart_area)
        self.verticalLayout_6.addWidget(self.chart_central_widget)
        self.tabwidget.addTab(self.tab_charts, "")
        self.verticalLayout_2.addWidget(self.tabwidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        mainwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1486, 22))
        self.menubar.setObjectName("menubar")
        self.menuExpenses_Tracker = QtWidgets.QMenu(parent=self.menubar)
        self.menuExpenses_Tracker.setObjectName("menuExpenses_Tracker")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainwin)
        self.statusbar.setObjectName("statusbar")
        mainwin.setStatusBar(self.statusbar)
        self.actionImport_expenses = QtGui.QAction(parent=mainwin)
        self.actionImport_expenses.setObjectName("actionImport_expenses")
        self.actionQuit = QtGui.QAction(parent=mainwin)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAccount_Manager = QtGui.QAction(parent=mainwin)
        self.actionAccount_Manager.setObjectName("actionAccount_Manager")
        self.actionCategory_Manager = QtGui.QAction(parent=mainwin)
        self.actionCategory_Manager.setObjectName("actionCategory_Manager")
        self.actionCategory_Mappings = QtGui.QAction(parent=mainwin)
        self.actionCategory_Mappings.setObjectName("actionCategory_Mappings")
        self.actionSettings = QtGui.QAction(parent=mainwin)
        self.actionSettings.setObjectName("actionSettings")
        self.actionPlanned_Expenses = QtGui.QAction(parent=mainwin)
        self.actionPlanned_Expenses.setObjectName("actionPlanned_Expenses")
        self.actionAbout = QtGui.QAction(parent=mainwin)
        self.actionAbout.setObjectName("actionAbout")
        self.menuExpenses_Tracker.addAction(self.actionImport_expenses)
        self.menuExpenses_Tracker.addSeparator()
        self.menuExpenses_Tracker.addAction(self.actionSettings)
        self.menuExpenses_Tracker.addSeparator()
        self.menuExpenses_Tracker.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionAccount_Manager)
        self.menuSettings.addAction(self.actionCategory_Manager)
        self.menuSettings.addAction(self.actionCategory_Mappings)
        self.menuSettings.addAction(self.actionPlanned_Expenses)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuExpenses_Tracker.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainwin)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainwin)

    def retranslateUi(self, mainwin):
        _translate = QtCore.QCoreApplication.translate
        mainwin.setWindowTitle(_translate("mainwin", "Expenses Tracker"))
        self.lbl_accounts.setText(_translate("mainwin", "Accounts"))
        self.lbl_current_balance.setText(_translate("mainwin", "Current Balance"))
        self.lbl_month_end_balance.setText(_translate("mainwin", "Month End Balance"))
        self.label_9.setText(_translate("mainwin", "Curr. Balance All Accounts"))
        self.label_10.setText(_translate("mainwin", "Month End Balance all Accounts"))
        item = self.tbl_expenses.horizontalHeaderItem(0)
        item.setText(_translate("mainwin", "id"))
        item = self.tbl_expenses.horizontalHeaderItem(1)
        item.setText(_translate("mainwin", "Date"))
        item = self.tbl_expenses.horizontalHeaderItem(2)
        item.setText(_translate("mainwin", "Name"))
        item = self.tbl_expenses.horizontalHeaderItem(3)
        item.setText(_translate("mainwin", "Purpose"))
        item = self.tbl_expenses.horizontalHeaderItem(4)
        item.setText(_translate("mainwin", "IBAN"))
        item = self.tbl_expenses.horizontalHeaderItem(5)
        item.setText(_translate("mainwin", "Amount"))
        item = self.tbl_expenses.horizontalHeaderItem(6)
        item.setText(_translate("mainwin", "Category"))
        item = self.tbl_expenses.horizontalHeaderItem(7)
        item.setText(_translate("mainwin", "Sub Category"))
        item = self.tbl_expenses.horizontalHeaderItem(8)
        item.setText(_translate("mainwin", "Comment"))
        self.label.setText(_translate("mainwin", "Date"))
        self.label_5.setText(_translate("mainwin", "Amount"))
        self.spn_amount.setSuffix(_translate("mainwin", "€"))
        self.label_2.setText(_translate("mainwin", "Name"))
        self.label_7.setText(_translate("mainwin", "IBAN"))
        self.chk_future.setText(_translate("mainwin", "Future Record"))
        self.label_4.setText(_translate("mainwin", "Comment"))
        self.label_3.setText(_translate("mainwin", "Purpose"))
        self.label_6.setText(_translate("mainwin", "Category"))
        self.btn_new_record.setText(_translate("mainwin", "New Record"))
        self.btn_save_record.setText(_translate("mainwin", "Save Record"))
        self.btn_del_record.setText(_translate("mainwin", "Delete Record"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_expensetable), _translate("mainwin", "Expense Data"))
        self.lbl_from_month.setText(_translate("mainwin", "From:"))
        self.label_8.setText(_translate("mainwin", "To:"))
        self.btn_pivot_apply.setText(_translate("mainwin", "Apply"))
        self.chk_pivot_show_sub_categories.setText(_translate("mainwin", "Show Sub Categories"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_pivot), _translate("mainwin", "Summary by Category"))
        self.label_11.setText(_translate("mainwin", "Chart Type "))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_charts), _translate("mainwin", "Charts"))
        self.menuExpenses_Tracker.setTitle(_translate("mainwin", "Expenses Tracker"))
        self.menuSettings.setTitle(_translate("mainwin", "Settings"))
        self.menuHelp.setTitle(_translate("mainwin", "Help"))
        self.actionImport_expenses.setText(_translate("mainwin", "Import expenses..."))
        self.actionQuit.setText(_translate("mainwin", "Quit"))
        self.actionAccount_Manager.setText(_translate("mainwin", "Account Manager"))
        self.actionCategory_Manager.setText(_translate("mainwin", "Category Manager"))
        self.actionCategory_Mappings.setText(_translate("mainwin", "Category Mappings"))
        self.actionSettings.setText(_translate("mainwin", "Settings..."))
        self.actionPlanned_Expenses.setText(_translate("mainwin", "Planned Expenses"))
        self.actionAbout.setText(_translate("mainwin", "About"))
