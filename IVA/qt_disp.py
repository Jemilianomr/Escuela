# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PyQt5.QtWidgets import (
    QApplication, 
    QPushButton, 
    QMainWindow,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QWidget,
    QSpinBox,
    QComboBox,
    QMessageBox,
    QFileDialog
    )
from PyQt5.QtCore import Qt, QTimer
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import serial
import numpy as np
import glob

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
        
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toogled)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        print("clicked")
        new_window_title = choice(window_titles)
        print("Setting title: %s" %(new_window_title))
        self.setWindowTitle(new_window_title)
        
    def the_window_title_changed(self, window_title):
        print("window title changed: %s" %(window_title))
        if(window_title == "Something went wrong"):
            self.button.setDisabled(True)
        
    # def the_button_was_toogled(self, checked):
    #     print("checked?", checked)
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec_()        