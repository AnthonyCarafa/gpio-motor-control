# GPIO-Motor-Control
This is a very basic script to control motor drivers such as the L298N or similar devices with ease. It leverages the use of the gpiozero Python library.

Although gpiozero already has a built-in motor controlling systen, there are certain limitations. For example, when using PWM to control speed, the built-in "Motor" class in the library forces you to use hardware PWM GPIO pins (PWM0 or PWM1 on the Raspberry Pi). This is impractical, especially during experiments. Having your own class with a similar system also allows you to modify certain things to fit your project's needs.

## Example
Let's create an imaginary workspace:
- You are using an L298N motor driver
- The IN1 pin is connected to GPIO14
- The IN2 pin is connected to GPIO15
- The ENA pin is connected to GPIO18

Now you want to move the motor forward for 5 seconds, pause for 2 seconds, and then go backwards for 5 seconds. You'd add this code to the ``main.py`` file:
```py

motor = Motor(14, 15, 18)

motor.forward()
print("Moving forward for 5 seconds...")
sleep(5)
print("Pausing for 2 seconds...")
motor.stop()
sleep(2)
print("Moving backwards for 5 seconds...")
motor.backwards()
sleep(5)
print("Done!")
```

Thank you for taking the time to read this! If you have any questions, feel free to add me on Discord (anthonyssh) and ask away :)
