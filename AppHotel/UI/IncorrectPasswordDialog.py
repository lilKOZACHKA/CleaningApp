# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IncorrectPassDialogmxNcJW.ui'
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

class Ui_IncorrectPassDialog(object):
    def setupUi(self, IncorrectPassDialog):
        if not IncorrectPassDialog.objectName():
            IncorrectPassDialog.setObjectName(u"IncorrectPassDialog")
        IncorrectPassDialog.resize(314, 165)
        self.verticalLayout_2 = QVBoxLayout(IncorrectPassDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(IncorrectPassDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.confirm_button.setStyleSheet(u"background-color: rgb(133, 188, 255);")

        self.horizontalLayout.addWidget(self.confirm_button)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(IncorrectPassDialog)

        QMetaObject.connectSlotsByName(IncorrectPassDialog)
    # setupUi

    def retranslateUi(self, IncorrectPassDialog):
        IncorrectPassDialog.setWindowTitle(QCoreApplication.translate("IncorrectPassDialog", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439", None))
        self.label.setText(QCoreApplication.translate("IncorrectPassDialog", u"\u041d\u0435 \u0432\u0435\u0440\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.confirm_button.setText(QCoreApplication.translate("IncorrectPassDialog", u"\u041e\u043a", None))
    # retranslateUi

