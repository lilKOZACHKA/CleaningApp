# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminDialogJsToQZ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AdminDialog(object):
    def setupUi(self, AdminDialog):
        if not AdminDialog.objectName():
            AdminDialog.setObjectName(u"AdminDialog")
        AdminDialog.resize(780, 573)
        AdminDialog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"border-radius: 7px;")
        self.gridLayout = QGridLayout(AdminDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AdminDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_new_user_button = QPushButton(self.widget_2)
        self.add_new_user_button.setObjectName(u"add_new_user_button")

        self.verticalLayout.addWidget(self.add_new_user_button)

        self.change_user_button = QPushButton(self.widget_2)
        self.change_user_button.setObjectName(u"change_user_button")

        self.verticalLayout.addWidget(self.change_user_button)

        self.del_user_button = QPushButton(self.widget_2)
        self.del_user_button.setObjectName(u"del_user_button")

        self.verticalLayout.addWidget(self.del_user_button)

        self.verticalSpacer_2 = QSpacerItem(20, 336, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.refresh_tablet_button = QPushButton(self.widget_2)
        self.refresh_tablet_button.setObjectName(u"refresh_tablet_button")

        self.verticalLayout.addWidget(self.refresh_tablet_button)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"selection-background-color: rgb(255, 19, 19);")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.widget_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(AdminDialog)

        QMetaObject.connectSlotsByName(AdminDialog)
    # setupUi

    def retranslateUi(self, AdminDialog):
        AdminDialog.setWindowTitle(QCoreApplication.translate("AdminDialog", u"\u0410\u0434\u043c\u0438\u043d", None))
        self.add_new_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.del_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.refresh_tablet_button.setText(QCoreApplication.translate("AdminDialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminDialog", u"account_id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminDialog", u"username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminDialog", u"password_hash", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminDialog", u"role", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminDialog", u"status", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminDialog", u"login_attempts", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AdminDialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AdminDialog", u"Tab 2", None))
    # retranslateUi

