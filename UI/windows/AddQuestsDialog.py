from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem, QApplication, QDialog

from UI.windows.ui_AddQuestsDialog import Ui_Dialog


class AddQuestsDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # hide row numbers
        self.AddQuestsTableWidget.verticalHeader().setVisible(False)

        self.last_category = None
        self.last_dlc = None

        self.add_quest_row()

    def add_quest_row(self):
        row_position = self.AddQuestsTableWidget.rowCount()
        self.AddQuestsTableWidget.insertRow(row_position)

        # update defaults for Category and DLC and carry them over to the next new row
        if row_position > 0:
            last_row_index = row_position - 1
            self.last_category = self.AddQuestsTableWidget.item(last_row_index, 1)
            self.last_dlc = self.AddQuestsTableWidget.item(last_row_index, 2)

        if self.last_category:
            self.AddQuestsTableWidget.setItem(row_position, 1, QTableWidgetItem(self.last_category))
        if self.last_dlc:
            self.AddQuestsTableWidget.setItem(row_position, 2, QTableWidgetItem(self.last_dlc))

        # when a new row is added, make it so user can immediately begin typing in newest Quests cell
        self.AddQuestsTableWidget.setCurrentCell(row_position, 0)
        self.AddQuestsTableWidget.setFocus()

    def keyPressEvent(self, event):
        # i think i need to inherit from QWidget for this to work, but I'll see
        # also the key stroke values aren't right, or aren't coming from the right class
        if (event.key() == Qt.Key_Return) or (event.key() == Qt.Key_Enter):
            self.add_quest_row()
        elif event.key() == Qt.Key_V and (event.modifiers() & Qt.ControlModifier):
            self.handle_paste_event()
        else:
            super().keyPressEvent(event)

    def handle_paste_event(self):
        clipboard = QApplication.clipboard()
        pasted_data = clipboard.text()

        rows = pasted_data.split('\n')

        for row_data in rows:
            columns = row_data.split('\t')

            if len(columns) >= 1:
                row_position = self.AddQuestsTableWidget.rowCount() - 1
                self.AddQuestsTableWidget.insertRow(row_position)

                self.AddQuestsTableWidget.setItem(row_position, 0, QTableWidgetItem(columns[0]))
                if len(columns) > 1:
                    self.AddQuestsTableWidget.setItem(row_position, 1, QTableWidgetItem(columns[1]))
                    self.last_category = columns[1]
                if len(columns) > 2:
                    self.AddQuestsTableWidget.setItem(row_position, 2, QTableWidgetItem(columns[2]))
                    self.last_dlc = columns[2]
