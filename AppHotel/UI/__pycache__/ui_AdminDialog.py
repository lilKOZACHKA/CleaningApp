# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminDialogYYBTFB.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AdminDialog(object):
    def setupUi(self, AdminDialog):
        if not AdminDialog.objectName():
            AdminDialog.setObjectName(u"AdminDialog")
        AdminDialog.resize(720, 573)
        AdminDialog.setMinimumSize(QSize(700, 573))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(109, 123, 141, 255))
        gradient.setColorAt(1, QColor(74, 112, 139, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(127, 127, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 170, 170, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(109, 123, 141, 255))
        gradient1.setColorAt(1, QColor(74, 112, 139, 255))
        brush5 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(109, 123, 141, 255))
        gradient2.setColorAt(1, QColor(74, 112, 139, 255))
        brush6 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(109, 123, 141, 255))
        gradient3.setColorAt(1, QColor(74, 112, 139, 255))
        brush9 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(109, 123, 141, 255))
        gradient4.setColorAt(1, QColor(74, 112, 139, 255))
        brush10 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(109, 123, 141, 255))
        gradient5.setColorAt(1, QColor(74, 112, 139, 255))
        brush11 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(109, 123, 141, 255))
        gradient6.setColorAt(1, QColor(74, 112, 139, 255))
        brush12 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(109, 123, 141, 255))
        gradient7.setColorAt(1, QColor(74, 112, 139, 255))
        brush13 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(109, 123, 141, 255))
        gradient8.setColorAt(1, QColor(74, 112, 139, 255))
        brush14 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        AdminDialog.setPalette(palette)
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        AdminDialog.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        AdminDialog.setWindowIcon(icon)
        AdminDialog.setWindowOpacity(1.000000000000000)
        AdminDialog.setStyleSheet(u"QDialog {\n"
"        background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */\n"
"        );\n"
"        color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    }")
        self.gridLayout = QGridLayout(AdminDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AdminDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(693, 555))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(684, 537))
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formWidget = QWidget(self.tab)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setMinimumSize(QSize(107, 443))
        self.formWidget.setMaximumSize(QSize(443, 443))
        self.formWidget.setStyleSheet(u"background: qlineargradient(\n"
"            x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #6D7B8D,  /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 */\n"
"            stop:1 #4A708B   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 */)")
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.add_new_user_button = QPushButton(self.formWidget)
        self.add_new_user_button.setObjectName(u"add_new_user_button")
        self.add_new_user_button.setMinimumSize(QSize(103, 30))
        font1 = QFont()
        font1.setBold(True)
        self.add_new_user_button.setFont(font1)
        self.add_new_user_button.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.add_new_user_button)

        self.change_user_button = QPushButton(self.formWidget)
        self.change_user_button.setObjectName(u"change_user_button")
        self.change_user_button.setMinimumSize(QSize(103, 30))
        self.change_user_button.setFont(font1)
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

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.change_user_button)

        self.refresh_tablet_button = QPushButton(self.formWidget)
        self.refresh_tablet_button.setObjectName(u"refresh_tablet_button")
        self.refresh_tablet_button.setMinimumSize(QSize(103, 30))
        self.refresh_tablet_button.setFont(font1)
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

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.refresh_tablet_button)

        self.del_user_button = QPushButton(self.formWidget)
        self.del_user_button.setObjectName(u"del_user_button")
        self.del_user_button.setMinimumSize(QSize(103, 30))
        self.del_user_button.setFont(font1)
        self.del_user_button.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.del_user_button)


        self.horizontalLayout.addWidget(self.formWidget)

        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font2 = QFont()
        font2.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font3 = QFont()
        font3.setPointSize(10)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(502, 288))
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(AdminDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminDialog)
    # setupUi

    def retranslateUi(self, AdminDialog):
        AdminDialog.setWindowTitle(QCoreApplication.translate("AdminDialog", u"\u0410\u0434\u043c\u0438\u043d-\u043f\u0430\u043d\u0435\u043b\u044c", None))
        self.add_new_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.refresh_tablet_button.setText(QCoreApplication.translate("AdminDialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.del_user_button.setText(QCoreApplication.translate("AdminDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminDialog", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminDialog", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminDialog", u"\u0420\u043e\u043b\u044c", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AdminDialog", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442\u044b", None))
    # retranslateUi

