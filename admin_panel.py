import sys
import PySide6.QtCore
from PySide6.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from dialogs.ui_AdminDialog import Ui_AdminDialog

class AdminPanel(QDialog):
    def __init__(self):
        super(AdminPanel, self).__init__()
        self.autorize_ui = Ui_AdminDialog()
        self.autorize_ui.setupUi(self)