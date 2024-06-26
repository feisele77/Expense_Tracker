# Form implementation generated from reading ui file '.\dlg_settings.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlg_settings(object):
    def setupUi(self, dlg_settings):
        dlg_settings.setObjectName("dlg_settings")
        dlg_settings.resize(600, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlg_settings.sizePolicy().hasHeightForWidth())
        dlg_settings.setSizePolicy(sizePolicy)
        dlg_settings.setMinimumSize(QtCore.QSize(600, 230))
        dlg_settings.setMaximumSize(QtCore.QSize(600, 230))
        self.chk_archive = QtWidgets.QCheckBox(parent=dlg_settings)
        self.chk_archive.setGeometry(QtCore.QRect(30, 30, 261, 20))
        self.chk_archive.setObjectName("chk_archive")
        self.label = QtWidgets.QLabel(parent=dlg_settings)
        self.label.setGeometry(QtCore.QRect(50, 50, 391, 31))
        self.label.setObjectName("label")
        self.chk_duplicate_check = QtWidgets.QCheckBox(parent=dlg_settings)
        self.chk_duplicate_check.setGeometry(QtCore.QRect(30, 90, 211, 20))
        self.chk_duplicate_check.setObjectName("chk_duplicate_check")
        self.label_2 = QtWidgets.QLabel(parent=dlg_settings)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 381, 31))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.spn_months_planned = QtWidgets.QSpinBox(parent=dlg_settings)
        self.spn_months_planned.setGeometry(QtCore.QRect(30, 170, 42, 22))
        self.spn_months_planned.setMinimum(1)
        self.spn_months_planned.setMaximum(12)
        self.spn_months_planned.setProperty("value", 2)
        self.spn_months_planned.setObjectName("spn_months_planned")
        self.label_3 = QtWidgets.QLabel(parent=dlg_settings)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 341, 16))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(parent=dlg_settings)
        self.line.setGeometry(QtCore.QRect(463, 10, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btn_save = QtWidgets.QPushButton(parent=dlg_settings)
        self.btn_save.setGeometry(QtCore.QRect(490, 20, 91, 24))
        self.btn_save.setObjectName("btn_save")
        self.btn_cancel = QtWidgets.QPushButton(parent=dlg_settings)
        self.btn_cancel.setGeometry(QtCore.QRect(490, 190, 91, 24))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(dlg_settings)
        QtCore.QMetaObject.connectSlotsByName(dlg_settings)

    def retranslateUi(self, dlg_settings):
        _translate = QtCore.QCoreApplication.translate
        dlg_settings.setWindowTitle(_translate("dlg_settings", "Settings"))
        self.chk_archive.setText(_translate("dlg_settings", "Archive imported files"))
        self.label.setText(_translate("dlg_settings", "Stores a copy of the imported file in the data folder of the application"))
        self.chk_duplicate_check.setText(_translate("dlg_settings", "Duplicate check during import"))
        self.label_2.setText(_translate("dlg_settings", "Checks if an expense from an import file already exists in the database, and skips it if it does."))
        self.label_3.setText(_translate("dlg_settings", "Number of months to add planned expenses in advance"))
        self.btn_save.setText(_translate("dlg_settings", "Save"))
        self.btn_cancel.setText(_translate("dlg_settings", "Cancel"))
