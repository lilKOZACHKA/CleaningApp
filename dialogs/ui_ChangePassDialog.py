# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangePassDialogHGpayR.ui'
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
        ChangePassDialog.resize(289, 275)
        ChangePassDialog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(ChangePassDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ChangePassDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.old_password_input = QPlainTextEdit(self.widget)
        self.old_password_input.setObjectName(u"old_password_input")
        self.old_password_input.setMaximumSize(QSize(400, 25))
        self.old_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.old_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.old_password_input)

        self.new_password_input = QPlainTextEdit(self.widget)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setMaximumSize(QSize(400, 25))
        self.new_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.new_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.new_password_input)

        self.validate_password_input = QPlainTextEdit(self.widget)
        self.validate_password_input.setObjectName(u"validate_password_input")
        self.validate_password_input.setMaximumSize(QSize(400, 25))
        self.validate_password_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.validate_password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.validate_password_input)

        self.change_pass_button = QPushButton(self.widget)
        self.change_pass_button.setObjectName(u"change_pass_button")
        self.change_pass_button.setMaximumSize(QSize(400, 16777215))

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
        self.validate_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.change_pass_button.setText(QCoreApplication.translate("ChangePassDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

