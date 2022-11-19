import machine
from machine import Pin


#CLASSES
class Program:
    gate : int = 0
    hold : int = 1
    clockedGate : int = 2
    clockedHold : int = 3

    # selectedMode : int = gate

    
#define modeSelectorPins
rotarySwitchPin0 = machine.Pin(6, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin1 = machine.Pin(7, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin2 = machine.Pin(8, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin3 = machine.Pin(9, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin4 = machine.Pin(10, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin5 = machine.Pin(11, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin6 = machine.Pin(12, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin7 = machine.Pin(13, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin8 = machine.Pin(14, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin9 = machine.Pin(15, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin10 = machine.Pin(16, mode= Pin.IN, pull= Pin.PULL_UP)
rotarySwitchPin11 = machine.Pin(17, mode= Pin.IN, pull= Pin.PULL_UP)

#function for reading state of the rotary switch
def GetSelectedProgramMode():
    if rotarySwitchPin0.value() == False:
        print('selected mode is Gate')
        return(Program.gate)
    elif rotarySwitchPin1.value() == False:
        print('selected mode is Hold')
        return(Program.hold)
    elif rotarySwitchPin2.value() == False:
        print('selected mode is Clocked Gate')
        return(Program.clockedGate)
    elif rotarySwitchPin3.value() == False:
        print('selected mode is Clocked Hold')
        return(Program.clockedHold)
    else: 
        print('no mode')
        return(-1)