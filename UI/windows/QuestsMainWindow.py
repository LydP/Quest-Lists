from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize

import sys

from FlowLayout import FlowLayout
from ui_QuestsMainWindow import Ui_MainWindow


class QuestsMainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.layout = FlowLayout(self.gameIconsScrollArea)

        self.addQuestsPushButton.clicked.connect(self.add_quests_btn_clicked)
        self.removeQuestsPushButton.clicked.connect(self.remove_quests_btn_clicked)

    def remove_quests_btn_clicked(self):
        # TODO remove quest list corresponding to highlighted game icon
        pass

    def add_quests_btn_clicked(self):
        # TODO add game icon with placeholder image and title
        pass
