from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

from DatabaseManager import DatabaseManager
from FlowLayout import FlowLayout
from UI.windows.ui_QuestsMainWindow import Ui_MainWindow


class QuestsMainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.layout = FlowLayout(self.gameIconsScrollArea)

        self.addQuestsPushButton.clicked.connect(self.add_quests_btn_clicked)
        self.removeQuestsPushButton.clicked.connect(self.remove_quests_btn_clicked)

        self.database = DatabaseManager()

        # populate scrollArea with the games already in the database
        game_titles_icons = self.database.get_all_games()
        for game in game_titles_icons:
            self.generate_game_icon(game[0], game[1])

    def remove_quests_btn_clicked(self):
        # TODO remove quest list corresponding to highlighted game icon
        pass

    def add_quests_btn_clicked(self):
        title, image_path = self.database.add_new_game()
        self.generate_game_icon(title, image_path)

    def generate_game_icon(self, title, image):
        tool_button = QToolButton(self)
        tool_button.setIcon(QIcon(image))
        tool_button.setIconSize(QSize(100, 150))  # Set the icon size
        tool_button.setText(title)  # Set the label text
        tool_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # Text under the icon
        tool_button.setObjectName(title)

        palette = QApplication.palette()
        highlight_color = palette.highlight().color().name()

        tool_button.setStyleSheet('QToolButton { border: none; background: transparent; }'
                                  f'QToolButton:hover {{ background-color: {highlight_color}; }}')

        self.layout.setSpacing(tool_button.width() / 2)
        self.layout.addWidget(tool_button)
