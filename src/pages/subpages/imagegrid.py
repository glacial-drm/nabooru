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
        self.total_pages = ceil(len(file_paths) / (x_grid*y_grid))
        
        self.max_var_pages = 9 # number of pages in navigation bar excluding the start and end pages

        # QGridLayout should contain both image grid and navigation arrows/nums
            # Navigation items should fill the entire last row_i
        self.layout_ = QGridLayout(self) # maybe this doesn't have to be stored, we just set layout and call using built-in layout (non underscore) ---------


        if self.file_paths == []:
            # Dialog that gets user to add a new file path
            pass
        
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
        # print(image_path)
        return QPixmap(image_path)
    
    def get_image_path(self):
        pass
    def get_image_name(self):
        pass
    def get_image(self):
        pass
    
    def update_image_grid(self, new_page_index:int): # wrapper for functions that update the image grid
        self.update_grid_page(new_page_index)
        self.update_grid_navigation()

    def update_grid_page(self, new_page_index:int):
        # image grid navigation can't be out of index range
            # grey out buttons if they can't be activated

        # ignore new_page_index if shift is impossible (current pos is either end of array)
            # flag and display this to the user somehow using colour

        
        # take new image position based on the page number the user clicked, or left/right (-index, +index)
            # using a new_page_index int
                #  0 reserved for first page, -1 for last page
        print(new_page_index)
        if new_page_index < 0 or new_page_index > self.total_pages-1:
            print("New page index out of range")
            return 
        
        self.current_page_index = new_page_index
        file_path_indexer = self.current_page_index * (self.x_grid*self.y_grid)
        
        self.clear_image_grid()
        self.create_image_grid(self.file_paths[file_path_indexer:])
    def update_grid_navigation(self):
        '''Updates the elements of the navigation bar based on the current_page_index'''
        # change text for buttons
            # if on the last page, don't display more buttons
        # change active buttons
            # if on last page, the user can't use the > or >> buttons
        # change ... placements

        # reassign numbers to buttons when a new button is clicked (no need to store a billion references) 

        # only display ...s and center page number buttons if we have more pages to display than the max displayed at a given time
        if self.total_pages > self.max_var_pages:
            self.update_navigation_buttons()
            self.update_navigation_ellipses()

    def update_navigation_buttons(self):
        # CASES
            # right ... is shown, left ... isn't shown
                # Default case
                # Clicking on button < midpoint doesn't change buttons
                # Clicking on button > midpoint changes to case when both are shown
                    # Doesn't update to case when neither, or left... but not right...
                        # Create these cases based on 
            # left ... is shown, right ... isn't shown
                # 
            # both ...s are shown
                # 
            # neither are shown
                # not within this scope, buttons values aren't changed if all can be displayed at once
        
        
        # get current page index
        # iterate through buttons
            # adjust pages buttons point to
                # current page index +- increasing value
        pages_displayed_midpoint = self.max_var_pages//2
        if self.current_page_index > pages_displayed_midpoint and self.current_page_index < (self.total_pages - pages_displayed_midpoint):
            
            button_max = min(self.max_var_pages, self.total_pages)
            for i_button in range(0, button_max):
                
                new_index = - pages_displayed_midpoint + self.current_page_index + i_button
                new_btn = 'btn_'+str(i_button)
                
                self.navbar_dict[new_btn].setText(str(new_index))
                self.navbar_dict[new_btn].clicked.disconnect()
                self.navbar_dict[new_btn] = self.update_navigation_button(self.navbar_dict[new_btn], new_index-1)
        elif self.current_page_index < pages_displayed_midpoint:
            # The current default for the navbar
            # Ensure this state is reachable again
            pass
        elif self.current_page_index > (self.total_pages - pages_displayed_midpoint):
            pass
        else:
            pass

    def update_navigation_ellipses(self):
        # if current page is more than ellipses_midpoint away from left, or from right
            # display ...
        pages_displayed_midpoint = self.max_var_pages//2
    
        # Separate ifs as each statement is independent and both can occur in the same check
        if self.current_page_index > pages_displayed_midpoint:
            self.navbar_dict['ellipses_start'].show()
        else:
            self.navbar_dict['ellipses_start'].hide()    
        
        if self.current_page_index < (self.total_pages - pages_displayed_midpoint):
            self.navbar_dict['ellipses_end'].show()
        else:
            self.navbar_dict['ellipses_end'].hide()
    
    def create_image_grid(self, file_paths:list[str]): 
        '''Create a default image grid, displaying the first page (n images) of the image list'''

        for row_i in range(self.x_grid):
            
            for col_i in range(self.y_grid):
                
                file_list_index = row_i*self.y_grid + col_i

                if file_list_index >= len(file_paths): # return if no more images    
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
        '''Create a default image grid, setting navigation to the first page of the image list'''
        # implementation
            # < and > buttons
                # pass new_page_index = current page +/- 1
            # first and last buttons
                # start and end pages (1 and self.total_pages)
            # ... labels
                # if current page > 5 or < total_pages-5
                    # display corresponding ...
                # user can still skip to first and last
            # other numbered buttons
                # pass number as new_page_index
                
                # current page is the central button
                # 

        naviagation_bar = QHBoxLayout()
        self.navbar_dict = {} # define as empty in constructor -----

        # Grid left-shift (show previous page)
        self.navbar_dict['btn_ls'] = self.update_navigation_button_shift(QPushButton('<'), -1)
        naviagation_bar.addWidget(self.navbar_dict['btn_ls'])
        
        # Grid first page (btn_1/page_0)
        self.navbar_dict['btn_start'] = self.update_navigation_button(QPushButton(str(1)), 0)
        naviagation_bar.addWidget(self.navbar_dict['btn_start'])

        # Ellipses (...) after first page
        self.navbar_dict['ellipses_start'] = QLabel('...')
        self.navbar_dict['ellipses_start'].hide()
        naviagation_bar.addWidget(self.navbar_dict['ellipses_start'])
        
        
        # Variable buttons (variable total and change value based on current_page_index)
        button_max = min(self.max_var_pages, self.total_pages) # minimum between preset number (user config?) and total pages in corpus
        for i_button in range(0, button_max):
            
            # var btns are range 0 - n
                # string passed to QPushButton is i+2, denoting page 2 onward, as page 1 is defined separately
                # page_index is i+1 for same reason above, with button n corresponding to page n-1 (as pages are indexes)
            self.navbar_dict['btn_'+str(i_button)] = self.update_navigation_button(QPushButton(str(i_button+2)), i_button+1)
            naviagation_bar.addWidget(self.navbar_dict['btn_'+str(i_button)])
            
        # Ellipses (...) before last page
        self.navbar_dict['ellipses_end'] = QLabel('...')
        self.navbar_dict['ellipses_end'].hide()
        naviagation_bar.addWidget(self.navbar_dict['ellipses_end'])

        # Grid last page
        if self.total_pages > button_max:
            self.navbar_dict['btn_end'] = self.update_navigation_button(QPushButton(str(self.total_pages)), self.total_pages-1)
            naviagation_bar.addWidget(self.navbar_dict['btn_end'])

        # Grid right-shift (show next page)
        self.navbar_dict['btn_rs'] = self.update_navigation_button_shift(QPushButton('>'), 1)
        naviagation_bar.addWidget(self.navbar_dict['btn_rs'])

        self.layout_.addLayout(naviagation_bar, self.x_grid, 0, 1, self.y_grid)
     
    def update_navigation_button(self, btn:QPushButton, page_index:int):
        '''Function returns a QPushButton that navigates to a specified page index'''
        btn.clicked.connect(lambda: self.update_image_grid(page_index))
        return btn
    def update_navigation_button_shift(self, btn:QPushButton, shift:int):
        '''Function returns a QPushButton that shifts the current_page by a provided "shift" int'''
        btn.clicked.connect(lambda: self.update_image_grid(self.current_page_index+shift))
        return btn