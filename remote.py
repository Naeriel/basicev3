#!/usr/bin/env python3
""" 
    remote.py: Checks which button is pressed
    Author: Cristina Serrano Gonzalez (Naeriel)
"""

import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
from time import sleep

remote = ev3.RemoteControl(sensor=None, channel=1)
lcd = ev3.Screen()

while True:
    if remote.red_up:
        lcd.draw.text((10,10), 'Red Up', font=fonts.load("luBS14"))
        lcd.update()
        sleep(5)
    else:
        lcd.draw.text((10,10), 'None pressed', font=fonts.load("luBS14"))
        lcd.update()
        sleep(5)