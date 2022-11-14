#incluir librerias necesariar para el proyecto
import time
import machine
from machine import UART
from machine import Pin, I2C
import mcp23017
import ustruct
import allMidiNotes
from allMidiNotes import MidiNotesList
import programMode_BotonVersion

LED = machine.Pin(25, machine.Pin.OUT)

pressed = False
notPressed = True
octava : int = 4
circleOffset : int = 3

noteOn = 0x90
noteOff = 0x80
noteVelocity = 0x46

#CLASS
class Circle:
    Inner = 1
    Outer = 2

class clsBoton:
    def __init__(self, circle: int, pin: int, scaleDegree : int, state : bool = True):
        self.circle = circle
        self.pin = pin
        self.scaleDegree = scaleDegree
        self.state = True


# Crear Objeto Uart para poder enviar datos por el puerto serial (midi)
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


# Crear los objetos de los Botones del circulo exterior
boton_out_0 = clsBoton(Circle.Outer, 0, 0)
boton_out_1 = clsBoton(Circle.Outer, 1, 7)
boton_out_2 = clsBoton(Circle.Outer, 2, 2)
boton_out_3 = clsBoton(Circle.Outer, 3, 9)
boton_out_4 = clsBoton(Circle.Outer, 4, 4)
boton_out_5 = clsBoton(Circle.Outer, 5, 11)
boton_out_6 = clsBoton(Circle.Outer, 6, 6)
boton_out_7 = clsBoton(Circle.Outer, 7, 1)
boton_out_8 = clsBoton(Circle.Outer, 8, 8)
boton_out_9 = clsBoton(Circle.Outer, 9, 3)
boton_out_10 = clsBoton(Circle.Outer, 10, 10)
boton_out_11 = clsBoton(Circle.Outer, 11, 5)

# Crear los objetos de los Botones del circulo interior
boton_in_0 = clsBoton(Circle.Inner, 0, 9)
boton_in_1 = clsBoton(Circle.Inner, 1, 4)
boton_in_2 = clsBoton(Circle.Inner, 2, 11)
boton_in_3 = clsBoton(Circle.Inner, 3, 6)
boton_in_4 = clsBoton(Circle.Inner, 4, 1)
boton_in_5 = clsBoton(Circle.Inner, 5, 8)
boton_in_6 = clsBoton(Circle.Inner, 6, 3)
boton_in_7 = clsBoton(Circle.Inner, 7, 10)
boton_in_8 = clsBoton(Circle.Inner, 8, 5)
boton_in_9 = clsBoton(Circle.Inner, 9, 1)
boton_in_10 = clsBoton(Circle.Inner, 10, 7)
boton_in_11 = clsBoton(Circle.Inner, 11, 2)

# Crear lista que incluya todos los botones
innerCircleList = [boton_in_0, boton_in_1, boton_in_2, boton_in_3, boton_in_4, boton_in_5, boton_in_6, boton_in_7, boton_in_8, boton_in_9, boton_in_10, boton_in_11]
OuterCircleList = [boton_out_0, boton_out_1, boton_out_2, boton_out_3, boton_out_4, boton_out_5, boton_out_6, boton_out_7, boton_out_8, boton_out_9, boton_out_10, boton_out_11]

# Function para impimir el estado de un circulo completo (12 Botones)
def PrintCircleState(mcp, circle):
    for boton in circle:
        if mcp.pin(boton[1]) is False:
            print(boton[0] , "\t is ON")
        else:
            print(boton[0], "\t is OFF")

#Send a global Note Off Command
def SendAllNotesOff():
    uart.write(ustruct.pack('bbb', 0xB0, 0x7B, 0))

#Send a Note On/Off Command
def SendSingleNote(note, OnOff):
    LED.toggle()
    if OnOff is pressed:
        uart.write(ustruct.pack("bbb", noteOn, note, noteVelocity))
    else:
        uart.write(ustruct.pack('bbb', noteOff, note, noteVelocity))

#Send 3 Notes corresponding to a major chord            
def SendMajorChord(boton : clsBoton):
    #calculate note to send based on boton pressed, selected octave  and circle offset
    rootNote = boton.scaleDegree + (12 * octava) + circleOffset

    if boton.state is pressed:
        print(MidiNotesList[rootNote][1], "\tmajor ", "On")
    else:
        print(MidiNotesList[rootNote][1], "\tmajor ", "Off")

    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 4, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 11, OnOff)

#Send 3 Notes corresponding to a minor chord            
def SendMinorChord(boton : clsBoton):
    #calculate note to send based on boton pressed, selected octave  and circle offset
    rootNote = boton.scaleDegree + (12 * octava) + circleOffset

    if boton.state is False:
        print(MidiNotesList[rootNote][1], "\tminor ", "On")
    else:
        print(MidiNotesList[rootNote][1], "\tminor ", "Off")
    
    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 3, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 10, OnOff)


def SendChord_GateMode(boton : clsBoton):
    if boton.circle is Circle.Outer:
        SendMajorChord(boton)
    elif boton.circle is Circle.Inner:
        SendMinorChord(boton)

def SendChord_LatchMode(boton : clsBoton):
    if boton.state is pressed:
        SendAllNotesOff()
        if boton.circle is Circle.Outer:
            SendMajorChord(boton)
        elif boton.circle is Circle.Inner:
            SendMinorChord(boton)

#PrintCircleState(mcpOuterCircle, outerCircleList)
#PrintCircleState(mcpInnerCircle, innerCircleList)

def BotonStateChanged(boton : clsBoton):
    #check SelectedMode and act accordingly
    if SelectedMode is GateMode:
        SendChord_GateMode(boton)
    elif SelectedMode is LatchMode:
        SendChord_LatchMode(boton)


#######################################################
# Main loop
#######################################################
print("Running Circulo de Quintas. Selected Mode: ", SelectedMode, ". octava : ", octava, ". Circle offset : ", circleOffset)
SendAllNotesOff()
ReadProgramMode()
while True:
    # Outer Circle (Major chords)
    for boton in OuterCircleList:
        if mcpOuterCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            BotonStateChanged(boton)

    # Inner Circle (Minor chords)
    for boton in innerCircleList:
        if mcpInnerCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            BotonStateChanged(boton)