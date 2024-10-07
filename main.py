from PySide6.QtWidgets import QApplication

import sys

from UI.windows.QuestsMainWindow import QuestsMainWindow

app = QApplication(sys.argv)

window = QuestsMainWindow()
window.show()

app.aboutToQuit.connect(window.quit_app)

sys.exit(app.exec())
