##############################################
#   This is an example for SH01 capacitive
#   touch sensor.
#
#   A touch input is detected on SH01 and 
#   printed out on the console.
##############################################

import streams
from xinabox.sh01 import sh01

streams.serial()

# SH01 instance
SH01 = sh01.SH01(I2C0)

# configure SH01
SH01.init()

while True:
    button = SH01.touched()         # return which button is pressed
    if button  == 'square':         # square touched
        print('SQUARE TOUCHED')
    elif button == 'triangle':      # triangle touched
        print('TRIANGLE TOUCHED')
    elif button == 'circle':        # circle touched
        print('CIRCLE TOUCHED')
    elif button == 'cross':         # cross touched
        print('CROSS TOUCHED')
    
    sleep(100)