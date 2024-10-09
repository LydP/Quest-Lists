# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestsMainWindowXupUTP.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_new_quest_list = QAction(MainWindow)
        self.actionAdd_new_quest_list.setObjectName(u"actionAdd_new_quest_list")
        self.actionDelete_selected_quest_list = QAction(MainWindow)
        self.actionDelete_selected_quest_list.setObjectName(u"actionDelete_selected_quest_list")
        self.actionAdd_new_quest_list_2 = QAction(MainWindow)
        self.actionAdd_new_quest_list_2.setObjectName(u"actionAdd_new_quest_list_2")
        self.actionDelete_selected_quest_list_2 = QAction(MainWindow)
        self.actionDelete_selected_quest_list_2.setObjectName(u"actionDelete_selected_quest_list_2")
        self.actionExport_all = QAction(MainWindow)
        self.actionExport_all.setObjectName(u"actionExport_all")
        self.actionExport_selected = QAction(MainWindow)
        self.actionExport_selected.setObjectName(u"actionExport_selected")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.layoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.gameIconsScrollArea = QWidget()
        self.gameIconsScrollArea.setObjectName(u"gameIconsScrollArea")
        self.gameIconsScrollArea.setGeometry(QRect(0, 0, 406, 492))
        self.scrollArea.setWidget(self.gameIconsScrollArea)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addQuestsPushButton = QPushButton(self.layoutWidget)
        self.addQuestsPushButton.setObjectName(u"addQuestsPushButton")
        self.addQuestsPushButton.setEnabled(True)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.addQuestsPushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addQuestsPushButton)

        self.removeQuestsPushButton = QPushButton(self.layoutWidget)
        self.removeQuestsPushButton.setObjectName(u"removeQuestsPushButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.removeQuestsPushButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.removeQuestsPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.questsMetadata = QGroupBox(self.splitter)
        self.questsMetadata.setObjectName(u"questsMetadata")
        self.questsMetadata.setAutoFillBackground(False)
        self.questsMetadata.setStyleSheet(u"QGroupBox {\n"
"	border-style: none;\n"
"}")
        self.gridLayout = QGridLayout(self.questsMetadata)
        self.gridLayout.setObjectName(u"gridLayout")
        self.questsMetadataStackedWidget = QStackedWidget(self.questsMetadata)
        self.questsMetadataStackedWidget.setObjectName(u"questsMetadataStackedWidget")
        self.noGamesPage = QWidget()
        self.noGamesPage.setObjectName(u"noGamesPage")
        self.verticalLayout_3 = QVBoxLayout(self.noGamesPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.noGamesLabel = QLabel(self.noGamesPage)
        self.noGamesLabel.setObjectName(u"noGamesLabel")

        self.verticalLayout_3.addWidget(self.noGamesLabel)

        self.questsMetadataStackedWidget.addWidget(self.noGamesPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gameCoverImage = QLabel(self.page_2)
        self.gameCoverImage.setObjectName(u"gameCoverImage")

        self.verticalLayout_4.addWidget(self.gameCoverImage)

        self.questsMetadataStackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.questsMetadataStackedWidget, 0, 0, 1, 1)

        self.splitter.addWidget(self.questsMetadata)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuExport.addAction(self.actionExport_all)
        self.menuExport.addAction(self.actionExport_selected)
        self.menuEdit.addAction(self.actionAdd_new_quest_list_2)
        self.menuEdit.addAction(self.actionDelete_selected_quest_list_2)

        self.retranslateUi(MainWindow)

        self.questsMetadataStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_new_quest_list.setText(QCoreApplication.translate("MainWindow", u"Add new quest list", None))
        self.actionDelete_selected_quest_list.setText(QCoreApplication.translate("MainWindow", u"Delete selected quest list", None))
        self.actionAdd_new_quest_list_2.setText(QCoreApplication.translate("MainWindow", u"Add new quest list", None))
        self.actionDelete_selected_quest_list_2.setText(QCoreApplication.translate("MainWindow", u"Delete selected quest list", None))
        self.actionExport_all.setText(QCoreApplication.translate("MainWindow", u"Export all...", None))
        self.actionExport_selected.setText(QCoreApplication.translate("MainWindow", u"Export selected...", None))
#if QT_CONFIG(tooltip)
        self.addQuestsPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add a quest list", None))
#endif // QT_CONFIG(tooltip)
        self.addQuestsPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.removeQuestsPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Delete selected quest list", None))
#endif // QT_CONFIG(tooltip)
        self.removeQuestsPushButton.setText("")
        self.questsMetadata.setTitle("")
        self.noGamesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">(no games)</span></p></body></html>", None))
        self.gameCoverImage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

