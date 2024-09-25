# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gameIconWidgetUaMTQG.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Icon(object):
    def setupUi(self, Icon):
        if not Icon.objectName():
            Icon.setObjectName(u"Icon")
        Icon.resize(100, 190)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Icon.sizePolicy().hasHeightForWidth())
        Icon.setSizePolicy(sizePolicy)
        Icon.setMinimumSize(QSize(100, 190))
        Icon.setMaximumSize(QSize(100, 190))
        self.verticalLayout_2 = QVBoxLayout(Icon)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Image = QLabel(Icon)
        self.Image.setObjectName(u"Image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Image.sizePolicy().hasHeightForWidth())
        self.Image.setSizePolicy(sizePolicy1)
        self.Image.setMinimumSize(QSize(100, 150))
        self.Image.setMaximumSize(QSize(100, 150))
        self.Image.setPixmap(QPixmap(u"resources/test_img.jpg"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.Image)

        self.IconTitle = QLabel(Icon)
        self.IconTitle.setObjectName(u"IconTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.IconTitle.sizePolicy().hasHeightForWidth())
        self.IconTitle.setSizePolicy(sizePolicy2)
        self.IconTitle.setMaximumSize(QSize(100, 40))
        self.IconTitle.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.IconTitle)


        self.retranslateUi(Icon)

        QMetaObject.connectSlotsByName(Icon)
    # setupUi

    def retranslateUi(self, Icon):
        Icon.setWindowTitle(QCoreApplication.translate("Icon", u"Form", None))
        self.Image.setText("")
        self.IconTitle.setText(QCoreApplication.translate("Icon", u"<html><head/><body><p align=\"center\">Test Icon</p></body></html>", None))
    # retranslateUi

