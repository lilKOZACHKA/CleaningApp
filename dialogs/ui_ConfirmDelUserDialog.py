# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfirmDelUserDialoglDtcFF.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ConfirmDelUserDialog(object):
    def setupUi(self, ConfirmDelUserDialog):
        if not ConfirmDelUserDialog.objectName():
            ConfirmDelUserDialog.setObjectName(u"ConfirmDelUserDialog")
        ConfirmDelUserDialog.resize(311, 154)
        ConfirmDelUserDialog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"border-radius: 7px;")
        self.gridLayout = QGridLayout(ConfirmDelUserDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(ConfirmDelUserDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.confirm_button = QPushButton(self.widget_2)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setMinimumSize(QSize(25, 30))

        self.horizontalLayout.addWidget(self.confirm_button)

        self.cancel_button = QPushButton(self.widget_2)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(ConfirmDelUserDialog)

        QMetaObject.connectSlotsByName(ConfirmDelUserDialog)
    # setupUi

    def retranslateUi(self, ConfirmDelUserDialog):
        ConfirmDelUserDialog.setWindowTitle(QCoreApplication.translate("ConfirmDelUserDialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("ConfirmDelUserDialog", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f?", None))
        self.confirm_button.setText(QCoreApplication.translate("ConfirmDelUserDialog", u"\u041e\u043a", None))
        self.cancel_button.setText(QCoreApplication.translate("ConfirmDelUserDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

