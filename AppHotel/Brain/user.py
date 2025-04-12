from PySide6.QtWidgets import QDialog
from AppHotel.UI.ChangePassDialog import Ui_ChangePassDialog
from AppHotel.UI.IncorrectPassDialog import Ui_IncorrectPassDialog
from AppHotel.UI.SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from AppHotel.UI.UserDialog import Ui_Dialog


class UserPanel(QDialog):
    def __init__(self):
        super(UserPanel, self).__init__()
        self.main_ui = Ui_Dialog()
        self.main_ui.setupUi(self)
        self.change_pass_dialog = QDialog()
        self.change_pass_ui = Ui_ChangePassDialog()
        self.change_pass_ui.setupUi(self.change_pass_dialog)
        self.main_ui.change_pass_button.clicked.connect(self.show_change_pass_dialog)
        self.change_pass_ui.change_pass_button.clicked.connect(self.change_password)

    def show_change_pass_dialog(self):

        self.change_pass_dialog.show()

    def change_password(self):
        from Handle import Handler
        hand = Handler()
        old_passw = self.change_pass_ui.old_password_input.toPlainText()
        new_passw = self.change_pass_ui.new_password_input.toPlainText()
        conf_new_passw = self.change_pass_ui.validate_password_input.toPlainText()

        if new_passw != old_passw:
            if len(new_passw) >= 8:
                if new_passw == conf_new_passw:
                    status_code = hand.key_change_user_password(old_passw, new_passw, conf_new_passw)
                    if status_code == 3:
                        self.incorrect_dialog("Старый пароль не совпадает, проверьте его")
                    if status_code == 2:
                        self.incorrect_dialog("Проверьте новый пароль в двух последних полях")
                    if status_code == 1:
                        self.success_dialog("Вы успешно сменили пароль!")
                        self.change_pass_dialog.close()  # Закрываем диалог после успешной смены
                else:
                    self.incorrect_dialog("Проверьте новый пароль в двух последних полях")
            else:
                self.incorrect_dialog("Пароль должен быть больше или равен 8 символам")
        else:
            self.incorrect_dialog("Старый пароль совпадает с новым, введите новый пароль")

    @staticmethod
    def incorrect_dialog(message):
        window = QDialog()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(window)

        ui.label.setText(message)
        ui.confirm_button.clicked.connect(window.close)

        window.show()
        window.exec()

    @staticmethod
    def success_dialog(message):
        window = QDialog()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(window)

        ui.label.setText(message)
        ui.confirm_button.clicked.connect(window.close)

        window.show()
        window.exec()
