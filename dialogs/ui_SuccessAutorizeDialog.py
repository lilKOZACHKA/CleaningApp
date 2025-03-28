# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SuccessAutorizeDialogaEcdfp.ui'
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

class Ui_SuccessAutorizeDialog(object):
    def setupUi(self, SuccessAutorizeDialog):
        if not SuccessAutorizeDialog.objectName():
            SuccessAutorizeDialog.setObjectName(u"SuccessAutorizeDialog")
        SuccessAutorizeDialog.resize(311, 159)
        self.verticalLayout_2 = QVBoxLayout(SuccessAutorizeDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(SuccessAutorizeDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

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


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(SuccessAutorizeDialog)

        QMetaObject.connectSlotsByName(SuccessAutorizeDialog)
    # setupUi

    def retranslateUi(self, SuccessAutorizeDialog):
        SuccessAutorizeDialog.setWindowTitle(QCoreApplication.translate("SuccessAutorizeDialog", u"\u0423\u0441\u043f\u0435\u0445", None))
        self.label.setText(QCoreApplication.translate("SuccessAutorizeDialog", u"\u0412\u044b \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043b\u0438\u0441\u044c!", None))
        self.confirm_button.setText(QCoreApplication.translate("SuccessAutorizeDialog", u"\u041e\u043a", None))
    # retranslateUi

