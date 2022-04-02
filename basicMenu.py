# importing necessary medules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

# instanialted our class for the own GUI:
class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        
    def initialize_ui(self):
        """
        Initialize the windaow and display its contents to the screen.
        """
        