# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserDialogumvnGM.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(978, 583)
        Dialog.setStyleSheet(u"QDialog {\n"
"        background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 963, 567))
        self.widget.setMinimumSize(QSize(693, 555))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(684, 537))
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formWidget = QWidget(self.tab)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget.sizePolicy().hasHeightForWidth())
        self.formWidget.setSizePolicy(sizePolicy)
        self.formWidget.setMinimumSize(QSize(107, 443))
        self.formWidget.setMaximumSize(QSize(443, 443))
        self.formWidget.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.formWidget.setFont(font1)
        self.formWidget.setStyleSheet(u"background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */)")
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.change_pass_button = QPushButton(self.formWidget)
        self.change_pass_button.setObjectName(u"change_pass_button")
        self.change_pass_button.setMinimumSize(QSize(103, 30))
        font2 = QFont()
        font2.setBold(True)
        self.change_pass_button.setFont(font2)
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

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.change_pass_button)

        self.refresh_tablet_button = QPushButton(self.formWidget)
        self.refresh_tablet_button.setObjectName(u"refresh_tablet_button")
        self.refresh_tablet_button.setMinimumSize(QSize(103, 30))
        self.refresh_tablet_button.setFont(font2)
        self.refresh_tablet_button.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.refresh_tablet_button)

        self.refresh_tablet_button_2 = QPushButton(self.formWidget)
        self.refresh_tablet_button_2.setObjectName(u"refresh_tablet_button_2")
        self.refresh_tablet_button_2.setMinimumSize(QSize(103, 30))
        self.refresh_tablet_button_2.setFont(font2)
        self.refresh_tablet_button_2.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.refresh_tablet_button_2)


        self.horizontalLayout.addWidget(self.formWidget)

        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.change_pass_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.refresh_tablet_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.refresh_tablet_button_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi

