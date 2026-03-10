# S1 SDD - NeoPixels


## Introduction

A micro:bit can be used to control [NeoPixels](https://www.adafruit.com/category/168).


## Set up


### Extra Code

The `neopixel` extension needs to be installed.

![Extension](assets/neopixels1.png "Extension")

![Extension](assets/neopixels2.png "Extension")


### On start

To set up the NeoPixel the `Neopixel at pin` block is used.  The default values are:

* variable name is `strip`
* pin for commands is `P0`
* number of LEDs is 24

![on start](assets/neopixels3.png "on start")


## Display

### On button A pressed

To change all the LEDs to one colour, `show color` is used.  Various colours are available in the drop down list.

![on button A](assets/neopixels4.png "on button A")


### On button B pressed

To change all the LEDs to a rainbow, `show rainbow` is used.

![on button B](assets/neopixels5.png "on button B")


### On button A+B pressed

To rotate all the LEDs on the strip, `rotate pixel by` is used.
Nothing will until the `show` command is used.

![on button A+B](assets/neopixels6.png "on button A+B")
