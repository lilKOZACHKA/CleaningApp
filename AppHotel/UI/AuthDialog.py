# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading Brain file 'AutorizationDialogyqvrjr.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_AutorizationDiolog(object):
    def setupUi(self, AutorizationDiolog):
        if not AutorizationDiolog.objectName():
            AutorizationDiolog.setObjectName(u"AutorizationDiolog")
        AutorizationDiolog.resize(205, 261)
        AutorizationDiolog.setMinimumSize(QSize(179, 261))
        AutorizationDiolog.setStyleSheet(u"background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"")
        self.gridLayout = QGridLayout(AutorizationDiolog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AutorizationDiolog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(187, 243))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.head = QLabel(self.widget_2)
        self.head.setObjectName(u"head")
        self.head.setMaximumSize(QSize(400, 30))
        font = QFont()
        font.setPointSize(14)
        self.head.setFont(font)
        self.head.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.head.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.head)

        self.verticalSpacer_2 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 69, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.login_input = QTextEdit(self.widget_2)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setMaximumSize(QSize(400, 25))
        self.login_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.login_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.login_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.login_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.login_input.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.login_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.login_input)

        self.password_input = QTextEdit(self.widget_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMaximumSize(QSize(400, 25))
        self.password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.password_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.password_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.password_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.password_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.password_input)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.login_button = QPushButton(self.widget_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u"QPushButton {\n"
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
        self.login_input.setPlaceholderText(QCoreApplication.translate("AutorizationDiolog", u"\u043b\u043e\u0433\u0438\u043d", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("AutorizationDiolog", u"\u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_button.setText(QCoreApplication.translate("AutorizationDiolog", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
    # retranslateUi

