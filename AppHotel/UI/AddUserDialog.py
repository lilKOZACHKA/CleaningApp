# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading Brain file 'AddUserDialogOiVJJX.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling Brain file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AddUserDialog(object):
    def setupUi(self, AddUserDialog):
        if not AddUserDialog.objectName():
            AddUserDialog.setObjectName(u"AddUserDialog")
        AddUserDialog.resize(252, 236)
        AddUserDialog.setStyleSheet(u"QDialog{\n"
"        background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }")
        self.verticalLayout = QVBoxLayout(AddUserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AddUserDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(234, 217))
        self.widget.setStyleSheet(u"background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.new_username_input = QTextEdit(self.widget)
        self.new_username_input.setObjectName(u"new_username_input")
        self.new_username_input.setMaximumSize(QSize(400, 25))
        self.new_username_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_username_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.new_username_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_username_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_username_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.new_username_input)

        self.new_role_input = QComboBox(self.widget)
        self.new_role_input.addItem("")
        self.new_role_input.addItem("")
        self.new_role_input.addItem("")
        self.new_role_input.addItem("")
        self.new_role_input.setObjectName(u"new_role_input")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.new_role_input.setFont(font1)
        self.new_role_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.new_role_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.new_role_input.setMinimumContentsLength(0)
        self.new_role_input.setFrame(False)

        self.verticalLayout_2.addWidget(self.new_role_input)

        self.new_password_input = QTextEdit(self.widget)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setMaximumSize(QSize(400, 25))
        self.new_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_password_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.new_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_password_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.new_password_input)

        self.change_user_button = QPushButton(self.widget)
        self.change_user_button.setObjectName(u"change_user_button")
        self.change_user_button.setMaximumSize(QSize(400, 16777215))
        self.change_user_button.setStyleSheet(u"QPushButton {\n"
"        background: #5D6D7E;  /* \u0421\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        border: 1px solid #4A708B;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border-radius: 8px;\n"
"        font-size: 14px;\n"
"	border-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: #6D7B8D;  /* \u0421\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background: #4A708B;  /* \u0422\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    }\n"
"")

        self.verticalLayout_2.addWidget(self.change_user_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AddUserDialog)

        QMetaObject.connectSlotsByName(AddUserDialog)
    # setupUi

    def retranslateUi(self, AddUserDialog):
        AddUserDialog.setWindowTitle(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c  \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.new_username_input.setPlaceholderText(QCoreApplication.translate("AddUserDialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.new_role_input.setItemText(0, QCoreApplication.translate("AddUserDialog", u"admin", None))
        self.new_role_input.setItemText(1, QCoreApplication.translate("AddUserDialog", u"client", None))
        self.new_role_input.setItemText(2, QCoreApplication.translate("AddUserDialog", u"manager", None))
        self.new_role_input.setItemText(3, QCoreApplication.translate("AddUserDialog", u"staff", None))

        self.new_role_input.setCurrentText(QCoreApplication.translate("AddUserDialog", u"admin", None))
        self.new_password_input.setPlaceholderText(QCoreApplication.translate("AddUserDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.change_user_button.setText(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

