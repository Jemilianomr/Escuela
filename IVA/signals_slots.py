# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PyQt5.QtWidgets import (
    QApplication, 
    QLabel, 
    QMainWindow, 
    QLineEdit,
    QVBoxLayout,
    QWidget)
from PyQt5.QtCore import QSize, Qt 
import sys

window_titles = [
    "MyApp",
    "Something went wrong",
    "What on earth",
    "This is surprising",
    "Still My App"
    ]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec_()        