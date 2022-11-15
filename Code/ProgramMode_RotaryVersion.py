#this class will be used for selecting the operating mode of the circle.
#the class receives a value as parameter indicating which program mode should be selected.

import machine
import time
from machine import Pin

# class clsMode:
#     mode0 : tuple = (0, 'Gate')
#     mode1 : tuple = (1, 'Latch')
#     mode2 : tuple = (2, 'Clock')
#     mode4 : tuple = (3, 'tbd')
    
#     allModes = []

#     def __init__(self, pinNumber: int, mode : tuple):
#         self.pinNumber = pinNumber
#         self.pin = Pin
#         self.mode = mode
#         self = machine.Pin(pinNumber, machine.Pin.IN, pull = Pin.PULL_UP)
#         clsMode.allModes.append(self)

# #declare posible modes
# programmMode0 = clsMode (6, clsMode.mode0)
# programmMode1 = clsMode (7, clsMode.mode1)
# programmMode2 = clsMode (8, clsMode.mode2)

# #default Mode = Mode1
# selectedMode : clsMode = programmMode0


#define modeSelectorPins
selectorMode0 = machine.Pin(6, mode= Pin.IN, pull= Pin.PULL_DOWN)
selectorMode1 = machine.Pin(7, mode= Pin.IN, pull= Pin.PULL_DOWN)
selectorMode2 = machine.Pin(8, mode= Pin.IN, pull= Pin.PULL_DOWN)
#function for reading state of the rotary switch
def GetProgramMode():
    if selectorMode0.value() == True:
        print('selected mode is Gate')
        return(0)
    elif selectorMode1.value() == True:
        print('selected mode is Latch')
        return(1)
    elif selectorMode2.value() == True:
        print('selected mode is Clock')
        return(2)
    else: 
        print('no mode')
        return(-1)



# while True:
#     # print('.')
#     if selectorMode0.value():
# 	    led.toggle()
#         # time.sleep(0.3)
# while(True):
#     GetProgramMode()
#     time.sleep(0.5)