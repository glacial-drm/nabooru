import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QLabel, QWidget, QToolBar
from PySide6.QtGui import QAction

from pages import homepage, searchpage
from database import FileDB

def main():
    # launch UI
    app = QApplication(sys.argv)
    WidgetManager(app)
    
class WidgetManager(QMainWindow):
    '''Determines the currently active page'''
    
    # contains navigation bar and footer (as they are independent of pages/widgets)
        # navigation bar gets pages from here to get page functions

        # how do we switch pages (within pages)
            # each page contains some pagecontroller
            # this can take the calling page as an argument to set the calling page

    def __init__(self, app:QApplication):
        super().__init__()
        self.fileDB = FileDB()

        self.windowSwitcher = QStackedWidget()
        self.setCentralWidget(self.windowSwitcher)
        
        # instantiate (top) naviagation bar and footer
        menubar = self.menuBar() # title and logo
        
        toolbar = QToolBar("Pages")
        self.addToolBar(toolbar)
        status_bar = self.statusBar()
        
        # issue: no intrinsic means to switch between pages
            # pass stackedWidget for all pages we can switch between using signals
                # we call add widget(self) within child widget
            # also pass this class as a parent to contain page-index mapping
                

                # call change signal to desired page based on index within stackedWidget
                    # we need to store indices in some way
                        # do we hardcode to specify the desired widget
                            # do we do this here and pass the parent as a reference?
                            # or do we create a parent page class that provides this method

        # instantiate pages
            # splash page
            # main page
            # search page
            # image page
            # tag page
        
        # each page has to be (wrapped in) a widget that we can put within the windowSwitcher (stackedwidget)
            # this results in each page being a layout wrapped within some widget
        self.homePage = homepage.HomePage(self, self.windowSwitcher, self.fileDB.get_db_filepaths())
        self.windowSwitcher.addWidget(self.homePage)

        self.searchPage = searchpage.SearchPage(self, self.
        windowSwitcher)
        self.windowSwitcher.addWidget(self.searchPage)
        

        self.pages = {
            'home': self.homePage,
            'search': self.searchPage
        }
        self.switch_window('home')

        # Add references to navigation bar / toolbar
        home_action = QAction("Home", self)
        home_action.triggered.connect(lambda: self.switch_window('home'))
        toolbar.addAction(home_action)

        search_action = QAction("Search", self)
        search_action.triggered.connect(lambda: self.switch_window('search'))
        toolbar.addAction(search_action)

        self.show()
        sys.exit(app.exec())

    def test_widget(self): # call this method in page class, or make a toolbar here
        # iterate through widgets
        # slice string to get name somehow
        # switch widget based on nam (using switch_window function here?)
        # profit

        # not sure if this would lead to a circular import
        count = self.windowSwitcher.count()
        for i_window in range(count):
            window = self.windowSwitcher.widget(i_window)
        
        
            if type(window) == searchpage.SearchPage:
                print("ee")

    def switch_window(self, ref:str):
        if ref not in self.pages:
            return "widget not found"
        
        widget = self.pages[ref]
        self.windowSwitcher.setCurrentWidget(widget)
    


if __name__ == "__main__":
    main()