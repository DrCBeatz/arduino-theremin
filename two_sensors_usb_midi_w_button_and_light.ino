/*
 * 
 *
 * Created: 4/6/2015 10:47:08 AM
 * Author: gurbrinder grewal
 * Modified by Arduino LLC (2015)
 * 
 * Modified by Derek Pritchett
 * with Bryne Carruthers
 * 2022 
 * for Arduino Theremin project
 * arduinotheremin.com
 */ 

#include "MIDIUSB.h"
const int echoPin = 4;
const int trigPin = 5;

const int echoPin2 = 6;
const int trigPin2 = 7;
const int  buttonPin = 10;    // the pin that the pushbutton is attached to
const int ledPin = 12;       // the pin that the LED is attached to
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button
int noteState =0;
// First parameter is the event type (0x09 = note on, 0x08 = note off).
// Second parameter is note-on/note-off, combined with the channel.
// Channel can be anything between 0-15. Typically reported to the user as 1-16.
// Third parameter is the note number (48 = middle C).
// Fourth parameter is the velocity (64 = normal, 127 = fastest).

void noteOn(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOn = {0x09, 0x90 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOn);
}

void noteOff(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOff = {0x08, 0x80 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOff);
}

void pitchBend(int channel,int value) {
      if (value > 0x3FFF) {
        value = 0;
    }

  byte lowValue = value & 0x7F;
  byte highValue = value >> 7;
  midiEventPacket_t event = {0x0E, 0xE0 | channel, lowValue, highValue};
  MidiUSB.sendMIDI(event);
  MidiUSB.flush();
}


void setup() {

  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

// First parameter is the event type (0x0B = control change).
// Second parameter is the event type, combined with the channel.
// Third parameter is the control number number (0-119).
// Fourth parameter is the control value (0-127).

void controlChange(byte channel, byte control, byte value) {
  midiEventPacket_t event = {0x0B, 0xB0 | channel, control, value};
  MidiUSB.sendMIDI(event);
  MidiUSB.flush();
}

float readSensorDataVolume(){
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);  
  int distance = pulseIn(echoPin, HIGH)/58;  //58 Equivalent to (340m/s*1us)/2
  Serial.println(distance);
  int correctedInput = (min(distance,60)*1.7)+30;
  return correctedInput;
}


float readSensorDataPitch(){
  digitalWrite(trigPin2, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);  
  unsigned int distance = pulseIn(echoPin2, HIGH)/58;  //58 Equivalent to (340m/s*1us)/2
  Serial.println("pitch value " + distance);
  int correctedInput = min(distance,60)*273;
  return correctedInput; 
}

void loop() {
buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button went from off to on:
      buttonPushCounter++;
      Serial.println("on");
      Serial.print("number of button pushes: ");
      Serial.println(buttonPushCounter);
    } else {
      // if the current state is LOW then the button went from on to off:
      Serial.println("off");
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = buttonState;

 unsigned int volumeValue = readSensorDataVolume();
 unsigned int pitchValue = readSensorDataPitch();

     pitchBend(0,pitchValue);
   MidiUSB.flush();
  controlChange(0x00,7,volumeValue);
  MidiUSB.flush();
  delay(10);

  MidiUSB.flush();
   delay(10);

    if (buttonPushCounter % 2 == 1) {
    digitalWrite(ledPin, HIGH);
    //turn on LED and start playing note
    if (noteState == 0 ){
      noteOn(0, 60, 64); 
      noteState =1;
    }
  } else {
    digitalWrite(ledPin, LOW);
    if (noteState == 1) {
      noteOff(0, 60, 64); 
      noteState = 0;
    }
  }
}
