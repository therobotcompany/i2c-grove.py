#!/usr/bin/env python
#
# Copyright (c) 2014 OpenElectrons.com
# Explorer example script.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author        Comments
# 04/15/14  Michael       Initial authoring.
#

import time
import os, sys
import explorerlib

print "Connect I2C device..."
time.sleep(3)
addr = 0x00     # DO NOT change this address!!!
i2c = explorerlib.Explorer(addr)
found = i2c.ping(0x00)

# Checks for connection on all I2C addresses until connection is found
while found == -1:
    if (addr < 0xef):
        addr = addr + 1
        i2c = explorerlib.Explorer(addr)
        found = i2c.ping(0x00)
    else:
        addr = 0x00

print "--------------------"
print "7 bit address: " + str(hex(addr/2))      # RaspberryPi will find device at this address
print "8 bit address: " + str(hex(addr))        # Use this address for use with OpenElectrons_i2c.py 
print i2c.GetFirmwareVersion()
print i2c.GetVendorName()
print i2c.GetDeviceId()
print "--------------------"

#Press Pause/Break button on your keyboard to stop the program
