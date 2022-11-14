#this class will be used for selecting the operating mode of the circle.
#the class receives a value as parameter indicating which program mode should be selected.

import machine
from machine import Pin

#define Pins
#4 pins will be used for a binary representation of the  mode. 2^4 = 16 possible modes.
modeSelectorPin0 = machine.Pin(5, machine.Pin.IN, pull = Pin.PULL_UP)
modeSelectorPin1 = machine.Pin(6, machine.Pin.IN, pull = Pin.PULL_UP)
modeSelectorPin2 = machine.Pin(7, machine.Pin.IN, pull = Pin.PULL_UP)
modeSelectorPin3 = machine.Pin(8, machine.Pin.IN, pull = Pin.PULL_UP)

#posible modes:
#(mode : modeNumber, name)
mode1 : tuple = (1, 'Gate')
mode2 : tuple = (2, 'Latch')
mode3 : tuple = (3, 'Clock')
mode4 : tuple = (4, 'tbd')

#function for reading state of the rotary switch
def getProgramMode():

    print('Getting Program Mode...')
    
    #read GPIOs
    bit0 = int(modeSelectorPin0.value)
    bit1 = int(modeSelectorPin1.value)
    bit2 = int(modeSelectorPin2.value)
    bit3 = int(modeSelectorPin3.value)
    print('bit3 = ', bit3, 'bit2 = ', bit2, 'bit1 = ', bit1, 'bit0 = ', bit0)

    result : int = bit0 | bit1 << 1 | bit2 << 2 | bit3 << 3
    print('result = ', result)

    if result == 1:
        return(mode1)
    elif result == 2:
        return(mode2)
    elif result == 3:
        return(mode3)

