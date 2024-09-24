# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gameIconWidgetlfTjlk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon = QLabel(Form)
        self.icon.setObjectName(u"icon")

        self.verticalLayout.addWidget(self.icon)

        self.iconTitle = QLabel(Form)
        self.iconTitle.setObjectName(u"iconTitle")

        self.verticalLayout.addWidget(self.iconTitle)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.iconTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
    # retranslateUi

