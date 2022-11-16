# import machine
# from machine import Pin


class clsMode:
    allModes = []
    def __init__(self, pinNumber: int, modeName : str):
        self.pinNumber = pinNumber
        self.name = modeName
        self.allModes.append(modeName)
        # self.allModes.append(self)
        # self.Pin = machine.Pin(pinNumber, machine.Pin.IN, pull = Pin.PULL_UP)
        self.Pin = 8

#declare posible modes
mode0 = clsMode(6, 'Gated')
mode0 = clsMode(7, 'Latched')
mode0 = clsMode(8, 'Clock')
# print(mode0.name)
# print(mode0.pinNumber)

print(len(clsMode.allModes))
print(clsMode.allModes[1])

