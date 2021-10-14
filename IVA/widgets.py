# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PyQt5.QtWidgets import (
    QApplication, 
    QDial, 
    QMainWindow)
from PyQt5.QtCore import QSize, Qt 
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)
        
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, i):
        print(i)
    
    def slider_position(self, p):
        print("Position: ",p)
    
    def slider_pressed(self):
        print("Pressed!")
        
    def slider_released(self):
        print("Released!")
        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec_()        