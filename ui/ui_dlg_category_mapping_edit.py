# Form implementation generated from reading ui file '.\dlg_category_mapping_edit.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlg_category_mappings(object):
    def setupUi(self, dlg_category_mappings):
        dlg_category_mappings.setObjectName("dlg_category_mappings")
        dlg_category_mappings.resize(572, 124)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dlg_category_mappings)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=dlg_category_mappings)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.cmb_fieldname = QtWidgets.QComboBox(parent=dlg_category_mappings)
        self.cmb_fieldname.setObjectName("cmb_fieldname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmb_fieldname)
        self.label_2 = QtWidgets.QLabel(parent=dlg_category_mappings)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txt_matchedtext = QtWidgets.QLineEdit(parent=dlg_category_mappings)
        self.txt_matchedtext.setObjectName("txt_matchedtext")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txt_matchedtext)
        self.label_3 = QtWidgets.QLabel(parent=dlg_category_mappings)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.cmb_categories = QtWidgets.QComboBox(parent=dlg_category_mappings)
        self.cmb_categories.setObjectName("cmb_categories")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cmb_categories)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_save = QtWidgets.QPushButton(parent=dlg_category_mappings)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_2.addWidget(self.btn_save)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(parent=dlg_category_mappings)
        self.btn_cancel.setObjectName("btn_cancel")
        self.verticalLayout_2.addWidget(self.btn_cancel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(dlg_category_mappings)
        QtCore.QMetaObject.connectSlotsByName(dlg_category_mappings)

    def retranslateUi(self, dlg_category_mappings):
        _translate = QtCore.QCoreApplication.translate
        dlg_category_mappings.setWindowTitle(_translate("dlg_category_mappings", "Add/Edit Category Mapping"))
        self.label.setText(_translate("dlg_category_mappings", "Field Name"))
        self.label_2.setText(_translate("dlg_category_mappings", "Matched Text"))
        self.label_3.setText(_translate("dlg_category_mappings", "Mapped Category"))
        self.btn_save.setText(_translate("dlg_category_mappings", "Save"))
        self.btn_cancel.setText(_translate("dlg_category_mappings", "Cancel"))
