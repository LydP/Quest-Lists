from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QToolButton, QLabel, QButtonGroup, QLineEdit
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize

from DatabaseManager import DatabaseManager
from FlowLayout import FlowLayout
from UI.windows.ui_QuestsMainWindow import Ui_MainWindow


class QuestsMainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.layout = FlowLayout(self.gameIconsScrollArea)

        self.database = DatabaseManager()

        # add QToolButton icons to QButtonGroup so that only one can be checked at a time
        self.icon_group = QButtonGroup()
        self.icon_group.setExclusive(True)

        # define QActions
        self.actionAdd_Game.triggered.connect(self.action_add_game)
        self.actionExit.triggered.connect(self.quit_app)
        self.actionRename.triggered.connect(self.action_rename_game)

        # populate scrollArea with the games already in the database
        game_titles_icons = self.database.get_all_games()

        window_width = self.width()
        self.splitter.setSizes([(window_width * 2) // 3, window_width // 3])

        if not game_titles_icons:
            self.questsMetadataStackedWidget.setCurrentIndex(0)
        else:
            self.questsMetadataStackedWidget.setCurrentIndex(1)
            self.renameGameLineEdit.hide()
            # add games to scrollArea
            for game in game_titles_icons:
                self.generate_game_icon(game[0], game[1], game[2])

            # populate metadata panel with metadata from first item in game_titles_icons on startup
            self.icon_group.button(game_titles_icons[0][2]).click()

    def action_delete_game(self):
        # TODO remove all data corresponding to highlighted game icon
        pass

    def action_add_game(self):
        title, image_path, game_id = self.database.add_new_game()
        self.generate_game_icon(title, image_path, game_id)

        # necessary for when adding a new game to empty database
        self.gameCoverImage.setFixedSize(200, 300)
        self.questsMetadataStackedWidget.setCurrentIndex(1)

        # populate metadata with newest addition's data
        self.icon_group.buttons()[-1].click()

    def action_rename_game(self):
        self.gameTitle.hide()

        self.renameGameLineEdit.setText(self.gameTitle.text())
        self.renameGameLineEdit.show()
        self.renameGameLineEdit.setFocus()

        self.renameGameLineEdit.editingFinished.connect(self.name_edit)

    def name_edit(self):
        current_button = self.icon_group.checkedButton()

        new_name = self.renameGameLineEdit.text()
        old_name = current_button.text()

        current_button.setText(new_name)
        self.gameTitle.setText(new_name)

        self.renameGameLineEdit.hide()
        self.gameTitle.show()

        self.database.rename_game(old_name, new_name)

    def generate_game_icon(self, title, image, game_id):
        tool_button = QToolButton(self)
        tool_button.setIcon(QIcon(image))
        tool_button.setIconSize(QSize(100, 150))  # Set the icon size
        tool_button.setText(title)  # Set the label text
        tool_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # Text under the icon
        tool_button.setObjectName(title)  # set name so I can refer to it later
        tool_button.setProperty('icon_path', image)  # store the image path on the button
        tool_button.setCheckable(True)

        # set button's ID in icon_group
        self.icon_group.addButton(tool_button)
        self.icon_group.setId(tool_button, game_id)

        # click signals
        tool_button.clicked.connect(self.game_icon_clicked)

        palette = QApplication.palette()
        highlight_color = palette.highlight().color().name()

        tool_button.setStyleSheet('QToolButton { border: none; background: transparent; }'
                                  f'QToolButton:hover, QToolButton:checked {{ background-color: {highlight_color}; }}')

        self.layout.setSpacing(tool_button.width() / 2)

        self.layout.addWidget(tool_button)

    def game_icon_clicked(self):
        current_game = self.sender()
        current_icon = current_game.property('icon_path')
        current_title = current_game.text()

        self.populate_metadata(current_title, current_icon)

    def populate_metadata(self, title, image):
        # TODO need to test this when database has some stuff in it
        # TODO this is convoluted. clean it up
        # add game cover image to metadata panel
        icon = QPixmap(image).scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.gameCoverImage.setPixmap(icon)
        # add game title
        self.gameTitle.setText(title)
        self.gameTitle.setAlignment(Qt.AlignCenter)
        self.gameTitle.setStyleSheet('font-style: italic')

        quest_counts = self.database.count_quests(title)

        if quest_counts:
            total_quests_completed = 0
            total_quest_count = 0
            base_category_quest_counts = []
            dlc_category_quest_counts = []
            # find the total number of completed quests, the total number of quests overall, and number of completed
            # quests and overall quests for each category
            for game, categories in quest_counts:
                for category, (completed_quests, total_quests) in categories.items():
                    total_quests_completed += completed_quests
                    total_quest_count += total_quests

                    if game == title:
                        base_category_quest_counts.append((game, category, completed_quests, total_quests))
                    else:
                        dlc_category_quest_counts.append((game, category, completed_quests, total_quests))

            percent_completed = (total_quests_completed / total_quest_count) * 100

            completionist_label = QLabel(f'Completionist: {percent_completed:.2f}')
            self.questsMetadataStackedWidget.addWidget(completionist_label)

            # base game label shows number of completed quests versus total quests across all categories in base game
            base_quests_completed = sum([q[2] for q in base_category_quest_counts])
            base_quest_count = sum([q[3] for q in base_category_quest_counts])
            base_game_label = QLabel(f'{title}: {base_quests_completed} / {base_quest_count}')
            self.questsMetadataStackedWidget.addWidget(base_game_label)

            # add quest counts for each category in base game
            for q in base_category_quest_counts:
                category_label = QLabel(f'\t{q[1]}: {q[2]} / {q[3]}')
                self.questsMetadataStackedWidget.addWidget(category_label)

            dlc = list(set(dlc[0] for dlc in dlc_category_quest_counts))
            for d in dlc:
                # completed quests versus total quests across all categories for each DLC
                dlc_quests_completed = sum([q[2] for q in dlc_category_quest_counts if q[1] == d])
                dlc_quest_count = sum([q[3] for q in dlc_category_quest_counts if q[1] == d])
                dlc_label = QLabel(f'{d}: {dlc_quests_completed} / {dlc_quest_count}')
                self.questsMetadataStackedWidget.addWidget(dlc_label)

                # complete quests versus total quests for each category in each DLC
                dlc_categories = [dlc for dlc in dlc_category_quest_counts if dlc[0] == d]
                for q in dlc_categories:
                    dlc_category_label = QLabel(f'\t{q[1]}: {q[2]} / {q[3]}')
                    self.questsMetadataStackedWidget.addWidget(dlc_category_label)

    def quit_app(self):
        self.database.close_database()
        QApplication.instance().aboutToQuit.disconnect(self.quit_app)
        QApplication.instance().quit()
