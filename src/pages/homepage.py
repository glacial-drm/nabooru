import os, sys

from PySide6.QtGui import QPixmap
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QSlider, QSpinBox, QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget

from pages.subpages import tagsearch, imagegrid

# Eventually replaced with db
dir = 'E:/Downloads/ref/Navia'
dir_list = os.listdir(dir)

class HomePage(QWidget): # contain all the images or contain window that contains all images
    def __init__(self, manager:QMainWindow, switcher:QStackedWidget, filePaths:list[str]):
        super().__init__()

        
        # new
        self.windowManager = manager
        self.windowSwitcher = switcher
        self.filePaths = filePaths
        
        # HBox of widgets
            # search widget
            # img grid widget

        self.layout_ = QHBoxLayout(self)

        # Left search widget
        left_search = tagsearch.SearchWidget()
        self.layout_.addWidget(left_search)
        
        # Main Widget (image grid)
            # check if filepaths is empty, queue tutorial / add files dialog -----------------------------------------------
        main_grid = imagegrid.ImageGrid(3, 8, 200, self.filePaths)
        self.layout_.addWidget(main_grid)

        

        # self.setLayout(self.layout_) # verify how this works (as opposed to passing self into widget constructor)


  
class DemoScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Function to add widget with label
        def add_widget_with_label(layout, widget, label_text):
            hbox = QHBoxLayout()
            label = QLabel(label_text)
            hbox.addWidget(label)
            hbox.addWidget(widget)
            layout.addLayout(hbox)

        #QImage
        self.image = QLabel('img')
        pixmap = QPixmap(dir+'/'+dir_list[5])
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio) 
        self.image.setPixmap(pixmap)
        add_widget_with_label(main_layout, self.image, 'QImage:')

        # QLabel
        self.label = QLabel('Hello PySide6!')
        add_widget_with_label(main_layout, self.label, 'QLabel:')

        # QPushButton
        self.button = QPushButton('Click Me')
        self.button.clicked.connect(self.on_button_clicked)
        add_widget_with_label(main_layout, self.button, 'QPushButton:')

        # QLineEdit
        self.line_edit = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit, 'QLineEdit:')

        # QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
        add_widget_with_label(main_layout, self.combo_box, 'QComboBox:')

        # QSlider
        self.slider = QSlider()
        add_widget_with_label(main_layout, self.slider, 'QSlider:')

        # QSpinBox
        self.spin_box = QSpinBox()
        add_widget_with_label(main_layout, self.spin_box, 'QSpinBox:')

        # QProgressBar
        self.progress_bar = QProgressBar()
        add_widget_with_label(main_layout, self.progress_bar, 'QProgressBar:')

    def on_button_clicked(self):
        self.label.setText('Button Clicked!')