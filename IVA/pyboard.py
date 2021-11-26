# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:51:54 2021

@author: josue_montero

Generación de una señal sinusoidal de 400Hz

placa: pyboard
"""

from pyb import DAC
from math import sin, pi

dac = DAC(1) # Pin x5

buf = bytearray(100)

for i in range(len(buf)):
    buf[i] = 128 + int(127*sin(2*pi*i/len(buf)))
    
dac.write_timed(buf, 400*len(buf), mode = DAC.CIRCULAR)