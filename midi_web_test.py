import machine
import time
import ustruct

pin = machine.Pin(25, machine.Pin.OUT)
uart = machine.UART(0,31250)
uart.init(31250, bits=8, parity=None, stop=1)


notes = [60,61,62,63,64,63,62,61]

msg = b'\x90\x3C\x01'
uart.write(msg)

while True:
  for x in notes:
    pin.value(1)
    uart.write(msg)
    time.sleep(0.5)
  
    """

    uart.write(ustruct.pack("bbb",0x90,0x3C,0x01))
    time.sleep(0.5)
    pin.value(0)
    time.sleep(0.5)
    uart.write(ustruct.pack("bbb",0x80,0x3C,0x3D))

    """