# S1 SDD - NeoPixels


## Introduction

A [micro:bit](https://makecode.microbit.org/) can be used to control [NeoPixels](https://www.adafruit.com/category/168).


## Set up


### Extra Code

The `neopixel` extension needs to be installed.
This is accessed via `Extensions`.

![Extension](assets/neopixels1.png "Extension")

The required extension is then selected.

![Extension](assets/neopixels2.png "Extension")


### On start

To set up the NeoPixel the `Neopixel at pin` block is used.  The default values are:

* variable name is `strip`
* pin for commands is `P0`
* number of LEDs is 24

The number of LEDs needs to be changed to the number of actual LEDs.

![on start](assets/neopixels3.png "on start")


## Display

### On button A pressed

To change all the LEDs to one colour, `show color` is used.
Various colours are available in the drop down list.

![on button A](assets/neopixels4.png "on button A")


### On button B pressed

To change all the LEDs to a rainbow, `show rainbow` is used.

![on button B](assets/neopixels5.png "on button B")

To only use part of a rainbow, adjust the numbers `1 to 360` to something else, e.g. `90 to 180`.

![rainbow](assets/rainbow.png "rainbow")

### On button A+B pressed

To rotate all the LEDs on the strip, `rotate pixels by` is used.
The LEDs will not rotate until the `show` command is used.

![on button A+B](assets/neopixels6.png "on button A+B")

Compare with `shift pixels by`.


### On shake

To make the LEDs flash a loop is used, with a short pauses after a change of colour.

To turn the LEDs off `clear` is used.
The LEDs will not turn off until the `show` command is used.

![on shake](assets/neopixels7.png "on shake")
