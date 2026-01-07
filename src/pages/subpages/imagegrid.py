from math import ceil

from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
import PIL.Image

class ImageGrid(QWidget):
    def __init__(self, x_grid:int, y_grid:int, img_size:int, file_paths:list[str]):
        super().__init__()
        
        # keep in file, make function in taskbar to configure... config file?
            # with respect to a default size imagegrid?

        self.x_grid = x_grid
        self.y_grid = y_grid
        self.img_size = img_size
        self.file_paths = file_paths
        
        self.current_page_index = 0
        self.max_pages = ceil(len(file_paths) / (x_grid*y_grid))

        # QGridLayout should contain both image grid and navigation arrows/nums
            # Navigation items should fill the entire last row_i
        self.layout_ = QGridLayout(self) # maybe this doesn't have to be stored, we just set layout and call using built-in layout (non underscore) ---------
        
        # Grid of images 8x3 (default)
        self.create_image_grid(self.file_paths)

        # Navigation Arrows / Page Numbers
        self.create_grid_navigation()
    
    # overloaded constructor
        # If db is empty then display this and ask user to add images
    # @classmethod

    def focus_image_page(self):
        # get the clicked image using get_image
        # switch to image page, pass specified image in some way
            # how do we access the switcher
                # pass a parent widget that we can use to call the widget manager switch function 
        pass
    
    # get image functions take the current index and perform some function on the grid position to get the specified image
        # this gets the image using get_image, then gets further data using the get_image_xyz functions
    def pixmap_to_label(self, pixmap:QPixmap):
        label = QLabel()
        label.setPixmap(pixmap)

        return label

    def get_file_pixmap(self, image_path:str):
        print(image_path)
        return QPixmap(image_path)
    
    def get_image_path(self):
        pass
    def get_image_name(self):
        pass
    def get_image(self):
        pass
    

    def update_image_grid(self, new_page_index:int):
        # image grid navigation can't be out of index range
            # grey out buttons if they can't be activated

        # ignore new_page_index if shift is impossible (current pos is either end of array)
            # flag and display this to the user somehow using colour

        
        # take new image position based on the page number the user clicked, or left/right (-index, +index)
            # using a new_page_index int
                #  0 reserved for first page, -1 for last page
        
        if new_page_index < 0 or new_page_index > self.max_pages:
            print("New page index out of range")
            return 
        
        self.current_page_index = new_page_index
        file_path_indexer = self.current_page_index * (self.x_grid*self.y_grid)
        
        self.clear_image_grid()
        self.create_image_grid(self.file_paths[file_path_indexer:])
    
    def update_grid_navigation(self, new_page_index:int):
        # ignore new_page_index if shift is impossible (current pos is either end of array)
            # flag and display this to the user somehow using colour

        # navigation bar components include
            # arrow buttons
                # 
            # first/last page buttons
                #
            # buttons for other pages
                # other pages are present based on the length of the passed image list
            # how many until ... for more pages
                # standardise to 10

        # edit navigation bar in some way
            # change text for buttons
                # if on the last page, don't display more buttons
            # change active buttons
                # if on last page, the user can't use the > or >> buttons
            # change ... placements
        
        self.layout_.itemAtPosition(self.y_grid, 0)

    def create_image_grid(self, file_paths:list[str]): 
        
        for row_i in range(self.x_grid):
            
            for col_i in range(self.y_grid):
                
                file_list_index = row_i*self.y_grid + col_i

                if file_list_index > len(file_paths): # return if no more images    
                    return
                
                file_pixmap = self.get_file_pixmap(file_paths[file_list_index]).scaled(self.img_size, self.img_size, QtCore.Qt.KeepAspectRatio)
                file_label = self.pixmap_to_label(file_pixmap)
                
                # file_label = QLabel(str(file_list_index))

                self.layout_.addWidget(file_label, row_i, col_i)
                

        # start from i = 0 in list
            # what if list len less than row_i*col_i
            # return pos?
    def clear_image_grid(self):
        pass

    def create_grid_navigation(self):
        # implementation
            # < and > buttons
                # pass new_page_index = current page +/- 1
            # first and last buttons
                # start and end pages (1 and self.max_pages)
            # ... labels
                # if current page > 5 or < max_pages-5
                    # display corresponding ...
                # user can still skip to first and last
            # other numbered buttons
                # pass number as new_page_index
                
                # current page is the central button
                # 
            
            # reassign numbers to buttons when a new button is clicked (no need to store a billion references)

        naviagation_bar = QHBoxLayout()
    

        # Grid left-shift (show previous page)
        left_button = QPushButton('<')
        left_button.clicked.connect(lambda: self.update_image_grid(self.current_page_index-1))
        naviagation_bar.addWidget(left_button)
        
        # Grid first page
        left_end_button = QPushButton(str(1)) # button 0
        left_button.clicked.connect(lambda: self.update_image_grid(self.current_page_index-1))
        naviagation_bar.addWidget(left_end_button)

        # button array range (number of pages to navigate between)
            # should be the minimum between the maximium possible number of buttons at a given time (standard is 10) and length of array / (x_grid * y_grid)
        button_max = min(10, self.max_pages)
        for i in range(0, button_max):
            
            # start from 1 as 0th button is the '<<' button
            i_button = str(i+1)
            naviagation_bar.addWidget(QPushButton(i_button))

        # Grid last page
        right_end_button = QPushButton(str(self.max_pages)) # button -1
        naviagation_bar.addWidget(right_end_button)

        # Grid right-shift (show next page)
        right_button = QPushButton('>')
        right_button.clicked.connect(lambda: self.update_image_grid(self.current_page_index+1))
        naviagation_bar.addWidget(right_button)

        self.layout_.addLayout(naviagation_bar, self.x_grid, 0, 1, self.y_grid)
    
    def add_navigation_button(self, text:str, ):
        ''''''
        pass