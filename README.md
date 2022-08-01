# arduino-theremin

Source code for prototype of Arduino midi controller using HC-SR04 ultra-sonic sensors to control midi continuous controller data (WIP).

Current version uses Python scripts to take Arduino sensor input and send midi messages for volume and pitchbend data via the Arduino
serial port (see Pymidi module).

Unit tests written using Pytest (type 'pytest' in command line to run).

Currently rewriting code in C++ (also included).
