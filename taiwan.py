#!/usr/bin/python3
from time import sleep
import piglow
import random

piglow.auto_update = True
piglow.all( 0 )


def taipei():
    count = 0
    while ( count < 7 ):
        x = 0
        while ( x < 6 ):
            piglow.led( x + 1, 100 )
            piglow.led( x + 7, 100 )
            piglow.led( x + 13,100 )
            sleep( 0.1 )
            piglow.led( x + 1, 0 )
            piglow.led( x + 7, 0 )
            piglow.led( x + 13,0 )
            x = x + 1
        count = count + 1

def kaohsiung():
    count = 0
    while ( count < 6 ):
        x = 0
        while ( x < 18 ):
            piglow.led( x + 1, 100)
            sleep( 0.1 )
            piglow.led( x + 1, 0)
            x = x + 1
        count = count + 1

def taichung():
    v = 0
    while ( v < 2 ):
        count = 0
        target = 6
        y = 1
        z = 0
        while ( z < 6 ):
            x = 6
            while ( count < target ):
                piglow.led( x + 0, 100 )
                piglow.led( x + 6, 100 )
                piglow.led( x + 12, 100 )

                if target == 0:
                    pass
                else:
                    sleep( 0.1 )
                    piglow.led( x + 0, 0 )
                    piglow.led( x + 6, 0 )
                    piglow.led( x + 12, 0 )
                    count = count + 1
                    x = x - 1
            piglow.led( y + 0, 100 )
            piglow.led( y + 6, 100 )
            piglow.led( y + 12, 100 )
            target = target - 1
            count = 0
            z = z + 1
            y = y + 1

        count = 0
        x = 6
        while ( count < 6 ):
            piglow.led( x, 0 )
            piglow.led( 6 + x, 0 )
            piglow.led( 12 + x, 0 )
            sleep( 0.1 )
            count = count + 1
            x = x - 1
        v = v + 1

def tainan():
    count = 0
    while ( count < 6 ):
        x = 1
        while ( x < 6 ):
            piglow.led( x + 0, 100 )
            piglow.led( x + 6, 100 )
            piglow.led( x + 12, 100 )
            sleep( 0.1 )
            piglow.led( x + 0, 0 )
            piglow.led( x + 6, 0 )
            piglow.led( x + 12, 0 )
            x = x + 1
        x = 6
        while ( x > 0 ):
            piglow.led( x + 0, 100 )
            piglow.led( x + 6, 100 )
            piglow.led( x + 12, 100 )
            sleep( 0.1 )
            piglow.led( x + 0, 0 )
            piglow.led( x + 6, 0 )
            piglow.led( x + 12, 0 )
            x = x - 1
        count += 1

def taidung():
    count = 0
    while ( count < 3 ):
        x = 1
        for i in range(18):
            piglow.led( x, 100 )
            sleep( 0.1 )
            piglow.led( x, 0 )
            x = x + 1
        count += 1

def hsinchu():
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

        
def taiwan( cities ):
    random.shuffle( cities )
    return( cities )

if __name__ == '__main__':
    list1 = [ taipei(),kaohsiung(),taichung() ]
    list2 = [ tainan(),taidung(),hsinchu() ]
    cities = list1 + list2
    taiwan( cities )

#        


