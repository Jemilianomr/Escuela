# -*- coding: utf-8 -*-
"""
Created on Sun Nov  21 14:43:04 2021

@author: Josue Emiliano Montero Rasgado
"""

# Paquetes
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
import time

# CLase del lienzo para graficar
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent = None, width = 5, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel("Time (s)")
        self.axes.set_ylabel("Voltage (V)")
        super(MplCanvas, self).__init__(fig)

# Clase de la ventana principal
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SPM PyQt5 and Arduino")
        self.canvas = MplCanvas(self, width = 5, height = 4, dpi = 100)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.canvas)
        
        control_layout = QGridLayout()
        lbl_com_port = QLabel("COM Port:")
        lbl_samples = QLabel("Samples:")
        control_layout.addWidget(lbl_com_port, 0, 0)
        control_layout.addWidget(lbl_samples, 0, 1)
        
        self.com_port = ""
        self.cb_port = QComboBox()
        self.cb_port.addItems(self.serial_ports())
        self.cb_port.activated.connect(self.add_port)
        control_layout.addWidget(self.cb_port, 1, 0)
        
        self.samples = 1
        spb_samples = QSpinBox()
        spb_samples.setMinimum(1)
        spb_samples.setMaximum(1000)
        spb_samples.setSingleStep(1)
        spb_samples.valueChanged.connect(self.spb_samples_changed)
        control_layout.addWidget(spb_samples, 1, 1)
        
        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.start_acquisition)
        control_layout.addWidget(self.btn_start, 1, 2)
        
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.clicked.connect(self.stop_acquisition)
        control_layout.addWidget(self.btn_stop, 1, 3)
        
        main_layout.addLayout(control_layout)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.btn_start.show()
        self.btn_stop.hide()
        self.count = 0
        self.micro_board = None
        self.logic_value = 5.0
        self.board_resolution = 1023
    
    # Funcion de paro
    def stop_acquisition(self):
        print("Stop")
        self.btn_stop.hide()
        self.stp_acq = True
        self.btn_start.show()
    
    # Funcion de inicio
    def start_acquisition(self):
        print("Start")
        self.canvas.axes.clear()
        self.stp_acq = False
        self.value1 = 0
        self.value2 = 0
        try:
            self.micro_board = serial.Serial(str(self.com_port), 9600,
                                             timeout = 1)
            time.sleep(1)
            print("Conexión lista")
            self.micro_board.reset_input_buffer()
        except:
            dig_board = QMessageBox()
            dig_board.setWindowTitle("COM Port Error!")
            str_dlg_board = "The board cannot be read "
            str_dlg_board += "or it wasn't selected"
            dig_board.setText(str_dlg_board)
            dig_board.setStandardButtons(QMessageBox.Ok)
            dig_board.setIcon(QMessageBox.Warning)
            dig_board.exec_()
            self.micro_board = None
            
        if (self.com_port != "" and self.micro_board != None):
            self.btn_start.hide()
            self.btn_stop.show()
            if (self.count == 0):
                self.time_val = 0
                self.values = []
                self.t = np.asarray([])
                self.v1 = np.asarray([])
                self.v2 = np.asarray([])
                if (self.micro_board != None):
                    self.micro_board.reset_input_buffer()
                self.timer = QTimer()
                self.timer.setInterval(500)
                self.timer.timeout.connect(self.update_plot)
                self.timer.start()
                print()
                print("Time (s) \t Voltage (V)")
    
    # Funcion de generacion del grafico
    def update_plot(self):
        try:
            temp = str(self.micro_board.readline().decode('cp437'))
            temp = temp.replace("\n", "")
            temp1 = temp.split(",")
            value1 = (float(temp1[0])*(self.logic_value/self.board_resolution))
            value2 = (float(temp1[1])*(self.logic_value/self.board_resolution))
            print_console = "voltage: " + "{0:.3f}".format(value1) + " (V)"
            print_console += "voltage: " + "{0:.3f}".format(value2) + " (V)"
            print(print_console)
            self.values.append(str(self.count) + "," + 
                               "{0:.3f}".format(value1) + "," + 
                               "{0:.3f}".format(value2))
            self.t = np.append(self.t, self.count)
            self.v1 = np.append(self.v1, value1)
            self.v2 = np.append(self.v2, value2)

            self.canvas.axes.clear()
            self.canvas.axes.plot(self.t, self.v1, 'C1o--')
            self.canvas.axes.plot(self.t, self.v2, 'b-s')
            self.canvas.axes.grid(True)
            self.canvas.draw()

        except:
            pass
        
        if (self.count == self.samples or self.stp_acq == True):
            self.count = 0
            self.btn_stop.hide()
            self.btn_start.show()
            self.micro_board.close()
            self.timer.stop()
        self.count = self.count + 1
    
    # Funcion para el numero de muestras    
    def spb_samples_changed(self, val_samples):
        self.samples = val_samples
        print(self.samples)
    
    # Funcion de cambio de puerto    
    def add_port(self):
        self.com_port = str(self.cb_port.currentText())
        print(self.com_port)
        
    # Funcion de conexion serial    
    def serial_ports(self) -> list:
        if(sys.platform.startswith('win')):
            ports = ['COM%s' % (i+1) for i in range(256)]
        elif(sys.platform.startswith('linux') or sys.platform.startswith('cygwin')):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif(sys.platform.startswith('darwin')):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError("Unsupported platform")
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except(OSError, serial.SerialException):
                pass
        return result
        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()        