*************
XinaBox SH01
*************

The SH01 xChip is a multiple channel capacitive touch sensor controller. It is based on the `CAP1296 <https://www.microchip.com/wwwproducts/en/CAP1296>`_ manufactured by Microchip. Each sensor input is calibrated to compensate for system parasitic capacitance and automatically recalibrated to compensate for gradual environmental changes. In addition, the CAP1296 can be configured to detect proximity on one or more channels with an optional signal guard to reduce noise sensitivity. The CAP1296 includes Multiple Pattern Touch recognition that allows the user to select a specific set of buttons to be touched simultaneously. If this pattern is detected, a status bit is set and an interrupt is generated.

Please note, SH01 and all other xChips is currently only supported in Zerynth Studio with `XinaBox CW02 <https://docs.zerynth.com/latest/official/board.zerynth.xinabox_esp32/docs/index.html>`_. Review the `Quick Start <https://wiki.xinabox.cc/Quick-Start>`_ guide for interfacing xChips.

==================
Technical Details
==================
CAP1296
__________
* Based on CAP1296 From Microchip Technology
* Multiple Button Pattern Detection
* Power Button Support
* Press and Hold Feature for Volume-like Applications
* I2C
* Operating Ambient Temperature Range: -40 to 125 °C
* Storage Temperature Range: -55 to 150 °C

.. include:: __toc.rst


