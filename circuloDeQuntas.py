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
#from dataclasses import dataclass
# Crear Objeto Uart para poder enviar datos por el puerto serial (midi)
uart = UART(1, 9600)
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

#print(mcpOutterCircle.pin(0))

# Crear Clase boton
#@dataclass
#class Boton:
#    acorde: str
#    pin: int
#    tonica: int

#C3 en midi es 48. Se usará como punto de referencia para todas las otras notas
C3 = 48

# Crear los objetos de los Botones del circulo exterior
boton_out_0 = ("CMaj", 0, C3)
boton_out_1 = ("C#Maj", 1, C3+1)
boton_out_2 = ("DMaj", 2, C3+2)
boton_out_3 = ("D#Maj", 3, C3+3)
boton_out_4 = ("EMaj", 4, C3+4)
boton_out_5 = ("FMaj", 5, C3+5)
boton_out_6 = ("F#Maj", 6, C3+6)
boton_out_7 = ("GMaj", 7, C3+7)
boton_out_8 = ("G#Maj", 8, C3+8)
boton_out_9 = ("AMaj", 9, C3+9)
boton_out_10 = ("A#Maj", 10, C3+10)
boton_out_11 = ("BMaj", 11, C3+11)

# Crear los objetos de los Botones del circulo exterior
boton_in_0 = ("Cmin", 0, C3)
boton_in_1 = ("C#min", 1, C3+1)
boton_in_2 = ("Dmin", 2, C3+2)
boton_in_3 = ("D#min", 3, C3+3)
boton_in_4 = ("Emin", 4, C3+4)
boton_in_5 = ("Fmin", 5, C3+5)
boton_in_6 = ("F#min", 6, C3+6)
boton_in_7 = ("Gmin", 7, C3+7)
boton_in_8 = ("G#min", 8, C3+8)
boton_in_9 = ("Amin", 9, C3+9)
boton_in_10 = ("A#min", 10, C3+10)
boton_in_11 = ("Bmin", 11, C3+11)

# Crear Lista que incluya todos los botones
outterCircleList = [boton_out_0, boton_out_1, boton_out_2, boton_out_3, boton_out_4, boton_out_5, boton_out_6, boton_out_7, boton_out_8, boton_out_9, boton_out_10, boton_out_11]
innerCircleList = [boton_in_0, boton_in_1, boton_in_2, boton_in_3, boton_in_4, boton_in_5, boton_in_6, boton_in_7, boton_in_8, boton_in_9, boton_in_10, boton_in_11]

# Crear Circulo exterior e interior.
outterCirle =[mcpOutterCircle, outterCircleList]
innerCirle =[mcpInnerCircle, innerCircleList]

# Test. Como leer el estado actual de un botón?
print(mcpOutterCircle.pin(boton_in_0[1]))

# Function para impimir el estado de un circulo completo (12 Botones)
def printCircleState(mcp, circle):
    for boton in circle:
        if mcp.pin(boton[1]) is False:
            print(boton[0] , "\t is ON")
        else:
            print(boton[0], "\t is OFF")

printCircleState(mcpOutterCircle, outterCircleList)
printCircleState(mcpInnerCircle, innerCircleList)

"""
for boton in outterCircleList:
   print(mcpOutterCircle.pin(boton[1]))
"""
