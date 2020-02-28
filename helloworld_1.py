# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd

from fpioa_manager import *
from Maix import GPIO

fm.register(board_info.LED_R,fm.fpioa.GPIO0)
fm.register(board_info.LED_G,fm.fpioa.GPIO1)
fm.register(board_info.LED_B,fm.fpioa.GPIO2)

led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
led_g=GPIO(GPIO.GPIO1,GPIO.OUT)
led_b=GPIO(GPIO.GPIO2,GPIO.OUT)

led_r.value(1)
led_g.value(1)
led_b.value(1)

count = 0
lcd.init(freq=15000000)
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    lcd.display(img)                # Display on LCD
    print(clock.fps())              # Note: MaixPy's Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
    if count > 0 and count < 15:
        led_r.value(0)
        led_g.value(1)
        led_b.value(1)
    if count > 15 and count < 30:
        led_r.value(1)
        led_g.value(0)
        led_b.value(1)
    if count > 30 and count < 45:
        led_r.value(1)
        led_g.value(1)
        led_b.value(0)
    if count > 45:
        count=0
    else:
        count+=1
