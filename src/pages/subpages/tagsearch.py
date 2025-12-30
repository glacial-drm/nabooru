from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel

# contains embedded search bar for tags and example tags below (either related or recent tags)
# similar to the left hand side of a booru
class SearchWidget(QWidget): # (search, recent tags)
    def __init__(self):
        super().__init__()
        
        self.mainLayout = QVBoxLayout(self)
        
        # search bar
        self.line_edit = QLineEdit()
        self.mainLayout.addWidget(self.line_edit)

        # list of tags
        self.label = QLabel('SearchWidget')
        self.mainLayout.addWidget(self.label)