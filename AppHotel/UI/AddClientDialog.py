# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading Brain file 'AddClientDialogkOBTSK.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_AddClientDialog(object):
    def setupUi(self, AddClientDialog):
        if not AddClientDialog.objectName():
            AddClientDialog.setObjectName(u"AddClientDialog")
        AddClientDialog.resize(251, 284)
        AddClientDialog.setMinimumSize(QSize(251, 270))
        AddClientDialog.setStyleSheet(u"QDialog{\n"
"        background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }")
        self.widget = QWidget(AddClientDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 234, 261))
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

        self.new_id_input = QComboBox(self.widget)
        self.new_id_input.setObjectName(u"new_id_input")
        self.new_id_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_id_input.setEditable(True)
        self.new_id_input.setFrame(False)

        self.verticalLayout_2.addWidget(self.new_id_input)

        self.new_name_input = QTextEdit(self.widget)
        self.new_name_input.setObjectName(u"new_name_input")
        self.new_name_input.setMaximumSize(QSize(400, 25))
        self.new_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_name_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.new_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_name_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_name_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.new_name_input)

        self.new_surname_input = QTextEdit(self.widget)
        self.new_surname_input.setObjectName(u"new_surname_input")
        self.new_surname_input.setMaximumSize(QSize(400, 25))
        self.new_surname_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_surname_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.new_surname_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_surname_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_surname_input.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.new_surname_input)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.new_email_input = QTextEdit(self.widget)
        self.new_email_input.setObjectName(u"new_email_input")
        self.new_email_input.setMaximumSize(QSize(400, 25))
        self.new_email_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.new_email_input.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.new_email_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.new_email_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.new_email_input)

        self.add_user_button = QPushButton(self.widget)
        self.add_user_button.setObjectName(u"add_user_button")
        self.add_user_button.setMaximumSize(QSize(400, 16777215))
        self.add_user_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.add_user_button)


        self.retranslateUi(AddClientDialog)

        QMetaObject.connectSlotsByName(AddClientDialog)
    # setupUi

    def retranslateUi(self, AddClientDialog):
        AddClientDialog.setWindowTitle(QCoreApplication.translate("AddClientDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435\u041a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("AddClientDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c  \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.new_id_input.setPlaceholderText(QCoreApplication.translate("AddClientDialog", u"\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.new_name_input.setPlaceholderText(QCoreApplication.translate("AddClientDialog", u"\u0418\u043c\u044f", None))
        self.new_surname_input.setPlaceholderText(QCoreApplication.translate("AddClientDialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("AddClientDialog", u"7(000)-000-00-00", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("AddClientDialog", u"\u041d\u043e\u043c\u0435\u0440 \u0422\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.new_email_input.setPlaceholderText(QCoreApplication.translate("AddClientDialog", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.add_user_button.setText(QCoreApplication.translate("AddClientDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

