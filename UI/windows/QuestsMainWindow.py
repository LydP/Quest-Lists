from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

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
        tool_button = QToolButton(self)
        tool_button.setIcon(QIcon("resources/test_img.jpg"))
        tool_button.setIconSize(QSize(100, 150))  # Set the icon size
        tool_button.setText("New Quests List")  # Set the label text
        tool_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # Text under the icon

        palette = QApplication.palette()
        highlight_color = palette.highlight().color().name()

        tool_button.setStyleSheet('QToolButton { border: none; background: transparent; }'
                                  f'QToolButton:hover {{ background-color: {highlight_color}; }}')

        self.layout.setSpacing(tool_button.width() / 2)
        self.layout.addWidget(tool_button)
