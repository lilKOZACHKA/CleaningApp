# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BanDialogzjuPzR.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_BanDialog(object):
    def setupUi(self, BanDialog):
        if not BanDialog.objectName():
            BanDialog.setObjectName(u"BanDialog")
        BanDialog.resize(323, 165)
        BanDialog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(BanDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(BanDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid  rgba(255, 255, 255, 90);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"border: none;\n"
"background: none;")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"border-radius: 7px;")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.confirm_button = QPushButton(self.widget_2)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setMinimumSize(QSize(25, 30))
        self.confirm_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.confirm_button)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(BanDialog)

        QMetaObject.connectSlotsByName(BanDialog)
    # setupUi

    def retranslateUi(self, BanDialog):
        BanDialog.setWindowTitle(QCoreApplication.translate("BanDialog", u"\u0417\u0430\u0431\u0430\u043d\u0435\u043d", None))
        self.label.setText(QCoreApplication.translate("BanDialog", u"\u0412 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0432\u044b \u0437\u0430\u0431\u0430\u043d\u0435\u043d\u044b, \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u0435\u0441\u044c \u043a \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0443", None))
        self.confirm_button.setText(QCoreApplication.translate("BanDialog", u"\u041e\u043a", None))
    # retranslateUi

