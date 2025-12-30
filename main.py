from gpiozero import PWMOutputDevice, DigitalOutputDevice
from time import sleep

class Motor:
    def __init__(self, in_pin_1, in_pin_2, en_pin): # setup func for the class
        self.en = PWMOutputDevice(en_pin)
        self.in_pin_1 = DigitalOutputDevice(in_pin_1)
        self.in_pin_2 = DigitalOutputDevice(in_pin_2)

    def forward(self, speed=1, time=0): # time being set to 0 = infinite
        if time == 0:
            self.en.value = speed
            self.in_pin_1.on()
            self.in_pin_2.off()
        else:
            self.en.value = speed
            self.in_pin_1.on()
            self.in_pin_2.off()
            sleep(time)

    def backwards(self, speed=1, time=0): # time being set to 0 = infinite
        if time == 0:
            self.en.value = speed
            self.in_pin_1.off()
            self.in_pin_2.on()
        else:
            self.en.value = speed
            self.in_pin_1.off()
            self.in_pin_2.on()
            sleep(time)

    def stop(self):
        self.en.value = 0
        self.in_pin_1.off()
        self.in_pin_2.off()

    def speed(self, speed):
        self.en.value = speed

test = Motor(1, 2, 3) # replace with real values

test.forward(1, 5) # max speed for 5 seconds, then motor shuts off
