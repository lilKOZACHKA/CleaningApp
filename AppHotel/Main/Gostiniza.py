import sys
from PySide6.QtWidgets import QDialog, QApplication
from AppHotel.UI.AuthDialog import Ui_AutorizationDiolog
from AppHotel.UI.IncorrectPassDialog import Ui_IncorrectPassDialog
from AppHotel.UI.SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from AppHotel.UI.BanDialog import Ui_BanDialog
from AppHotel.Brain.admin import AdminPanel
from AppHotel.Brain.user import UserPanel


class Authorization(QDialog):
    def __init__(self):
        super(Authorization, self).__init__()
        self.autorize_ui = Ui_AutorizationDiolog()
        self.autorize_ui.setupUi(self)

        self.autorize_ui.login_button.clicked.connect(lambda: self.validate_user_data())

    def validate_user_data(self):
        from AppHotel.Brain.Handle import Handler
        hand = Handler()
        login = self.autorize_ui.login_input.toPlainText()
        passw = self.autorize_ui.password_input.toPlainText()

        status_code = hand.key_autorization(login, passw)

        if status_code == 0:
            status_code = hand.key_check_user_type(login)
            self.success_dialog(status_code)
        elif status_code == 1:
            self.incorrect_dialog()
        else:
            self.ban_dialog()

    @staticmethod
    def incorrect_dialog():
        incorwin = QDialog()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(incorwin)

        ui.confirm_button.clicked.connect(lambda: incorwin.close())

        incorwin.show()
        incorwin.exec()

    def success_dialog(self, status_code):
        successwin = QDialog()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(successwin)

        ui.confirm_button.clicked.connect(lambda: self.confirm_and_switch_panel(status_code, successwin))

        successwin.show()
        successwin.exec()

    @staticmethod
    def ban_dialog():
        banwin = QDialog()
        ui = Ui_BanDialog()
        ui.setupUi(banwin)

        ui.confirm_button.clicked.connect(lambda: banwin.close())

        banwin.show()
        banwin.exec()

    def confirm_and_switch_panel(self, status_code, win):
        if status_code == 0:
            self.open_admin_panel(win)
        else:
            self.open_user_panel(win)

    def open_user_panel(self, win1):
        win1.close()
        user_window = UserPanel()
        user_window.show()
        self.close()
        user_window.exec()

    def open_admin_panel(self, win3):
        win3.close()
        admin_window = AdminPanel()
        admin_window.show()
        self.close()
        admin_window.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    sys.exit(app.exec())
