"""
.. module:: sh01

***************
 SH01 Module
***************

This is a Module for the `SH01 <https://wiki.xinabox.cc/SH01_-_Capacitive_Touch>`_ capacitive touch sensor.
The board is based off the CAP1296 capacitive touch sensor controller manufactured by Microchip Technology.
The board uses I2C for communication.

Data Sheets:

- `CAP1296 <http://ww1.microchip.com/downloads/en/DeviceDoc/00001569B.pdf>`_

    """

import i2c

CAP_TOUCH_GENERAL_STATUS = 0x02 
CAP_TOUCH_SENSOR_INPUT_STATUS = 0x03

class SH01(i2c.I2C):
    """

===============
SH01 class
===============

.. class:: SH01(i2cdrv, addr=0x28, clk=100000)

    Creates an intance of a new SH01.

    :param i2cdrv: I2C Bus used '( I2C0, ... )'
    :param addr: Slave address, default 0x28
    :param clk: Clock speed, default 100kHz

    """
    def __init__(self, drvname=I2C0,addr=0x28,clk=100000):
        i2c.I2C.__init__(self, drvname, addr, clk)
        self._addr = addr
        try:
            self.start()
        except PeripheralError as e:
            print(e)
            
    def init(self):
        '''
.. method:: init(self)
        
        Configures the registers of CAP1296.
        Call before using SH01

        '''     
        self.write_bytes(0x27, 0x00) 
        self.write_bytes(0x21, 0x39) 
        self.write_bytes(0x00, 0x00)
        
    def touched(self):
        '''
.. method:: touched(self)

        Detects a touch on all four buttons.

        Returns the button touched as a string data type.

        '''
        anyButtonTouched = self.write_read(CAP_TOUCH_GENERAL_STATUS, 1)[0] 
        #print(anyButtonTouched)
        response = '0'
        if anyButtonTouched == 33: 
            #print(anyButtonTouched)
            button = self.write_read(CAP_TOUCH_SENSOR_INPUT_STATUS, 1)[0]
            if button == 0x01:
                #print(button)
                response = 'triangle'
            if button == 0x20:
                #print(button)
                response = 'circle'
            if button == 0x08:
                #print(button)
                response = 'cross'
            if button == 0x10:
                #print(button)
                response = 'square'
            sleep(200)
            self.write_bytes(0x00, 0x00)
        else:
            pass
            #print('no touch detected')
            
        return response
        
        
        

    
    