# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddUserDialogQLTVnL.ui'
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

class Ui_AddUserDialog(object):
    def setupUi(self, AddUserDialog):
        if not AddUserDialog.objectName():
            AddUserDialog.setObjectName(u"AddUserDialog")
        AddUserDialog.resize(371, 300)
        self.verticalLayout = QVBoxLayout(AddUserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AddUserDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.new_username_input = QPlainTextEdit(self.widget)
        self.new_username_input.setObjectName(u"new_username_input")
        self.new_username_input.setMaximumSize(QSize(400, 25))

        self.verticalLayout_2.addWidget(self.new_username_input)

        self.new_password_input = QPlainTextEdit(self.widget)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setMaximumSize(QSize(400, 25))

        self.verticalLayout_2.addWidget(self.new_password_input)

        self.new_role_input = QPlainTextEdit(self.widget)
        self.new_role_input.setObjectName(u"new_role_input")
        self.new_role_input.setMaximumSize(QSize(400, 25))
        self.new_role_input.setTabStopDistance(90)

        self.verticalLayout_2.addWidget(self.new_role_input)

        self.change_user_button = QPushButton(self.widget)
        self.change_user_button.setObjectName(u"change_user_button")
        self.change_user_button.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_2.addWidget(self.change_user_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(AddUserDialog)

        QMetaObject.connectSlotsByName(AddUserDialog)
    # setupUi

    def retranslateUi(self, AddUserDialog):
        AddUserDialog.setWindowTitle(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.new_username_input.setPlaceholderText(QCoreApplication.translate("AddUserDialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.new_password_input.setPlaceholderText(QCoreApplication.translate("AddUserDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.new_role_input.setPlaceholderText(QCoreApplication.translate("AddUserDialog", u"\u0420\u043e\u043b\u044c", None))
        self.change_user_button.setText(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

