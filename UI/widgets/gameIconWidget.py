from PySide6.QtWidgets import QWidget

from UI.widgets.ui_gameIconWidget import Ui_Form


class gameIconWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)