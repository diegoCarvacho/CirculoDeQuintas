# este es el programa que se cargaria en el boot.py
# dependiendo de la position de un rotary switch (GPIOs Inputs) se eligirá una version distinta del codigo a ejecutar.

# import machine
# from machine import Pin

# pinMode1 = machine.Pin(1, mode = Pin.IN, pull= Pin.PULL_UP)
# pinMode2 = machine.Pin(2, mode = Pin.IN, pull= Pin.PULL_UP)
# pinMode3 = machine.Pin(3, mode = Pin.IN, pull= Pin.PULL_UP)


# playMode: int
# if pinMode1.value() is 0:
#     playMode = 0
#     import temp
# elif pinMode2.value() is 0:
#     playMode = 1
# elif pinMode3.value() is 0:
#     playMode = 2

playMode = 2
print ("program selecet")
import temp