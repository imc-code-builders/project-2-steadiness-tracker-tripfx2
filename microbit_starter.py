from microbit import *
import log

log.set_labels('x', 'y', 'z')
logging = False
display.show(Image.NO)

while True:

    # TASK 1: Toggle logging on/off with Button A
    # Press once to start logging (set logging = True, show Image.YES)
    # Press again to stop (set logging = False, show Image.NO)
    if button_a.was_pressed():
        pass

    # TASK 2: Delete the log with Button B
    if button_b.was_pressed():
        pass

    # TASK 3: Log accelerometer data while logging is True
    # Log x, y, z values and sleep for 100ms between readings
    if logging:
        pass