import utime
from machine import Pin
from micropython import const
import hid

led = Pin(25, Pin.OUT)
state = False

usb = hid.device(0x04D8, 0xFD50)
usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
utime.sleep(1)

while True:
    if state:
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    else:
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x20')  # 'H'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x17')  # 'e'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x24')  # 'l'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x16')  # 'o'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x16')  # ','
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x14')  # ' '
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x12')  # 'W'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x27')  # 'o'
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(0.1))
        usb.send(b'\x00\x00\x00\x00\x00\x00\x00\x00')
        utime.sleep(const(1))

    state = not state
    led.value(state)
    utime.sleep(1)
