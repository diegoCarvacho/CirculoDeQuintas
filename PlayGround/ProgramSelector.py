# este es el programa que se cargaria en el boot.py
# dependiendo de la position de un rotary switch (GPIOs Inputs) se eligirá una version distinta del codigo a ejecutar.

import machine
from machine import Pin

mode1 = machine.Pin(1, mode = Pin.IN, pull= Pin.PULL_UP)
mode2 = machine.Pin(2, mode = Pin.IN, pull= Pin.PULL_UP)

selectedMode = 