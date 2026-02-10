# search page for tag based search
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget

class SearchPage(QWidget):
    def __init__(self, manager:QMainWindow, switcher=QStackedWidget):
        super().__init__()

        self.windowManager = manager
        self.windowSwitcher = switcher

        # TODO Offer means to search by images