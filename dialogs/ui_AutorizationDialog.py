# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutorizationDialogOgXchx.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AutorizationDiolog(object):
    def setupUi(self, AutorizationDiolog):
        if not AutorizationDiolog.objectName():
            AutorizationDiolog.setObjectName(u"AutorizationDiolog")
        AutorizationDiolog.resize(281, 384)
        AutorizationDiolog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.gridLayout = QGridLayout(AutorizationDiolog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AutorizationDiolog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"border-radius: 7px;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 69, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.head = QLabel(self.widget_2)
        self.head.setObjectName(u"head")
        self.head.setMaximumSize(QSize(400, 30))
        self.head.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"border: none;\n"
"background: none;")
        self.head.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.head)

        self.verticalSpacer_2 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.login_input = QPlainTextEdit(self.widget_2)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setMinimumSize(QSize(0, 35))
        self.login_input.setMaximumSize(QSize(400, 25))
        self.login_input.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.login_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.login_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.login_input.setOverwriteMode(True)
        self.login_input.setCenterOnScroll(True)

        self.verticalLayout_2.addWidget(self.login_input)

        self.password_input = QPlainTextEdit(self.widget_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 35))
        self.password_input.setMaximumSize(QSize(400, 25))
        self.password_input.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.password_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.password_input.setOverwriteMode(True)

        self.verticalLayout_2.addWidget(self.password_input)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.login_button = QPushButton(self.widget_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"border-radius: 7px;")

        self.verticalLayout_2.addWidget(self.login_button)

        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(AutorizationDiolog)

        QMetaObject.connectSlotsByName(AutorizationDiolog)
    # setupUi

    def retranslateUi(self, AutorizationDiolog):
        AutorizationDiolog.setWindowTitle(QCoreApplication.translate("AutorizationDiolog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.head.setText(QCoreApplication.translate("AutorizationDiolog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.login_input.setPlainText("")
        self.login_input.setPlaceholderText(QCoreApplication.translate("AutorizationDiolog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("AutorizationDiolog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_button.setText(QCoreApplication.translate("AutorizationDiolog", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
    # retranslateUi

