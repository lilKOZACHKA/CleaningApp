import sys
import PySide6.QtCore
from PySide6.QtWidgets import QDialog, QApplication, QWidget
from dialogs.ui_AutorizationDialog import Ui_AutorizationDiolog
from dialogs.ui_IncorrectPassDialog import Ui_IncorrectPassDialog
from dialogs.ui_SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from dialogs.ui_BanDialog import Ui_BanDialog

class Authorization(QDialog):
    def __init__(self):
        super(Authorization, self).__init__()
        self.autorize_ui = Ui_AutorizationDiolog()
        self.autorize_ui.setupUi(self)

        self.autorize_ui.login_button.clicked.connect(lambda: self.validate_user_data())

    def validate_user_data(self):
        from handler_db import Handler
        hand = Handler()
        login = self.autorize_ui.login_input.toPlainText()
        passw = self.autorize_ui.password_input.toPlainText()
        status_code = 0

        status_code = hand.key_check_autorization(login, passw)

        if status_code == 0:
           self.success_dialog()
        elif status_code == 1:
            self.incorrect_dialog()
        else:
            self.ban_dialog()

    def incorrect_dialog(self):
        window = QWidget()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(window)

        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()

    def success_dialog(self):
        window = QWidget()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(window)

        window.show()
        window.exec()

    def ban_dialog(self):
        window = QWidget()
        ui = Ui_BanDialog()
        ui.setupUi(window)

        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    sys.exit(app.exec())