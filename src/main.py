from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QToolBar,QAction

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("File Organizer")
        self.setFixedSize(QSize(400,300))
        # self.resize(400,300)
        self._createMenuBar()
        self._createActions()
        
        self.centralWidget = QLabel("Hello, World")
        self.setCentralWidget(self.centralWidget)
        
    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        # add menus
        menuBar.addMenu(QMenu("&Settings",self))
        menuBar.addMenu(QMenu("&Help", self))
        
        self.addToolBar("Settings")
        self.addToolBar("Help")
        
        
        self.setMenuBar(menuBar)
    
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()   #windows are hidden by default
    app.exec_() # event loop