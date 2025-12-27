import os, sys
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QSlider, QSpinBox, QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout

# Eventually replaced with db
dir = 'E:/Downloads/ref/Navia'
dir_list = os.listdir(dir)

class HomeScreen(QMainWindow): # contain all the images or contain window that contains all images
    def __init__(self):
        super().__init__()

        # HBox of widgets
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)
        
        self.setCentralWidget(self.mainWidget)

        # Left Search Widget
        self.searchWidget = SearchWidget(self)
        self.mainLayout.addWidget(self.searchWidget)

        # Main Widget
        self.HomeWidget = HomeWidget()
        self.mainLayout.addWidget(self.HomeWidget)

class HomeWidget(QWidget): # contains all images, or welcome page, or something idk
    def __init__(self):
        super().__init__()
        
        self.mainLayout = QHBoxLayout(self)
        
        # Grid of images 8x3
        # self.imageGrid = self.create_image_grid()

        
        # Navigation Arrows / Page Numbers


        # self.image = QLabel('img')
        # pixmap = QPixmap(dir+'/'+dir_list[5]).scaled(500, 1000, QtCore.Qt.KeepAspectRatio) 
        # self.image.setPixmap(pixmap)

        # self.mainLayout = QVBoxLayout(self)
        # hbox = QHBoxLayout()
        # label = QLabel('label2')
        # hbox.addWidget(label)
        # hbox.addWidget(self.image)

        # self.mainLayout.addLayout(hbox)

    def rotate_image_grid(self):
        # if new_img_pos > curr_img_pos
            # rotate right | add xdim*ydim of grid to arr index
                # 
        pass
    def update_image_grid(self):
        # take new index and display corresponding new images
        pass
    def create_image_grid(self, x:int, y:int, dimension:int, images:list[str]): 
        grid = QGridLayout(self)
        
        for i in range(x):
            
            for j in range(y):

                if i*x + j+1 > len(images): # return if no more images
                    return

                # image list stores references to paths (as well as other data)
                    # we don't want to store a dict of images bozo
                        # fetch from json?
                            # json stores tags
                                # makes tag search (whole point of program) awful
                            # json stores comments?
                            # we get exif data during runtime
                        # fetch from db
                            # makes tag search based
                            # how do we store comments
                    # get image function to return path of image
                
                # pixmap = QPixmap(dir+'/'+dir_list[5]).scaled(500, 1000, QtCore.Qt.KeepAspectRatio) 
                # grid.addWidget(QLabel.setPixmap(pixmap))

        # start from i = 0 in list
            # what if list len less than x*y
            # return pos?
        
        # return reference to grid

    def getImage(self):
        # take image title
        # use to index storage and get path
        # return image pixmap (unscaled)
        pass
        

class SearchWidget(QWidget): # Dock Window left (search, recent tags)
    def __init__(self, parentWidget:QMainWindow):
        super().__init__()
        
        self.mainLayout = QVBoxLayout(self)
        # search bar

        # list of tags

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

# Run the application
app = QApplication(sys.argv)
# window = DemoScreen()
window = HomeScreen()
window.show()
sys.exit(app.exec())