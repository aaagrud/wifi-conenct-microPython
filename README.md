# WiFi Connect MicroPython

Simple MicroPython script to scan for available WiFi networks and connect to a specified network using an ESP32 or ESP8266.

## Features
- Scans for available WiFi networks
- Attempts to connect to a specified SSID with a password
- Displays network configuration if connected
- Times out after multiple failed attempts

## Requirements
- A board running MicroPython (ESP32, ESP8266, etc.)
- MicroPython firmware installed
- `network` and `time` modules
