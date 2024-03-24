from PyQt6.QtWidgets import QDialog

from ui.ui_settings import Ui_dlg_settings
from expensestracker import cfg


class DlgSettings(QDialog, Ui_dlg_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cfg = cfg.Config()
        self.chk_archive.setChecked(int(self.cfg.get_value('general', 'archive_imported_files')))
        self.chk_duplicate_check.setChecked(int(self.cfg.get_value('general', 'duplicates_check')))
        self.spn_months_planned.setValue(int(self.cfg.get_value('general', 'planned_expenses_months')))

        self.btn_save.clicked.connect(self.save)
        self.btn_cancel.clicked.connect(self.hide)

    def save(self):
        self.cfg.set_value('general', 'archive_imported_files', str(int(self.chk_archive.isChecked())))
        self.cfg.set_value('general', 'duplicates_check', str(int(self.chk_duplicate_check.isChecked())))
        self.cfg.set_value('general', 'planned_expenses_months', str(self.spn_months_planned.value()))
        self.cfg.save_config()
        self.hide()
