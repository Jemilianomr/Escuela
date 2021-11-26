# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:50:35 2021

Programa para leer un dato del ADC de la placa
RPI pico cada segundo.
El LED interno de la placa cada dos segundos.
Se guardan los datos aquiridos en una memoria 
micro SD.
Los datos se despliegan en una pantalla OLED

@author: josue_montero
"""

from machine import Pin, UART, Timer, I2C, ADC, SPI

import framebuf
import sdcard
import uos
import time

# Abrir el puerto serie del módulo serie-USB
uart0 = UART(0, baudrate = 9600, tx = Pin(0), rx = Pin(1))

# Declarar LED interno de la placa como una salida
led = Pin(25, Pin.OUT)

# Creación del Timer
timer = Timer()

# Crear el onjeto ADC

adc = ADC(0)

# Valores para hacer la conversión a tensión

logic_level = 3.3
board_resolution = (2**16)-1

# Resolución del display OLED
WIDTH = 128
HEIGHT = 64

# Objeto I2C

i2c = I2C(0)

time.sleep(0.1)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Logo RPI
buffer = bytearray()

# Cargar logo en el frame buffer
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Asignar la terminal cs al pin 31 e iniciar en alto (SD card)
cs = Pin(13, Pin.OUT)

spi = SPI(1,
          baudrate = 1000000,
          polarity = 0,
          phase = 0,
          bits = 8,
          firstbit = SPI.MSB,
          sck = Pin(10),
          mosi = Pin(11),
          miso = Pin(12))

# Iniciar la tarjeta SD
sd = sdcard.SDCard(spi, cs)

# Montarel archivo de sistema
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

values = []
count = 0

def tick(timer):
    pass

timer.init(freq = 1, mode = Timer.PERIODIC, callback = tick)





















