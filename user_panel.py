import sys
import PySide6.QtCore
from PySide6.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from dialogs.ui_ChangePassDialog import Ui_ChangePassDialog
from dialogs.ui_IncorrectPassDialog import Ui_IncorrectPassDialog
from dialogs.ui_SuccessAutorizeDialog import Ui_SuccessAutorizeDialog

class UserPanel(QDialog):
    def __init__(self):
        super(UserPanel, self).__init__()
        self.user_ui = Ui_ChangePassDialog()
        self.user_ui.setupUi(self)

        self.user_ui.change_pass_button.clicked.connect(lambda: self.change_password())

    def change_password(self):
        from handler_db import Handler
        hand = Handler()
        old_passw = self.user_ui.old_password_input.toPlainText()
        new_passw = self.user_ui.new_password_input.toPlainText()
        conf_new_passw = self.user_ui.validate_password_input.toPlainText()
        status_code = 0

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
                else:
                    self.incorrect_dialog("Проверьте новый пароль в двух последних полях")
            else:
                self.incorrect_dialog("Пароль должен быть больше или равен 8 символам")
        else:
            self.incorrect_dialog("Старый пароль совпадает с новым, введите новый пароль")
    
    def incorrect_dialog(self, massage):
        window = QWidget()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()

    def success_dialog(self, massage):
        window = QWidget()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: window.close())

        window.show()
        window.exec()