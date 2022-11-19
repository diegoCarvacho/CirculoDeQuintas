#incluir librerias necesariar para el proyecto
import time
import machine
from machine import UART
from machine import Pin, I2C
import mcp23017
import ustruct
import allMidiNotes
from allMidiNotes import MidiNotesList
import ProgramModes_RotaryVersion
from ProgramModes_RotaryVersion import GetSelectedProgramMode, Program

# LED = machine.Pin(25, machine.Pin.OUT)


# Classes
class Midi:
    octava : int = 4
    noteOn = 0x90
    noteOff = 0x80
    noteVelocity = 0x46

class Circle:
    inner = 1
    outer = 2
    offset : int = 3  # Set according to the orientation of the circle.

class clsBoton:
    pressed = False
    notPressed = True
    def __init__(self, circle: int, scale_degree : int, state : bool = True):
        self.circle = circle
        self.scale_degree = scale_degree
        self.state = True


# Crear Objeto Uart para poder enviar datos por el puerto serial (midi)
# 31250 is the Baudrate used for MIDI
uart = UART(0, 31250)   
uart.init(31250, bits=8, parity=None, stop=1)

# Crear I2C Bus
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq = 200000)

# Crear los dos Objetos de la clase MCP23017 necesarios para los Port Expanders
mcpInnerCircle = mcp23017.MCP23017(i2c, 0x24)
mcpInnerCircle.init()
innerPins = list(range(0,12))
for pinNum in innerPins:
    mcpInnerCircle.pin(pinNum, mode= 1, pullup= True)

mcpOuterCircle = mcp23017.MCP23017(i2c, 0x20)
mcpOuterCircle.init()
OuterPins = list(range(0,12))
for pinNum in OuterPins:
    mcpOuterCircle.pin(pinNum, mode= 1, pullup= True)

outerCircleList = []
outerCircleList.append(clsBoton(Circle.inner, 0))
outerCircleList.append(clsBoton(Circle.inner, 7))
outerCircleList.append(clsBoton(Circle.inner, 2))
outerCircleList.append(clsBoton(Circle.inner, 9))
outerCircleList.append(clsBoton(Circle.inner, 4))
outerCircleList.append(clsBoton(Circle.inner, 11))
outerCircleList.append(clsBoton(Circle.inner, 6))
outerCircleList.append(clsBoton(Circle.inner, 1))
outerCircleList.append(clsBoton(Circle.inner, 8))
outerCircleList.append(clsBoton(Circle.inner, 3))
outerCircleList.append(clsBoton(Circle.inner, 10))
outerCircleList.append(clsBoton(Circle.inner, 5))

innerCircleList = []
innerCircleList.append(clsBoton(Circle.outer, 9))
innerCircleList.append(clsBoton(Circle.outer, 4))
innerCircleList.append(clsBoton(Circle.outer, 11))
innerCircleList.append(clsBoton(Circle.outer, 4))
innerCircleList.append(clsBoton(Circle.outer, 1))
innerCircleList.append(clsBoton(Circle.outer, 8))
innerCircleList.append(clsBoton(Circle.outer, 3))
innerCircleList.append(clsBoton(Circle.outer, 10))
innerCircleList.append(clsBoton(Circle.outer, 5))
innerCircleList.append(clsBoton(Circle.outer, 0))
innerCircleList.append(clsBoton(Circle.outer, 7))
innerCircleList.append(clsBoton(Circle.outer, 2))


#Send a global Note Off Command
def SendAllNotesOff():
    uart.write(ustruct.pack('bbb', 0xB0, 0x7B, 0))

#Send a Note On/Off Command
def SendSingleNote(note, OnOff):
    #LED.toggle()
    if OnOff is False:
        uart.write(ustruct.pack("bbb", Midi.noteOn, note, Midi.noteVelocity))
    else:
        uart.write(ustruct.pack('bbb', Midi.noteOff, note, Midi.noteVelocity))

#Send 3 Notes corresponding to a major chord            
def send_major_triad(boton : clsBoton):
    #calculate note to send based on boton pressed, selected octave and circle offset
    rootNote = boton.scale_degree + (12 * Midi.octava) + Circle.offset

    if boton.state is clsBoton.pressed:
        print(MidiNotesList[rootNote][1], "\tmajor ", "On")
    else:
        print(MidiNotesList[rootNote][1], "\tmajor ", "Off")

    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 4, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 11, OnOff)

#Send 3 Notes corresponding to a minor chord            
def send_minor_triad(boton : clsBoton):
    #calculate note to send based on boton pressed, selected octave  and circle offset
    rootNote = boton.scale_degree + (12 * Midi.octava) + Circle.offset

    if boton.state is False:
        print(MidiNotesList[rootNote][1], "\tminor ", "On")
    else:
        print(MidiNotesList[rootNote][1], "\tminor ", "Off")

    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 3, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 10, OnOff)


def send_chord_gate_mode(boton : clsBoton):
    if boton.circle is Circle.outer:
        send_major_triad(boton)
    elif boton.circle is Circle.inner:
        send_minor_triad(boton)

def send_chord_hold_mode(boton : clsBoton):
    if boton.state is clsBoton.pressed:
        SendAllNotesOff()
        if boton.circle is Circle.outer:
            send_major_triad(boton)
        elif boton.circle is Circle.inner:
            send_minor_triad(boton)

def boton_state_changed(boton : clsBoton):
    # check SelectedMode and act accordingly
    match GetSelectedProgramMode:
        case Program.gate:
            send_chord_gate_mode(boton)
        case Program.hold:
            send_chord_hold_mode(boton)
        # case Program.clockedGate:
        # case Program.clockedHold:

#######################################################
# Main loop
#######################################################
SendAllNotesOff()

print("Running Circulo de Quintas. Selected Mode: ", GetSelectedProgramMode(), ". octava : ", Midi.octava, ". Circle offset : ", Circle.offset)

while True:
    # Outer Circle (Major chords)
    for i in range(len(outerCircleList)):
        if mcpOuterCircle.pin(outerCircleList[i]) != outerCircleList[i].state:
            outerCircleList[i].state = not outerCircleList[i].state
            boton_state_changed(outerCircleList[i])


    # Inner Circle (Minor chords)
    for i in range(len(innerCircleList)):
        if mcpInnerCircle.pin(innerCircleList[i]) != innerCircleList[i].state:
            innerCircleList[i].state = not innerCircleList[i].state
            boton_state_changed(innerCircleList[i])


    # for boton in innerCircleList:
    #     if mcpInnerCircle.pin(boton.pin) != boton.state:
    #         boton.state = not boton.state
    #         BotonStateChanged(boton)