import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from pages import homepage
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

        self.widgetSwitcher = QStackedWidget()
        self.setCentralWidget(self.widgetSwitcher)
        
        # issue: no intrinsic means to switch between pages
            # pass stackedWidget for all pages we can switch between using signals
                # we call add widget(self) within child widget
            # also pass this class as a parent to contain page-index mapping
                

                # call change signal to desired page based on index within stackedWidget
                    # we need to store indices in some way
                        # do we hardcode to specify the desired widget
                            # do we do this here and pass the parent as a reference?
                            # or do we create a parent page class that provides this method

        # instantiate naviagation bar and footer
        
        # instantiate pages
            # splash page
            # main page
            # search page
            # image page
            # tag page
        
        # each page has to be (wrapped in) a widget that we can put within the widgetSwitcher (stackedwidget)
            # this results in each page being a layout wrapped within some widget
        self.homePage = homepage.HomePage(self, self.widgetSwitcher, self.fileDB.get_db_filepaths())
        self.widgetSwitcher.addWidget(self.homePage)

        self.pages = {
            'home': self.homePage
        }
        
        self.switch_window('home')
        self.show()
        sys.exit(app.exec())
    
    def switch_window(self, ref:str):
        if ref not in self.pages:
            return "widget not found"
        
        widget = self.pages[ref]
        self.widgetSwitcher.setCurrentWidget(widget)


if __name__ == "__main__":
    main()