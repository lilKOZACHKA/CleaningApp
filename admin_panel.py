import sys
from PySide6.QtGui import QTabletEvent, QInputEvent
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QDialog, QWidget, QTableWidgetItem, QTableWidget
from dialogs.ui_AdminDialog import Ui_AdminDialog
from dialogs.ui_IncorrectPassDialog import Ui_IncorrectPassDialog
from dialogs.ui_SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from dialogs.ui_ConfirmDelUserDialog import Ui_ConfirmDelUserDialog
from dialogs.ui_AddUserDialog import Ui_AddUserDialog
from dialogs.ui_ChangeUserDialog import Ui_ChangeUserDialog

class AdminPanel(QDialog):
    def __init__(self):
        super(AdminPanel, self).__init__()
        self.admin_ui = Ui_AdminDialog()
        self.admin_ui.setupUi(self)

        self.admin_ui.add_new_user_button.clicked.connect(lambda: self.add_new_user_dialog())
        self.admin_ui.del_user_button.clicked.connect(lambda: self.del_user_dialog())
        self.admin_ui.change_user_button.clicked.connect(lambda: self.change_user_dialog())
        self.admin_ui.refresh_tablet_button.clicked.connect(lambda: self.upload_data())

        self.upload_data()

    def upload_data(self):
        import sqlite3
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        query = "SELECT * FROM Accounts"
        result = cur.execute(query)

        self.admin_ui.tableWidget.setRowCount(0)
        for r_num, r_data in enumerate(result):
            self.admin_ui.tableWidget.insertRow(r_num)
            for col_num, data in enumerate(r_data):
                self.admin_ui.tableWidget.setItem(r_num, col_num, QTableWidgetItem(str(data)))

    def add_new_user_dialog(self):
        add_user_window = QWidget()
        ui = Ui_AddUserDialog()
        ui.setupUi(add_user_window)

        ui.change_user_button.clicked.connect(lambda: self.add_new_user_data(ui))

        add_user_window.show()
        add_user_window.exec()
    
    def add_new_user_data(self, ui):
        from handler_db import Handler
        hand = Handler()
        username = ui.new_username_input.toPlainText()
        passw = ui.new_password_input.toPlainText()
        role = ui.new_role_input.toPlainText()

        status_code = 0

        status_code = hand.key_add_new_user(username, passw, role)

        if status_code == 0:
            self.success_dialog('Пользователь добавлен')
            self.del_user_data()
            self.upload_data()
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        if status_code == 2:
            self.incorrect_dialog("Пароль должен содержать 8 и более символов")
        if status_code == 3:
            self.incorrect_dialog("Имя должно входить в диапозон от 4 до 49 символов")
        self.del_user_data()
        self.upload_data()
    def change_user_dialog(self):
        change_window = QWidget()
        ui = Ui_ChangeUserDialog()
        ui.setupUi(change_window)

        ui.change_user_button.clicked.connect(lambda: self.change_user_data(ui))

        change_window.show()
        change_window.exec()

    def change_user_data(self, ui):
        from handler_db import Handler
        hand = Handler()
        id = self.admin_ui.tableWidget.currentRow() + 1
        username = ui.new_username_input.toPlainText()
        passw = ui.new_password_input.toPlainText()
        role = ui.new_role_input.toPlainText()
        status = ui.new_status_input.toPlainText()
        status_code = 0

        status_code = hand.key_change_current_user(id, username, passw, role, status)

        if status_code == 0:
            self.success_dialog('Пользователь добавлен')
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        if status_code == 2:
            self.incorrect_dialog("Пароль должен содержать 8 и более символов")
        if status_code == 3:
            self.incorrect_dialog("Имя должно входить в диапозон от 4 до 49 символов")

    def del_user_dialog(self):
        self.del_window = QWidget()
        ui = Ui_ConfirmDelUserDialog()
        ui.setupUi(self.del_window)

        ui.confirm_button.clicked.connect(lambda: self.del_user_data())
        ui.cancel_button.clicked.connect(lambda:  self.del_window.close())

        self.del_window.show()
        self.del_window.exec()
    
    def del_user_data(self):
        from handler_db import Handler
        hand = Handler()
        id = self.admin_ui.tableWidget.currentRow() + 1
        status_code = 0

        status_code = hand.key_del_current_user(id)

        if status_code == 0:
            self.success_dialog('Пользователь удалён')
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        self.upload_data()
        self.del_window.close()
    def incorrect_dialog(self, massage):
        incorrect_window = QWidget()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(incorrect_window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: incorrect_window.close())

        self.upload_data()

        incorrect_window.show()
        incorrect_window.exec()

    def success_dialog(self, massage):
        success_window = QWidget()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(success_window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: success_window.close())

        self.upload_data()

        success_window.show()
        success_window.exec()