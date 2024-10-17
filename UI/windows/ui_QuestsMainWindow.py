# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestsMainWindoweWqPoV.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

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
        self.actionAdd_Game = QAction(MainWindow)
        self.actionAdd_Game.setObjectName(u"actionAdd_Game")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.gameIconsScrollArea = QWidget()
        self.gameIconsScrollArea.setObjectName(u"gameIconsScrollArea")
        self.gameIconsScrollArea.setGeometry(QRect(0, 0, 54, 500))
        self.scrollArea.setWidget(self.gameIconsScrollArea)
        self.splitter.addWidget(self.scrollArea)
        self.questsMetadataStackedWidget = QStackedWidget(self.splitter)
        self.questsMetadataStackedWidget.setObjectName(u"questsMetadataStackedWidget")
        sizePolicy.setHeightForWidth(self.questsMetadataStackedWidget.sizePolicy().hasHeightForWidth())
        self.questsMetadataStackedWidget.setSizePolicy(sizePolicy)
        self.noGamesPage = QWidget()
        self.noGamesPage.setObjectName(u"noGamesPage")
        sizePolicy.setHeightForWidth(self.noGamesPage.sizePolicy().hasHeightForWidth())
        self.noGamesPage.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.noGamesPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.noGamesLabel = QLabel(self.noGamesPage)
        self.noGamesLabel.setObjectName(u"noGamesLabel")
        sizePolicy.setHeightForWidth(self.noGamesLabel.sizePolicy().hasHeightForWidth())
        self.noGamesLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.noGamesLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.questsMetadataStackedWidget.addWidget(self.noGamesPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gameCoverImage = QLabel(self.page)
        self.gameCoverImage.setObjectName(u"gameCoverImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gameCoverImage.sizePolicy().hasHeightForWidth())
        self.gameCoverImage.setSizePolicy(sizePolicy1)
        self.gameCoverImage.setMinimumSize(QSize(0, 0))
        self.gameCoverImage.setMaximumSize(QSize(200, 300))

        self.verticalLayout_12.addWidget(self.gameCoverImage, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gameTitle = QLabel(self.page)
        self.gameTitle.setObjectName(u"gameTitle")

        self.verticalLayout_12.addWidget(self.gameTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 227, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.questsMetadataStackedWidget.addWidget(self.page)
        self.splitter.addWidget(self.questsMetadataStackedWidget)

        self.horizontalLayout.addWidget(self.splitter)

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
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionAdd_Game)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuExport.addAction(self.actionExport_all)
        self.menuExport.addAction(self.actionExport_selected)
        self.toolBar.addAction(self.actionAdd_Game)

        self.retranslateUi(MainWindow)

        self.questsMetadataStackedWidget.setCurrentIndex(0)


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
        self.actionAdd_Game.setText(QCoreApplication.translate("MainWindow", u"Add Game", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.noGamesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">(no games)</span></p></body></html>", None))
        self.gameCoverImage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.gameTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">TextLabel</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

