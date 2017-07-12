import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
from time import sleep
while True
    lcd = ev3.Screen()
    lcd.update()
    lcd.draw.text((10,10), 'Hello World!', font=fonts.load("luBS14"))
    sleep(2)