# para usar la libreria del Raspberry Pi Pico:
# 1.- instalar la extensión Pico-W-Go
# 2.- ir al menu View -> Command Palette -> Pico-W-Go - Configure project
# 3.- escribir: from machine import Pin, I2C

#incluir librerias necesariar para el proyecto
from machine import UART
from machine import Pin, I2C
import mcp23017
from dataclasses import dataclass

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

# Crear Clase boton
@dataclass
class Boton:
    acorde: str
    pin: int
    tonica: int

# Crear los objetos de los Botones del circulo exterior
boton_0 = Boton("CMaj", 0, 48)
boton_1 = Boton("C#Maj", 1, 49)
boton_2 = Boton("DMaj", 2, 50)
boton_3 = Boton("D#Maj", 3, 51)
boton_4 = Boton("EMaj", 4, 52)
boton_5 = Boton("FMaj", 5, 53)
boton_6 = Boton("F#Maj", 6, 54)
boton_7 = Boton("GMaj", 7, 55)
boton_8 = Boton("G#Maj", 8, 56)
boton_9 = Boton("AMaj", 9, 57)
boton_10 = Boton("A#Maj", 10, 58)
boton_11 = Boton("BMaj", 11, 59)

# Test. Como leer el estado actual de un botón?
mcpOutterCircle.