import sys, time
from PySide6.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from AppHotel.UI.ui_AutorizationDialog import Ui_AutorizationDiolog
from AppHotel.UI.ui_IncorrectPassDialog import Ui_IncorrectPassDialog
from AppHotel.UI.ui_SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from AppHotel.UI.ui_BanDialog import Ui_BanDialog
from AppHotel.UI.admin_panel import AdminPanel
from AppHotel.UI.user_panel import UserPanel

class Authorization(QDialog):
    def __init__(self):
        super(Authorization, self).__init__()
        self.autorize_ui = Ui_AutorizationDiolog()
        self.autorize_ui.setupUi(self)

        self.autorize_ui.login_button.clicked.connect(lambda: self.validate_user_data())

    def validate_user_data(self):
        from AppHotel.UI.Handle import Handler
        hand = Handler()
        login = self.autorize_ui.login_input.toPlainText()
        passw = self.autorize_ui.password_input.toPlainText()
        status_code = 0

        status_code = hand.key_autorization(login, passw)

        if status_code == 0:
            status_code = hand.key_check_user_type(login)
            self.success_dialog(status_code)
        elif status_code == 1:
            self.incorrect_dialog()
        else:
            self.ban_dialog()

    def incorrect_dialog(self):
        window = QDialog()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(window)

        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()

    def success_dialog(self, status_code):
        window = QDialog()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(window)

        ui.confirm_button.clicked.connect(lambda: self.confirm_and_switch_panel(status_code, window))

        window.show()
        window.exec()

    def ban_dialog(self):
        window = QDialog()
        ui = Ui_BanDialog()
        ui.setupUi(window)

        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()

    def confirm_and_switch_panel(self, status_code, window):
        if status_code == 0:
            self.open_admin_panel(window)
        else:
            self.open_user_panel(window)

    def open_user_panel(self, window):
        window.close()
        user_window = UserPanel()
        user_window.show()
        self.close()
        user_window.exec()

    def open_admin_panel(self, window):
        window.close()
        admin_window = AdminPanel()
        admin_window.show()
        self.close()
        admin_window.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    sys.exit(app.exec())