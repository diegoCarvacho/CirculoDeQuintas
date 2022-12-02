import machine
from machine import Pin


class Mode:
    '''this class defines the possible modes as integers.'''
    gate : int = 0
    hold : int = 1
    clocked_gate : int = 2
    clocked_hold : int = 3



    #function for reading state of the rotary switch
    @staticmethod
    def get_selected():
        '''reads the states of the GPIOs connected to the rotary and
        selects a defined program mode accordingly.'''
        if rotary_switch_pin_0.value() is False:
            print('selected mode is Gate')
            return(Mode.gate)
        if rotary_switch_pin_1.value() is False:
            print('selected mode is Hold')
            return(Mode.hold)
        if rotary_switch_pin_2.value() is False:
            print('selected mode is Clocked Gate')
            return(Mode.clocked_gate)
        if rotary_switch_pin_3.value() is False:
            print('selected mode is Clocked Hold')
            return(Mode.clocked_hold)
        
        print('mode not defined')
        return(-1)

#define modeSelectorPins
rotary_switch_pin_0 = machine.Pin(6, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_1 = machine.Pin(7, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_2 = machine.Pin(8, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_3 = machine.Pin(9, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_4 = machine.Pin(10, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_5 = machine.Pin(11, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_6 = machine.Pin(12, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_7 = machine.Pin(13, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_8 = machine.Pin(14, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_9 = machine.Pin(15, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_10 = machine.Pin(16, mode= Pin.IN, pull= Pin.PULL_UP)
rotary_switch_pin_11 = machine.Pin(17, mode= Pin.IN, pull= Pin.PULL_UP)