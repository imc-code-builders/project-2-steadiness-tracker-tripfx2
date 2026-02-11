from microbit import *
import log

# Initialize logging state and set column labels
log.set_labels('x', 'y', 'z')
logging = False
display.show(Image.NO)

while True:
    # TASK 1: Toggle logging on/off with Button A
    if button_a.was_pressed():
        logging = not logging  # Toggle state
        if logging:
            display.show(Image.YES)
        else:
            display.show(Image.NO)

    # TASK 2: Delete the log with Button B
    if button_b.was_pressed():
        log.delete()
        display.show(Image.YES) # Briefly show yes to confirm deletion
        sleep(500)
        display.show(Image.NO)  # Then return to off state
        logging = False

    # TASK 3: Log accelerometer data while logging is True
    if logging:
        log.add(
            x=accelerometer.get_x(),
            y=accelerometer.get_y(),
            z=accelerometer.get_z()
        )
        sleep(100) # 100ms interval