# importing necessary medules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

# instanialted our class for the own GUI:
class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        """
        Initialize the windaow and display its contents to the screen.
        """
        self.setGeometry(100,50, 350, 350)
        self.setWindowTitle("Basic Menu Example.")
        self.create_menu()
        
    def create_menu(self):
        """
        Create skeleton application with menubar
        """
        # Create Actions for file menu:
        exit_action = QAction("Exit",self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        # Create menubar:
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        
        # Create file menu and add actions:
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
        
        
        