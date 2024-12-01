# Connecting a cheap "Laser Light Show" to Home Assistant with ESPHome

This is my final configuration and hardware setup to connect a cheap "Laser Light Show" to Home Assistant using ESPHome using the DMX512 protocol.

This should work with both an ESP8266 and ESP32.

## Hardware

- Laser Light Show (I got this from (AliExpress)[https://www.aliexpress.com/item/1005005721491027.html])
- ESP8266 or ESP32 (I used a Wemos D1 Mini Pro)
- RS485 to TTL module, there are many options, this is (one of the ones that worked)[https://www.aliexpress.com/item/1893567852.html] - there are more suitable ones designer for 3.3v
- DMX 3 Pin Female Plug 

Plus a power supply, wires etc.

## Wiring

The wiring is pretty simple, connect the RS485 module to the ESP8266 as follows:

- ESP8266 5v -> RS485 VCC
- ESP8266 GND -> RS485 GND
- ESP8266 GPIO2 (D4) -> RS485 DI

*DO NOT* connect from the RS485 data output to the ESP as it is 5v and may damage the ESP. 

Connecting the laser light show is also simple, connect
- RS485 A -> XLR 3 (DMX +)
- RS485 B -> XLR 2 (DMX -)

The XLR pin numbers are printed on the XLR connectors.

Optionally, you can also connect the ground wire (although I didn't need it, but for longer runs it might be necessary):
- RS485 GND -> XLR 1 (GND)

See the included `dmx.yaml` for the full ESPHome configuration.

I have everything configured as a light as it was simple for me to work with, and nothing needed each step of the 255 range.

# Changing the pattern etc

Once ESPhome is installed and flashed on to the ESP, connect it to Home Assistant, once connected to Home Assistant, you can change the pattern/position/color etc by adjusting the brightness of the light entities that will be shown.

Referring to the included tables of channels and effects, you need to "scale down" the numbers (eg: 255 = 100%, 128 = 50%, 0 = 0%) to get the desired effect.

So to get a manually selected christmas tree pattern, in red, select the following brightnesses:

- Mode: 25% (64)
- Pattern: 34% (87)
- Color: 44% (112)

# Things I Learnt

- The RS485 module I used was 5v, and the VCC rail needed to match, however a 3.3v signal was enough to drive it.
- I needed the `force_full_frames: true` option set in the ESPHome configuration to get the DMX to work correctly.
- So it starts up in the right mode, I needed to get the back LCD to say "A001", an then _press "Enter"_ to get it save, and keep that mode at startup.