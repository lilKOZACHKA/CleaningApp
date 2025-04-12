# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangePassDialogqUBtql.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ChangePassDialog(object):
    def setupUi(self, ChangePassDialog):
        if not ChangePassDialog.objectName():
            ChangePassDialog.setObjectName(u"ChangePassDialog")
        ChangePassDialog.resize(301, 288)
        ChangePassDialog.setStyleSheet(u"background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"")
        self.verticalLayout = QVBoxLayout(ChangePassDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ChangePassDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(265, 57))
        self.label.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.old_password_input = QPlainTextEdit(self.widget)
        self.old_password_input.setObjectName(u"old_password_input")
        self.old_password_input.setMaximumSize(QSize(400, 25))
        self.old_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.old_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.old_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.old_password_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.old_password_input)

        self.new_password_input = QPlainTextEdit(self.widget)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setMaximumSize(QSize(400, 25))
        self.new_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_password_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.new_password_input)

        self.validate_password_input = QPlainTextEdit(self.widget)
        self.validate_password_input.setObjectName(u"validate_password_input")
        self.validate_password_input.setMaximumSize(QSize(400, 25))
        self.validate_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.validate_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.validate_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.validate_password_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.validate_password_input)

        self.change_pass_button = QPushButton(self.widget)
        self.change_pass_button.setObjectName(u"change_pass_button")
        self.change_pass_button.setMaximumSize(QSize(400, 16777215))
        self.change_pass_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.change_pass_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(ChangePassDialog)

        QMetaObject.connectSlotsByName(ChangePassDialog)
    # setupUi

    def retranslateUi(self, ChangePassDialog):
        ChangePassDialog.setWindowTitle(QCoreApplication.translate("ChangePassDialog", u"\u0421\u043c\u0435\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("ChangePassDialog", u"  \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0441\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.old_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassDialog", u"\u0421\u0442\u0430\u0440\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.new_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.validate_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassDialog", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.change_pass_button.setText(QCoreApplication.translate("ChangePassDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

