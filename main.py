from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

class Motor:
    a = False
    def __init__(self, in_pin_1, in_pin_2, en_pin):
        self.en = PWMOutputDevice(en_pin)
        self.in_pin_1 = DigitalOutputDevice(in_pin_1)
        self.in_pin_2 = DigitalOutputDevice(in_pin_2)

    def forward(self, speed=1):
        self.en.value = speed
        self.in_pin_1.on()
        self.in_pin_2.off()

    def backwards(self, speed=1):
        self.en.value = speed
        self.in_pin_1.off()
        self.in_pin_2.on()

    def stop(self):
        self.en.value = 0
        self.in_pin_1.off()
        self.in_pin_2.off()

test = Motor(1, 2, 3) # replace with real values

test.forward()
sleep(5)
test.backwards()
