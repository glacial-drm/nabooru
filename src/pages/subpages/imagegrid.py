from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
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
        
        self.current_image_index = 0
        
        # QGridLayout should contain both image grid and navigation arrows/nums
            # Navigation items should fill the entire last row_i
        self.layout_ = QGridLayout(self)
        
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

    def update_image_grid(self):
        # take new image position based on the page number the user clicked, or left/right (-index, +index)
        # if new_img_pos > curr_img_pos
            # rotate right | add xdim*ydim of grid to arr index
                # 
        self.current_image_index
        pass
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
    
    def create_grid_navigation(self):
        # naviagation arrows and numbers to change grid
        pass