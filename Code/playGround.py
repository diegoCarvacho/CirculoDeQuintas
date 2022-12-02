''' Segunda Version de Circulo de Quintas.'''

# Libreries
import machine
from machine import UART
from machine import Pin, I2C
from mcp23017 import MCP23017
import ustruct
from all_midi_notes import midi_notes_list
from rotary_switch_modes import Mode

# Global variables
LED = machine.Pin(25, machine.Pin.OUT)
printer : bool = True
'''used for printing in the console.
Can be set to False if the final version of the proyect has no screen to display txt'''


pin1 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
pin2 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
pin3 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)
pin4 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
pin5 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)
pin6 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
pin7 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
pin8 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
pin9 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
pin10 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
pin11 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
pin12 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

while(True):
    print(pin1.value(), pin2.value(), pin3.value(), pin4.value(), pin5.value(), pin6.value(), pin7.value(), pin8.value(), pin9.value(), pin10.value(), pin11.value(), pin12.value())