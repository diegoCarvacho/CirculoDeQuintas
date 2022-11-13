#incluir librerias necesariar para el proyecto
#import rp2
import time
import machine
from machine import UART
from machine import Pin, I2C
import mcp23017
import ustruct

LED = machine.Pin(25, machine.Pin.OUT)

SelectedMode : int
GateMode = 0
HoldMode = 1
pressed = False
notPressed = True
octava : int = 12 * 1
circleOffset : int = 0

noteOn = 0x90
noteOff = 0x80
allNotesOff = 0xB0
noteVelocity = 0x46

#CLASS
class Circle:
    Inner = 1
    Outter = 2

class clsBoton:
    def __init__(self, circle: int, pin: int, note: int, state : bool = True):
        self.pin = pin
        self.circle = circle
        self.note = note
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

mcpOutterCircle = mcp23017.MCP23017(i2c, 0x20)
mcpOutterCircle.init()
outterPins = list(range(0,12))
for pinNum in outterPins:
    mcpOutterCircle.pin(pinNum, mode= 1, pullup= True)


#C3 en midi es 48. Se usará como punto de referencia para todas las otras notas
C3 = 48
Db3 = 49
D3 = 50
Eb3 = 51
E3 = 52
F3 = 53
Gb3 = 54
G3 = 55
Ab3 = 56
A3 = 57
Bb3 = 58
B3 = 59

# Crear los objetos de los Botones del circulo interior
boton_in_0 = clsBoton(Circle.Inner, 0, A3)
boton_in_1 = clsBoton(Circle.Inner, 1, E3)
boton_in_2 = clsBoton(Circle.Inner, 2, B3)
boton_in_3 = clsBoton(Circle.Inner, 3, Gb3)
boton_in_4 = clsBoton(Circle.Inner, 4, Db3)
boton_in_5 = clsBoton(Circle.Inner, 5, Ab3)
boton_in_6 = clsBoton(Circle.Inner, 6, Eb3)
boton_in_7 = clsBoton(Circle.Inner, 7, Bb3)
boton_in_8 = clsBoton(Circle.Inner, 8, F3)
boton_in_9 = clsBoton(Circle.Inner, 9, C3)
boton_in_10 = clsBoton(Circle.Inner, 10, G3)
boton_in_11 = clsBoton(Circle.Inner, 11, D3)

# Crear los objetos de los Botones del circulo exterior
boton_out_0 = clsBoton(Circle.Outter, 0, C3)
boton_out_1 = clsBoton(Circle.Outter, 1, G3)
boton_out_2 = clsBoton(Circle.Outter, 2, D3)
boton_out_3 = clsBoton(Circle.Outter, 3, A3)
boton_out_4 = clsBoton(Circle.Outter, 4, E3)
boton_out_5 = clsBoton(Circle.Outter, 5, B3)
boton_out_6 = clsBoton(Circle.Outter, 6, Gb3)
boton_out_7 = clsBoton(Circle.Outter, 7, Db3)
boton_out_8 = clsBoton(Circle.Outter, 8, Ab3)
boton_out_9 = clsBoton(Circle.Outter, 9, Eb3)
boton_out_10 = clsBoton(Circle.Outter, 10, Bb3)
boton_out_11 = clsBoton(Circle.Outter, 11, F3)

# Crear Lista que incluya todos los botones
innerCircleList = [boton_in_0, boton_in_1, boton_in_2, boton_in_3, boton_in_4, boton_in_5, boton_in_6, boton_in_7, boton_in_8, boton_in_9, boton_in_10, boton_in_11]
outterCircleList = [boton_out_0, boton_out_1, boton_out_2, boton_out_3, boton_out_4, boton_out_5, boton_out_6, boton_out_7, boton_out_8, boton_out_9, boton_out_10, boton_out_11]

# Function para impimir el estado de un circulo completo (12 Botones)
def PrintCircleState(mcp, circle):
    for boton in circle:
        if mcp.pin(boton[1]) is False:
            print(boton[0] , "\t is ON")
        else:
            print(boton[0], "\t is OFF")

# Funcion para enviar una nota por midi

def SendAllNotesOff():
    uart.write(ustruct.pack('bbb', allNotesOff, 128, 0))
def SendSingleNote(note, OnOff):
    LED.toggle()
    if OnOff is False:
        uart.write(ustruct.pack("bbb", noteOn, note, noteVelocity))
    else:
        uart.write(ustruct.pack('bbb', noteOff, note, noteVelocity))
        
def SendMajorChord(boton : clsBoton):
    #calculate note to send baed on boton pressed, selected octave  and circle offset
    rootNote = boton.pin + 1 + octava + circleOffset

    if boton.state is pressed:
        print("SendMajorChord: ", rootNote, "On")
    else:
        print("SendMajorChord: ", rootNote, "Off")

    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 4, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 11, OnOff)

def SendMinorChord(boton : clsBoton):
    #calculate note to send baed on boton pressed, selected octave  and circle offset
    rootNote = boton.pin + 1 + octava + circleOffset

    if boton.state is False:
        print("SendMinorChord: ", rootNote, "On")
    else:
        print("SendMinorChord: ", rootNote, "Off")
    
    SendSingleNote(rootNote, boton.state)
    SendSingleNote(rootNote + 3, boton.state)
    SendSingleNote(rootNote + 7, boton.state)
    #SendSingleNote(nota + 10, OnOff)


def SendChord_GateMode(boton : clsBoton):
    if boton.circle is Circle.Outter:
        SendMajorChord(boton)
    elif boton.circle is Circle.Inner:
        SendMinorChord(boton)

def SendChord_HoldMode(boton : clsBoton):
    if boton.circle is Circle.Outter:
        SendMajorChord(boton)
    elif boton.circle is Circle.Inner:
        SendMinorChord(boton)

#PrintCircleState(mcpOutterCircle, outterCircleList)
#PrintCircleState(mcpInnerCircle, innerCircleList)

def BotonStateChanged(boton):
    #check SelectedMode
    if SelectedMode is GateMode:
        SendChord_GateMode(boton)
    elif SelectedMode is HoldMode:
        SendChord_HoldMode(boton)

#main loop
while True:
    for boton in innerCircleList:
        if mcpInnerCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            BotonStateChanged(boton)
        
    for boton in outterCircleList:
        if mcpOutterCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            BotonStateChanged(boton)

    print("...")
