from PySide6.QtWidgets import QDialog, QTableWidgetItem

from AppHotel.UI.ui_AddClientDialog import Ui_AddClientDialog
from AppHotel.UI.ui_AdminDialog import Ui_AdminDialog
from AppHotel.UI.ui_IncorrectPassDialog import Ui_IncorrectPassDialog
from AppHotel.UI.ui_SuccessAutorizeDialog import Ui_SuccessAutorizeDialog
from AppHotel.UI.ui_ConfirmDelUserDialog import Ui_ConfirmDelUserDialog
from AppHotel.UI.ui_AddUserDialog import Ui_AddUserDialog
from AppHotel.UI.ui_ChangeUserDialog import Ui_ChangeUserDialog


class AdminPanel(QDialog):
    def __init__(self):
        super(AdminPanel, self).__init__()
        self.del_window = QDialog()
        self.admin_ui = Ui_AdminDialog()
        self.admin_ui.setupUi(self)

        self.add_client_dialog = QDialog()
        self.ui_add_client = Ui_AddClientDialog()
        self.ui_add_client.setupUi(self.add_client_dialog)

        self.admin_ui.add_new_user_button.clicked.connect(lambda: self.add_new_user_dialog())
        self.admin_ui.del_user_button.clicked.connect(lambda: self.del_user_dialog())
        self.admin_ui.change_user_button.clicked.connect(lambda: self.change_user_dialog())
        self.admin_ui.refresh_tablet_button.clicked.connect(lambda: self.upload_data())
        self.admin_ui.add_new_user_button_1.clicked.connect(lambda: self.add_clientuser_dialog())
        self.admin_ui.del_user_button_1.clicked.connect(lambda: self.del_client_dialog())
        self.admin_ui.refresh_tablet_button_1.clicked.connect(lambda: self.upload_data())
        self.upload_data()

    def upload_data(self):
        import sqlite3
        conn = sqlite3.connect('Guest.db')
        cur = conn.cursor()

        query = "SELECT * FROM Accounts"
        result = cur.execute(query).fetchall()

        self.admin_ui.tableWidget.setRowCount(0)
        for r_num, r_data in enumerate(result):
            self.admin_ui.tableWidget.insertRow(r_num)
            for col_num, data in enumerate(r_data):
                self.admin_ui.tableWidget.setItem(r_num, col_num, QTableWidgetItem(str(data)))

        self.ui_add_client.new_id_input.clear()
        cur.execute("SELECT account_id, username FROM Accounts ORDER BY username")
        accounts = cur.fetchall()

        for account_id, username in accounts:
            self.ui_add_client.new_id_input.addItem(f"{username} (ID: {account_id})", userData=account_id)

        query_1 = "SELECT * FROM Clients"
        result_1 = cur.execute(query_1).fetchall()

        self.admin_ui.tableWidget_1.setRowCount(0)
        for r_num, r_data in enumerate(result_1):
            self.admin_ui.tableWidget_1.insertRow(r_num)
            for col_num, data in enumerate(r_data):
                self.admin_ui.tableWidget_1.setItem(r_num, col_num, QTableWidgetItem(str(data)))

        conn.close()

    def add_new_user_dialog(self):
        add_user_window = QDialog()
        ui = Ui_AddUserDialog()
        ui.setupUi(add_user_window)

        ui.change_user_button.clicked.connect(lambda: self.add_new_user_data(ui))

        add_user_window.show()
        add_user_window.exec()

    def add_new_user_data(self, ui):
        from AppHotel.Brain.Handle import Handler

        hand = Handler()
        username = ui.new_username_input.toPlainText()
        passw = ui.new_password_input.toPlainText()
        role = ui.new_role_input.currentText()

        status_code = hand.key_add_new_user(username, passw, role)

        if status_code == 0:
            self.success_dialog('Пользователь добавлен')
            self.upload_data()
            id = self.admin_ui.tableWidget.currentRow() + 1
            status_code = hand.key_del_current_user(id)
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        if status_code == 2:
            self.incorrect_dialog("Пароль должен содержать 8 и более символов")
        if status_code == 3:
            self.incorrect_dialog("Имя должно входить в диапозон от 4 до 49 символов")
        self.upload_data()

    @staticmethod
    def add_clientuser_dialog():
        add_client_dialog = QDialog()
        ui = Ui_AddClientDialog()
        ui.setupUi(add_client_dialog)

        add_client_dialog.show()
        add_client_dialog.exec()

    def change_user_dialog(self):
        change_window = QDialog()
        ui = Ui_ChangeUserDialog()
        ui.setupUi(change_window)

        ui.change_user_button.clicked.connect(lambda: self.change_user_data(ui))

        change_window.show()
        change_window.exec()

    def change_user_data(self, ui):
        from AppHotel.Brain.Handle import Handler
        hand = Handler()
        id = self.admin_ui.tableWidget.currentRow() + 1
        username = ui.new_username_input.toPlainText()
        passw = ui.new_password_input.toPlainText()
        role = ui.new_role_input.currentText()
        status = ui.new_status_input.toPlainText()

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
        ui = Ui_ConfirmDelUserDialog()
        ui.setupUi(self.del_window)

        ui.confirm_button.clicked.connect(lambda: self.del_user_data())
        ui.cancel_button.clicked.connect(lambda: self.del_window.close())

        self.del_window.show()
        self.del_window.exec()

    def del_user_data(self):
        from AppHotel.Brain.Handle import Handler
        hand = Handler()
        id = self.admin_ui.tableWidget.currentRow() + 1
        status_code = hand.key_del_current_user(id)

        if status_code == 0:
            self.upload_data()

            self.success_dialog('Пользователь удалён')
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        self.del_window.close()
        self.upload_data()

    def del_client_dialog(self):
        self.del_window = QDialog()
        ui = Ui_ConfirmDelUserDialog()
        ui.setupUi(self.del_window)

        ui.confirm_button.clicked.connect(lambda: self.del_client_data())
        ui.cancel_button.clicked.connect(lambda: self.del_window.close())

        self.del_window.show()
        self.del_window.exec()

    def del_client_data(self):
        from AppHotel.Brain.Handle import Handler
        hand = Handler()
        id = self.admin_ui.tableWidget_1.currentRow() + 1

        status_code = hand.key_del_current_client(id)
        print(status_code)
        if status_code == 0:
            self.upload_data()

            self.success_dialog('Пользователь удалён')
        if status_code == 1:
            self.incorrect_dialog("Роли могут состоять из admin, manager, staff, client")
        self.del_window.close()
        self.upload_data()

    def incorrect_dialog(self, massage):
        incorrect_window = QDialog()
        ui = Ui_IncorrectPassDialog()
        ui.setupUi(incorrect_window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: incorrect_window.close())

        self.upload_data()

        incorrect_window.show()
        incorrect_window.exec()

    def success_dialog(self, massage):
        success_window = QDialog()
        ui = Ui_SuccessAutorizeDialog()
        ui.setupUi(success_window)

        ui.label.setText(massage)
        ui.confirm_button.clicked.connect(lambda: success_window.close())

        self.upload_data()

        success_window.show()
        success_window.exec()
