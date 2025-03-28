import sys
import PySide6.QtCore
from PySide6.QtWidgets import QDialog, QApplication
from ui.AuthorizationDialog import Ui_AuthorizationDiolog

class Admitistrator(QDialog):
    def __init__(self):
        super(Admitistrator, self).__init__()
        self.admin_ui = Ui_AuthorizationDiolog()
        self.admin_ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Admitistrator()
    window.show()
    sys.exit(app.exec())