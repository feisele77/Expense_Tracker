from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QDialog

from ui.ui_about import Ui_dlg_about


class DlgAbout(QDialog, Ui_dlg_about):
    def __init__(self, version):
        super().__init__()
        self.setupUi(self)

        self.lbl_version.setText(f'Version {version}')
        self.txt_browser.setSource(QUrl.fromLocalFile(r'C:\Users\Frank\Python\ExpenseTracker\about.html'))

        self.btn_close.clicked.connect(self.hide)
