.. module:: sh01

***************
 SH01 Module
***************

This is a Module for the `SH01 <https://wiki.xinabox.cc/SH01_-_Capacitive_Touch>`_ capacitive touch sensor.
The board is based off the CAP1296 capacitive touch sensor controller manufactured by Microchip Technology.
The board uses I2C for communication.

Data Sheets:

- `CAP1296 <http://ww1.microchip.com/downloads/en/DeviceDoc/00001569B.pdf>`_

    
===============
SH01 class
===============

.. class:: SH01(i2cdrv, addr=0x28, clk=100000)

    Creates an intance of a new SH01.

    :param i2cdrv: I2C Bus used '( I2C0, ... )'
    :param addr: Slave address, default 0x28
    :param clk: Clock speed, default 100kHz

    
.. method:: init(self)
        
        Configures the registers of CAP1296.
        Call before using SH01

        
.. method:: touched(self)

        Detects a touch on all four buttons.

        Returns the button touched as a string data type.

        
