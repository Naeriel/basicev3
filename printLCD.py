#!/usr/bin/env python3
""" 
    printLCD.py: Prints a message into EV3 LCD screen
    Author: Cristina Serrano Gonzalez (Naeriel)
"""

import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
from time import sleep

# Load Screen function and write a text
lcd = ev3.Screen()
lcd.draw.text((10,10), 'My name is Cristina', font=fonts.load("luBS14"))
lcd.draw.text((10,25), 'I am an engineer', font=fonts.load("luBS14"))
lcd.update()
sleep(2)