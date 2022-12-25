''' Segunda Version de Circulo de Quintas.'''

# Libreries
import machine
from machine import UART
from machine import Pin, I2C
from mcp23017 import MCP23017
import ustruct
from all_midi_notes import midi_notes_list
# from rotary_switch_modes import Mode

# Global variables
LED = machine.Pin(25, machine.Pin.OUT)
printer : bool = True
'''used for printing in the console.
Can be set to False if the final version of the proyect has no screen to display txt'''

# Classes
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
        if rotary_switch_pin_0.value() is 0:
            print('selected mode is Gate')
            return(Mode.gate)
        if rotary_switch_pin_1.value() is 0:
            print('selected mode is Hold')
            return(Mode.hold)
        if rotary_switch_pin_2.value() is 0:
            print('selected mode is Clocked Gate')
            return(Mode.clocked_gate)
        if rotary_switch_pin_3.value() is 0:
            print('selected mode is Clocked Hold')
            return(Mode.clocked_hold)
        if rotary_switch_pin_4.value() is 0:
            print('selected mode is 4')
        if rotary_switch_pin_5.value() is 0:
            print('selected mode is 5')
        if rotary_switch_pin_6.value() is 0:
            print('selected mode is 6')
        if rotary_switch_pin_7.value() is 0:
            print('selected mode is 7')
        if rotary_switch_pin_8.value() is 0:
            print('selected mode is 8')
        if rotary_switch_pin_9.value() is 0:
            print('selected mode is 9')
        if rotary_switch_pin_10.value() is 0:
            print('selected mode is 10')
        if rotary_switch_pin_11.value() is 0:
            print('selected mode is 11')
        else:
            print('mode not defined')
        return(999)

class Circle:
    ''' Class Circle just has some constants related to the circles'''
    INNER = 1
    OUTER = 2
    OFFSET : int = 9  # Set according to the orientation of the circle.

class Boton:
    
    PRESSED = False
 
    def __init__(self, circle : int, mcp : MCP23017, mcp_pin : int, chromatic_degree : int, state : bool = True):
        self.circle = circle
        self.mcp = mcp
        self.mcp_pin = mcp_pin
        self.scale_degree = chromatic_degree
        self.state = state

    def state_has_changed(self):
        if self.mcp.pin(self.mcp_pin) is not self.state:
            self.state = not self.state
            return True
        else:
            return False

class Midi:
    ''' Class Midi has the variables related to midi'''
    octave : int = 3
    '''refers to the octave used for the root not of the chord to be played'''
    note_on = 0x90
    '''byte value defined in midi protocol for sending a note on message'''
    note_off = 0x80
    '''byte value define in midi protocol for sending a note off message'''
    note_velocity = 0x46
    '''velocity with which the midi notes are sent'''

    @staticmethod
    def send_all_notes_off():
        '''Send a global note_off Command'''
        uart.write(ustruct.pack('bbb', 0xB0, 0x7B, 0))

    @staticmethod
    def send_single_note(note, on_off):
        '''Send a single note_on or note_off midi message'''
        #LED.toggle()
        if on_off is False:
            uart.write(ustruct.pack("bbb", Midi.note_on, note, Midi.note_velocity))
        else:
            uart.write(ustruct.pack('bbb', Midi.note_off, note, Midi.note_velocity))
        
        if printer is True:
            if on_off is False:
                print('send midi note_off: ', midi_notes_list[note][1])
            else:
                print('send midi note_on: ', midi_notes_list[note][1])


# Crear Objeto Uart para poder enviar datos por el puerto serial (midi)
# 31250 is the Baudrate used for MIDI
uart = UART(0, 31250)   
uart.init(31250, bits=8, parity=None, stop=1)

# Crear I2C Bus
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq = 200000)

# Crear los dos Objetos de la clase MCP23017 necesarios para los Port Expanders
mcp_outer_circle = MCP23017(i2c, 0x20)
mcp_outer_circle.init()
outer_pins = list(range(0,12))
for pin_number in outer_pins:
    mcp_outer_circle.pin(pin_number, mode= 1, pullup= True)

mcp_inner_circle = MCP23017(i2c, 0x24)
mcp_inner_circle.init()
inner_pins = list(range(0,12))
for pin_number in inner_pins:
    mcp_inner_circle.pin(pin_number, mode= 1, pullup= True)


outer_circle_botons = []
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 0, 0))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 1, 7))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 2, 2))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 3, 9))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 4, 4))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 5, 11))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 6, 6))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 7, 1))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 8, 8))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 9, 3))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 10, 10))
outer_circle_botons.append(Boton(Circle.OUTER, mcp_outer_circle, 11, 5))

inner_circle_botons = []
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 0, 9))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 1, 4))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 2, 11))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 3, 6))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 4, 1))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 5, 8))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 6, 3))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 7, 10))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 8, 5))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 9, 0))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 10, 7))
inner_circle_botons.append(Boton(Circle.INNER, mcp_inner_circle, 11, 2))


def send_triad(boton : Boton):
    '''sends 3 midi notes'''

    root_note = boton.scale_degree + (12 * Midi.octave) + Circle.OFFSET
    print("rootnote: ", root_note)
    print("circle offset: ",Circle.OFFSET)
    Midi.send_single_note(root_note + 0, boton.state)       # send root note
    if boton.circle is Circle.INNER:                        
        Midi.send_single_note(root_note + 3, boton.state)   # send minor third
    else:
        Midi.send_single_note(root_note + 4, boton.state)   # send major third
    Midi.send_single_note(root_note + 7, boton.state)       # send fifth

def send_chord_gate_mode(boton : Boton):
    '''send a chord over midi when a boton is pressed and
    stop the note when the boton is released'''
    send_triad(boton)

def send_chord_hold_mode(boton : Boton):
    '''send a chord over midi and holds it even if the boton was released.
    Only pressing a different boton will stop the first chord'''
    if boton.state is boton.PRESSED:
        Midi.send_all_notes_off()
        send_triad(boton)

def send_chord(boton : Boton):
    '''if the state of a boton has changed (pressed or released)
    a function will be called depending to the selected program'''
    mode =  Mode.get_selected()
    if mode is Mode.gate:
            send_chord_gate_mode(boton)
            print("circle: ", boton.circle)
            print("mcp_pin: ", boton.mcp_pin)
            print("scale degree: ", boton.scale_degree)
            print("circle: ", boton.circle)
    else:
        if mode is Mode.hold:
            send_chord_hold_mode(boton)
        # case Program.clockedGate:
        # case Program.clockedHold:


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


#######################################################
# House cleaning
#######################################################
Midi.send_all_notes_off()
print("Running Circulo de Quintas. Selected Mode: ", Mode.get_selected(),
". octava : ", Midi.octave, ". circle offset : ", Circle.OFFSET)

#######################################################
# Main loop
#######################################################
while True:

    for boton in outer_circle_botons:
        if boton.state_has_changed() is True:
            send_chord(boton)

    for boton in inner_circle_botons:
        if boton.state_has_changed() is True:
            send_chord(boton)

