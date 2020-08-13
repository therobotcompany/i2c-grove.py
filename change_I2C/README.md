Tutorial [How to change I2C Address using Raspberry Pi](http://www.mindsensors.com/content/54-how-to-change-i2c-address-using-raspberry-pi)

```
$ i2cdetect -y 1
$ sudo pip install OpenElectrons_i2c
$ python explorer.py
```
Follow on screen instructions, program will display both 7 and 8-bit formats and device information

## Change the I2C to a custom one
>`$ ./addresschange (i2c address) (new i2c address)`

1. Program will then find the device with current i2c address and display device information
1. Program will then change the i2c address
1. Program will attempt to find the device with new i2c address and display device information.

