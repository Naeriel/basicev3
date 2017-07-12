#!/usr/bin/env python3


import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
from time import sleep

# Load Screen
lcd = ev3.Screen()
lcd.draw.text((10,10), 'My name is Cristina', font=fonts.load("luBS14"))
lcd.draw.text((20,10), 'I am an engineer', font=fonts.load("luBS14"))
lcd.update()
sleep(2)