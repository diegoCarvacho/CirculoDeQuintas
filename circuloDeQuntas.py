# para usar la libreria del Raspberry Pi Pico:
# 1.- instalar la extensión Pico-W-Go
# 2.- ir al menu View -> Command Palette -> Pico-W-Go - Configure project
# 3.- escribir: from machine import Pin, I2C

#incluir librerias necesariar para el proyecto
#import rp2
import time
import machine
from machine import UART
from machine import Pin, I2C
import mcp23017
import ustruct

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
uart = UART(0, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

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

# Crear los objetos de los Botones del circulo interior
boton_in_0 = clsBoton(Circle.Inner, 0, C3)
boton_in_1 = clsBoton(Circle.Inner, 1, C3+1)
boton_in_2 = clsBoton(Circle.Inner, 2, C3+2)
boton_in_3 = clsBoton(Circle.Inner, 3, C3+3)
boton_in_4 = clsBoton(Circle.Inner, 4, C3+4)
boton_in_5 = clsBoton(Circle.Inner, 5, C3+5)
boton_in_6 = clsBoton(Circle.Inner, 6, C3+6)
boton_in_7 = clsBoton(Circle.Inner, 7, C3+7)
boton_in_8 = clsBoton(Circle.Inner, 8, C3+8)
boton_in_9 = clsBoton(Circle.Inner, 9, C3+9)
boton_in_10 = clsBoton(Circle.Inner, 10, C3+10)
boton_in_11 = clsBoton(Circle.Inner, 11, C3+11)

# Crear los objetos de los Botones del circulo exterior
boton_out_0 = clsBoton(Circle.Outter, 0, C3)
boton_out_1 = clsBoton(Circle.Outter, 1, C3+1)
boton_out_2 = clsBoton(Circle.Outter, 2, C3+2)
boton_out_3 = clsBoton(Circle.Outter, 3, C3+3)
boton_out_4 = clsBoton(Circle.Outter, 4, C3+4)
boton_out_5 = clsBoton(Circle.Outter, 5, C3+5)
boton_out_6 = clsBoton(Circle.Outter, 6, C3+6)
boton_out_7 = clsBoton(Circle.Outter, 7, C3+7)
boton_out_8 = clsBoton(Circle.Outter, 8, C3+8)
boton_out_9 = clsBoton(Circle.Outter, 9, C3+9)
boton_out_10 = clsBoton(Circle.Outter, 10, C3+10)
boton_out_11 = clsBoton(Circle.Outter, 11, C3+11)

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
noteOn = 0x90
noteOff = 0x80
noteVelocity = 127

def SendSingleNote(note, OnOff):
    if OnOff is False:
        uart.write(ustruct.pack("bbb", noteOn, note, noteVelocity))
    else:
        uart.write(ustruct.pack('bbb', noteOff, note, noteVelocity))
        
def SendMajorChord(nota, OnOff):
    if OnOff is False:
        print("SendMajorChord: ", nota, "On")
    else:
        print("SendMajorChord: ", nota, "Off")
    SendSingleNote(nota, OnOff)
    SendSingleNote(nota + 4, OnOff)
    SendSingleNote(nota + 7, OnOff)

def SendMinorChord(nota, OnOff):
    if OnOff is False:
        print("SendMinorChord: ", nota, "On")
    else:
        print("SendMinorChord: ", nota, "Off")
    SendSingleNote(nota, OnOff)
    SendSingleNote(nota + 3, OnOff)
    SendSingleNote(nota + 7, OnOff)

#PrintCircleState(mcpOutterCircle, outterCircleList)
#PrintCircleState(mcpInnerCircle, innerCircleList)


#main loop
while True:
    #startTime = time.ticks_cpu()
    for boton in innerCircleList:
        if mcpInnerCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            SendMinorChord(boton.note, boton.state)
        
    for boton in outterCircleList:
        if mcpOutterCircle.pin(boton.pin) != boton.state:
            boton.state = not boton.state
            SendMajorChord(boton.note, boton.state)

    time.sleep(1)
    print("...")
    #endTime = time.ticks_cpu() - startTime
    #print("endTime: ", endTime)

print("END")
import sys
sys.exit()