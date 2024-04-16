# arduino-theremin

Source code for Arduino midi controller using HC-SR04 ultra-sonic sensors to control midi continuous controller data (WIP).

The previous prototype version used Python scripts to take Arduino sensor input and send midi messages for volume and pitchbend data via the Arduino
serial port (see Pymidi module). Unit tests written using Pytest (type 'pytest' in command line to run).

Code was rewritten in C++ (also included) for performance and to allow device to operate stand-alone with USB connection without any additional software other than a DAW (e.g. Logic, Ableton Live, etc.).
