#!/usr/bin/python3
from time import sleep
import piglow
import random

piglow.auto_update = True
piglow.all( 0 )

def colorful_raindrops():
    count = 0
    leds = list(range( 0,18 ))
    random.shuffle( leds )
    while ( count < 3 ):
        for i in leds:
            piglow.led( i, 100 )
            sleep( 0.1 )
        random.shuffle( leds )
        for i in leds:
            piglow.led( i, 0 )
            sleep( 0.1 )
        count += 1

if __name__ == '__main__':
    while True:
        colorful_raindrops()

#        
