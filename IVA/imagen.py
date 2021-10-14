# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PyQt5.QtWidgets import (
    QApplication, 
    QLabel, 
    QMainWindow)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt 
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("otje.jpg"))
        widget.setScaledContents(True)
        
        self.setCentralWidget(widget)
        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec_()        