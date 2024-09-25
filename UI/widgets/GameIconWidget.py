from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from UI.widgets.ui_GameIconWidget import Ui_Icon
from UI.widgets import ElidedLabel


class GameIconWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.icon = Ui_Icon()
        self.icon.setupUi(self)

        # self.icon.Icon.setMaximumSize(100, 150)

        # self.label = ElidedLabel()
        # self.label.setElidedMode(Qt.ElideRight)
        #
        # self.layout = self.icon.Form.layout()
        # self.layout.addWidget(self.label)
